import mongoose from "mongoose";

const assignmentSchema = new mongoose.Schema({
  type: { type: String, enum: ["written", "programming"] },
  created: { type: Number, default: Date.now },
  description: String,
  body: String,
  language: { type: String },
  shouldKeep: { type: Boolean, default: false },
  name: String,
});

const Assignment = mongoose.model("Assignment", assignmentSchema);
export default Assignment;
