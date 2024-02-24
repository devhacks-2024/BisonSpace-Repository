import mongoose from "mongoose";

const assignmentSchema = new mongoose.Schema({
  type: { type: String, enum: ["written", "programming"] },
  created: { type: Number, default: Date.now },
  body: String,
  language: { type: String },
  shouldKeep: { type: Boolean, default: false },
});

const Assignment = mongoose.model("Assignment", assignmentSchema);
export default Assignment;
