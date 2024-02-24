import express from "express";
import userHandlers from "../handlers/users";
import authorization from "../middleware/authorization";

const userRouter = express.Router();

userRouter.post("/", userHandlers.createUser);
userRouter.post("/addCourses", authorization, userHandlers.addCourses);
userRouter.get("/courses", authorization, userHandlers.getCourses);
userRouter.get("/", authorization, userHandlers.getSelf);

export default userRouter;
