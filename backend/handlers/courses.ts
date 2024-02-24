import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";
import { Request, Response } from "express";

const courseHandler = {
  async getCourses(req: Request, res: Response) {
    try {
      const courses = await Course.find();
      res.status(StatusCodes.OK).json({ courses });
    } catch (error) {
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "server error" });
    }
  },
};

export default courseHandler;
