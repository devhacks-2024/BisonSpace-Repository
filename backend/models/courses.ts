import mongoose from "mongoose";

const courseSchema = new mongoose.Schema({
  _id: String,
  name: {
    officialName: String,
    shortName: String,
    description: String,
  },
  created: { default: Date.now, type: Number },
  messages: [{ type: mongoose.Schema.Types.ObjectId, ref: "Message" }],
  studyRooms: [{ type: mongoose.Schema.Types.ObjectId, ref: "StudyRoom" }],
  users: [{ type: String, ref: "User" }],
  history: [{ type: mongoose.Schema.Types.ObjectId, ref: "Assignment" }],
});

const Course = mongoose.model("Course", courseSchema);

export default Course;
