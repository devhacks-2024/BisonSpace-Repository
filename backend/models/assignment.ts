import mongoose from "mongoose";

const assignmentSchema = new mongoose.Schema({
  type: { type: String, enum: ["written", "programming"] },
  created: { type: Number, default: Date.now },
  file: {
    file: { type: Buffer, required: true },
    filename: { type: String },
    mimetype: { type: String, required: true },
  },
  language: { type: String },
  shouldKeep: { type: Boolean, default: false },
});

const Assignment = mongoose.model("Assignment", assignmentSchema);
export default Assignment;
