import express from "express";
import userHandlers from "../handlers/users";

const userRouter = express.Router();

userRouter.post("/", userHandlers.createUser);

export default userRouter;
