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

  //   async getPreviousGroupMessages(groupId: string) {
  //     try {
  //       const studyRoom = await StudyRoom.findById(groupId).populate({
  //         path: "messages",
  //         populate: {
  //           path: "sender",
  //           select: "_id firstName lastName defaultProfileColor",
  //         },
  //       });
  //       if (!studyRoom) return [];
  //       const messages = studyRoom.messages;
  //       return messages;
  //     } catch (error) {
  //       return [];
  //     }
  //   },

  async getStudyRoomAssignment(groupId: string) {
    try {
      const studyRoom = await StudyRoom.findById(groupId).populate<{
        assignment: any;
      }>({
        path: "assignment",
      });
      if (studyRoom) {
        console.log(studyRoom);
        const assignment = studyRoom.assignment;
        console.log(assignment);
        return assignment;
      }
    } catch (error) {
      console.log(error);
    }
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
      console.log(location, locationId, body);
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
        const course = await Course.findById(locationId).populate({
          path: "messages",
          populate: {
            path: "sender",
            select: "_id firstName lastName defaultProfileColor",
          },
        });
        io.to(locationId).emit("newMessage", course?.messages);
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
