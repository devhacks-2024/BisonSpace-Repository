import express from "express";
import studyRoomHandler from "../handlers/studyRoom";
import authorization from "../middleware/authorization";

const studyRoomRouter = express.Router();

studyRoomRouter.post("/", authorization, studyRoomHandler.createStudyRoom);

export default studyRoomRouter;
