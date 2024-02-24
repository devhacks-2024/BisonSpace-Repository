import { Request, Response } from "express";
import User from "../models/users";
import Helpers from "../lib/helpers";
import { StatusCodes } from "http-status-codes";

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
      user.save();
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
  addCourses(req: Request, res: Response) {},
  updateUser(req: Request, res: Response) {},
};

export default userHandlers;
