import { Request, Response } from "express";
import { RequestObject } from "../lib/types";
import User from "../models/users";
import Helpers from "../lib/helpers";
import { StatusCodes } from "http-status-codes";
import Course from "../models/courses";

const userHandlers = {
  async createUser(req: Request, res: Response) {
    try {
      const { firstName, lastName, email, password } = req.body;
      if (!(firstName && lastName && email && password)) {
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "you must fill in all required fields" });
      }
      let user = await User.findById(email);
      if (user) {
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "profile already exists" });
      }
      user = new User({
        _id: email,
        password: Helpers.passwordHasher(password),
        firstName: firstName,
        lastName: lastName,
      });
      await user.save();
      res
        .status(StatusCodes.CREATED)
        .json({ message: "profile created successfuly" });
    } catch (error) {
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },
  //   async getUser(req:Request, res:Response){
  //     try{
  //         const {user} = req.query
  //     }
  //     catch(error){
  //         res
  //         .status(StatusCodes.INTERNAL_SERVER_ERROR)
  //         .json({ message: "Server Error" });
  //     }
  //   }

  async addCourses(req: any, res: Response) {
    try {
      const { courses } = req.body;
      if (courses && courses instanceof Array) {
        const courseAddProcess = courses.map(async (course: string) => {
          const foundCourse = await Course.findById(course);
          if (foundCourse) {
            if (!foundCourse.users.includes(req.user._id)) {
              req.user.courses.push(course);
              foundCourse.users.push(req.user._id);
              await foundCourse.save();
            }
          }
        });
        await Promise.all(courseAddProcess);
        await req.user.save();
        res
          .status(StatusCodes.OK)
          .json({ message: "courses added successfuly" });
      } else {
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "you must fill in all required fields correctly" });
      }
    } catch (error) {
      console.log(error);
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },

  async getCourses(req: any, res: Response) {
    try {
      const user = await User.findById(req.user._id)
        .select({ courses: 1 })
        .populate({ path: "courses", select: "_id name" });
      if (!user)
        return res
          .status(StatusCodes.NOT_FOUND)
          .json({ message: "User not found" });
      res.status(StatusCodes.OK).json({ courses: user.courses });
    } catch (error) {
      console.log(error);
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },

  updateUser(req: Request, res: Response) {},
};

export default userHandlers;
