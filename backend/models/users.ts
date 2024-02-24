import mongoose from "mongoose";
import Helpers from "../lib/helpers";

const userSchema = new mongoose.Schema({
  _id: { type: String, required: true },
  password: { type: String, required: true },
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  defaultProfileColor: {
    type: String,
    default: Helpers.generateHexColorString,
  },
  courses: [{ type: String, ref: "Course" }],
});

const User = mongoose.model("User", userSchema);

export default User;
