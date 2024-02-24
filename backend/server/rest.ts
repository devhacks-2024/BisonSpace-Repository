import bodyParser from "body-parser";
import { Express } from "express";
import userRouter from "../routes/users";
import authRouter from "../routes/auth";
import courseRouter from "../routes/courses";
import studyRoomRouter from "../routes/studyRoom";

const rest = (app: Express) => {
  app.use(bodyParser.json());
  app.use("/api/users", userRouter);
  app.use("/api/auth", authRouter);
  app.use("/api/courses", courseRouter);
  app.use("/api/studyRoom", studyRoomRouter);
};

export default rest;
