import express from "express";
import courseHandler from "../handlers/courses";
import authorization from "../middleware/authorization";

const courseRouter = express.Router();

courseRouter.get("/:courseId/users", courseHandler.getAllUsersInCourse);
courseRouter.get("/", courseHandler.getCourses);

export default courseRouter;
