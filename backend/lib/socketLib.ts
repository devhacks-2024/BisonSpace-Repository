import Course from "../models/courses";
import User from "../models/users";
import Message from "../models/messages";
import StudyRoom from "../models/studyRooms";

import { Server } from "socket.io";

const socketLib = {
  async getPreviousMessages(courseId: string, userId: string) {
    const user = await User.findById(userId);
    if (!user) return [];
    if (!user.courses.includes(courseId)) return [];
    const course = await Course.findById(courseId).populate({
      path: "messages",
      populate: {
        path: "sender",
        select: "_id firstName lastName defaultProfileColor",
      },
    });
    if (!course) return [];
    const messages = course.messages;
    return messages;
  },

  async sendMessage(
    location: string,
    locationId: string,
    userId: string,
    body: string,
    socket: any,
    io: Server
  ) {
    try {
      let foundLocation;
      if (location == "course") {
        foundLocation = await Course.findById(locationId);
      } else if (location == "studyRoom") {
        foundLocation = await StudyRoom.findById(locationId);
      } else {
        socket.emit("error", { message: "room not found" });
      }

      if (foundLocation) {
        let message = new Message({
          body,
          sender: userId,
          location: location,
          locationId: locationId,
        });
        message = await message.save();
        foundLocation.messages.push(message._id);
        await foundLocation.save();
        message = await message.populate({
          path: "sender",
          select: "_id , firstName, lastName, defaultProfileColor ",
        });
        io.to(locationId).emit("newMessage", message);
        if (!foundLocation.users.includes(userId)) {
          socket.emit("error", {
            message: "you do not belong in this location",
          });
        }
      } else {
        socket.emit("error", { message: "room not found" });
      }
    } catch (error) {
      socket.emit("error", { message: "could not send message" });
    }
  },
};

export default socketLib;
