import Course from "../models/courses";
import User from "../models/users";

const socketLib = {
  async getPreviousMessages(courseId: string, userId: string) {
    const user = User.findById(userId);
    const course = await Course.findById(courseId).populate({
      path: "messages",
      populate: {
        path: "sender",
        select: "_id firstName lastName defaultProfileColor",
      },
    });
    if (!course) return [];
    const messages = course.messages;
    return messages;
  },

  async sendMessage(
    location: string,
    locationId: string,
    userId: string,
    body: string
  ) {},
};

export default socketLib;
