import jwt from "jsonwebtoken";
import User from "../models/users";
import { ExtendedError } from "socket.io/dist/namespace";

const authorization = async (
  socket: any,
  next: (err?: ExtendedError | undefined) => void
) => {
  let token = socket.handshake.auth.token;
  const key = process.env.KEY;
  if (token && typeof key == "string") {
    try {
    console.log(token)
      token = token.replace("Bearer", "").trim();
      const payload: any = jwt.verify(token, key);
      const user = await User.findById(payload.email);
      if (user) {
        socket.userId = user._id;
        next();
      } else return socket.emit("conn_error", new Error("not authorized"));
    } catch (err) {
      console.log("connection error", err);
      socket.emit("conn_error", new Error("server error"));
    }
  } else {
    console.log("connection error, invalid token");
    socket.emit("conn_error", new Error("invalid token"));
  }
};

export default authorization;
