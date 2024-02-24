import express from "express";
import studyRoomHandler from "../handlers/studyRoom";
import authorization from "../middleware/authorization";

const studyRoomRouter = express.Router();

studyRoomRouter.get("/", authorization, studyRoomHandler.getStudyRooms);
studyRoomRouter.post(
  "/assignment",
  authorization,
  studyRoomHandler.createAssignment
);
studyRoomRouter.post("/", authorization, studyRoomHandler.createStudyRoom);

export default studyRoomRouter;
