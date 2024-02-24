import bodyParser from "body-parser";
import { Express } from "express";
import userRouter from "../routes/users";
import authRouter from "../routes/auth";

const rest = (app: Express) => {
  app.use(bodyParser.json());
  app.use("/api/users", userRouter);
  app.use("/api/auth", authRouter);
};

export default rest;
