import { Server } from "socket.io";
import authorization from "../middleware/socketAuthorization";
import socketLib from "../lib/socketLib";

const socketApi = (io: Server) => {
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

    //socket.on("sendMessage", async({location,}))
  });
};

export default socketApi;
