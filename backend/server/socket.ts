import { Server } from "socket.io";
import authorization from "../middleware/socketAuthorization";

const socketApi = (io: Server) => {
  io.use(authorization);
  io.on("connection", () => {
    console.log("user connected");
  });
};

export default socketApi;
