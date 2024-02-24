import { NextFunction, Request, Response } from "express";
import { StatusCodes } from "http-status-codes";
import jwt from "jsonwebtoken";
import User from "../models/users";

const authorization = async (req: any, res: Response, next: NextFunction) => {
  let token = req.headers.authorization;
  const key = process.env.KEY;

  if (token && typeof key == "string") {
    try {
      token = token.replace("Bearer", "").trim();
      const payload: any = jwt.verify(token, key);
      const user = await User.findById(payload.email);

      if (user) {
        req.user = user;
        next();
      } else
        return res
          .status(StatusCodes.UNAUTHORIZED)
          .json({ message: "unauthorized" });
    } catch (err) {
      console.log(err);
      res.status(StatusCodes.UNAUTHORIZED).json({ message: "Invalid Token" });
    }
  } else res.status(StatusCodes.UNAUTHORIZED).json({ message: "unauthorized" });
};

export default authorization;
