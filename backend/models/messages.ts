import mongoose from "mongoose";

const messageSchema = new mongoose.Schema({
  timeStamp: { default: Date.now, type: Number },
  body: String,
  sender: { type: String, ref: "User" },
  location: { type: String, enum: ["studyRoom", "course"] },
  locationId: { type: String, refPath: "location" },
});

const Message = mongoose.model("Message", messageSchema);
export default Message;
