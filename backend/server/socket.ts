import { Server } from "socket.io";
import authorization from "../middleware/socketAuthorization";
import socketLib from "../lib/socketLib";

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

    socket.on("leaveCourse", async (courseId: string) => {
      try {
        await socket.leave(courseId);
      } catch {
        socket.emit("error", { message: "error leaving course" });
      }
    });
  });
};

export default socketApi;
