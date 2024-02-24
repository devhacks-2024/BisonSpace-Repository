import express from "express";
import authHandler from "../handlers/auth";

const authRouter = express.Router();

authRouter.post("/", authHandler.authenticate);

export default authRouter;
