import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";
import { Request, Response } from "express";

const courseHandler = {
  async getCourses(req: Request, res: Response) {
    try {
      const courses = await Course.find().select({ name: 1, _id: 1 });
      res.status(StatusCodes.OK).json({ courses });
    } catch (error) {
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "server error" });
    }
  },

  async getAllUsersInCourse(req: Request, res: Response) {
    try {
      const { courseId } = req.params;

      const course = await Course.findById(courseId).populate({
        path: "users",
        select: "_id firstName lastName",
      });
      if (!course)
        return res
          .status(StatusCodes.NOT_FOUND)
          .json({ message: "course not found" });
      const usersInCourse = course.users;
      res.status(StatusCodes.OK).json({ users: usersInCourse });
    } catch (error) {
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "server error" });
    }
  },
};

export default courseHandler;
