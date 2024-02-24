import { Server } from "socket.io";
import authorization from "../middleware/socketAuthorization";
import socketLib from "../lib/socketLib";
import Assignment from "../models/assignment";

const socketApi = (io: Server) => {
  console.log("socket lib started");
  io.use(authorization);
  io.on("connection", (socket: any) => {
    console.log("user connected");

    socket.on("join_course", async (courseId: string) => {
      const previousMessages = await socketLib.getPreviousMessages(
        courseId,
        socket.userId
      );
      socket.emit("previousCourseMessages", previousMessages);
      socket.join(courseId);
    });

    socket.on(
      "sendMessage",
      async ({
        location,
        locationId,
        body,
      }: {
        location: string;
        locationId: string;
        body: string;
      }) => {
        await socketLib.sendMessage(
          location,
          locationId,
          socket.userId,
          body,
          socket,
          io
        );
      }
    );

    socket.on("leaveCourses", async (courseId: string) => {
      try {
        for (let room of socket.rooms) {
          console.log(room);
          await socket.leave(room);
        }
      } catch {
        socket.emit("error", { message: "error leaving course" });
      }
    });

    socket.on("join_studyRoom", async (groupId: string) => {
      try {
        const studyRoomAssignment = await socketLib.getStudyRoomAssignment(
          groupId
        );
        if (studyRoomAssignment) {
          socket.join(studyRoomAssignment._id);
        }

        socket.emit("studyRoomAssignment", { studyRoomAssignment });
      } catch (error) {
        socket.emit("error", { message: "error leaving course" });
      }
    });

    // socket.on("change_assignment_text", async (assignmentID ))
  });
};

export default socketApi;
