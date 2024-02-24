import { Request, Response } from "express";
import User from "../models/users";

interface RequestObject extends Request {
  user: UserInterface;
}

interface UserInterface {
  _id: string;
  password: string;
  firstName: string;
  lastName: string;
  defaultProfileColor: string;
  courses: string[];
  registrationDate: number;
}

export { RequestObject };
