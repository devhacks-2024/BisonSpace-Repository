import StudyRoom from "../models/studyRooms";
import { Response } from "express";
import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";

const studyRoom = {
  async createStudyRoom(req: any, res: Response) {
    let { type, users, name, courseId } = req.body;
    if (!(type && users && name && courseId))
      return res
        .status(StatusCodes.BAD_REQUEST)
        .json({ message: "all fields must be filled correctly" });
    const course = await Course.findById(courseId);
    if (!course)
      return res
        .status(StatusCodes.NOT_FOUND)
        .json({ message: "course not found" });
    if (type == "public") users = course.users;
  },
};
