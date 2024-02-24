import StudyRoom from "../models/studyRooms";
import { Response } from "express";
import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";
import Assignment from "../models/assignment";

const studyRoomHandler = {
  async getStudyRooms(req: any, res: Response) {
    const { courseId } = req.body;
    if (!courseId)
      return res
        .status(StatusCodes.BAD_REQUEST)
        .json({ message: "all fields must be filled correctly" });
    const course = await Course.findById(courseId).populate("studyRooms");
    if (!course)
      return res.status(StatusCodes.NOT_FOUND).json({ message: "not found" });
    const studyRooms = course.studyRooms;
    res.status(StatusCodes.OK).json({ studyRooms });
  },

  async createAssignment(req: any, res: Response) {
    try {
      const { name, language, shouldKeep, type, studyRoomId, description } =
        req.body;

      if (!(name && language && type && studyRoomId && description))
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "all fields must be filled correctly" });

      const studyRoom = await StudyRoom.findById(studyRoomId);
      let assignment = new Assignment({
        language,
        body: "",
        shouldKeep,
        type,
        name,
        description,
      });

      if (!studyRoom)
        return res
          .status(StatusCodes.NOT_FOUND)
          .json({ message: "study Room not found" });
      assignment = await assignment.save();
      studyRoom.assignment = assignment._id;
      await studyRoom.save();
      res.status(StatusCodes.OK).json({ message: "assignment created" });
    } catch (error) {
      console.log(error);
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },

  async createStudyRoom(req: any, res: Response) {
    try {
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
      if (!course.users.includes(req.user._id)) {
        return res
          .status(StatusCodes.UNAUTHORIZED)
          .json({ message: "you do not belong in this course" });
      }

      if (type == "public") users = course.users;
      if (type == "private") {
        let allUsersBelongToCourse = true;
        if (users.length == 0) {
          return res
            .status(StatusCodes.BAD_REQUEST)
            .json({ message: "you have to add users to study group" });
        }

        users.forEach((user: string) => {
          if (!course.users.includes(user)) allUsersBelongToCourse = false;
        });
        if (!allUsersBelongToCourse)
          return res
            .status(StatusCodes.BAD_REQUEST)
            .json({ message: "all users added must belong to course" });

        users.push(req.user._id);
      }

      let room = new StudyRoom({
        course: courseId,
        users,
        type,
        name,
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
