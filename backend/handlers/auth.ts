import { StatusCodes } from "http-status-codes";
import User from "../models/users";
import { Request, Response } from "express";
import Helpers from "../lib/helpers";

const authHandler = {
  async authenticate(req: Request, res: Response) {
    try {
      const { email, password } = req.body;
      const user = await User.findById(email).select({ email: 1, password: 1 });
      if (!user)
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "incorrect email/password combination" });
      if (user.password !== Helpers.passwordHasher(password))
        return res
          .status(StatusCodes.BAD_REQUEST)
          .json({ message: "incorrect email/password combination" });
      const token = Helpers.generateUserToken({ email });
      res.status(StatusCodes.OK).json({ token });
    } catch (error) {
      res
        .status(StatusCodes.INTERNAL_SERVER_ERROR)
        .json({ message: "Server Error" });
    }
  },
};

export default authHandler;
