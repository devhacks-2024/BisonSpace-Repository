import express from "express";
import courseHandler from "../handlers/courses";

const courseRouter = express.Router();

courseRouter.get("/", courseHandler.getCourses);

export default courseRouter;
