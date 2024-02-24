import mongoose from "mongoose";

const studyRoomSchema = new mongoose.Schema({
  assignment: { type: mongoose.Schema.ObjectId, ref: "Assignment" },
  course: { type: mongoose.Schema.ObjectId, ref: "Course" },
  created: { default: Date.now, type: Number },
  users: [{ type: String, ref: "User" }],
  type: { type: String, required: true, enum: ["private", "public"] },
  messages: [{ type: mongoose.Schema.ObjectId, ref: "Message" }],
});

const StudyRoom = mongoose.model("StudyRoom", studyRoomSchema);

export default StudyRoom;
