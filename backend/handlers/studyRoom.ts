import StudyRoom from "../models/studyRooms";
import { Response } from "express";
import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";

const studyRoomHandler = {
  async createStudyRoom(req: any, res: Response) {
    try {
      let { type, users, name, courseId } = req.body;
      console.log(type, users, name, courseId);
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

      let room = new StudyRoom({
        course: courseId,
        users,
        type,
      });
      room = await room.save();
      course.studyRooms.push(room._id);
      await course.save();
      res.status(StatusCodes.CREATED).json({ studyRoomId: room._id });
    } catch (error) {
      console.log(error);
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },
};

export default studyRoomHandler;
