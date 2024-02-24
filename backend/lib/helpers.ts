import crypto from "crypto";
import jwt from "jsonwebtoken";

class Helpers {
  static generateUserToken = (payload: any) => {
    const key = process.env.KEY;
    if (typeof key == "string") {
      const token = `Bearer ${jwt.sign(payload, key)}`;
      return token;
    } else throw new Error("could not generate token");
  };

  static passwordHasher = (str: string) => {
    const secret = process.env.HASHING_SECRET;
    if (typeof secret == "string") {
      let hash = crypto.createHmac("sha256", secret).update(str).digest("hex");
      return hash;
    } else {
      throw new Error("hashing secret not found");
    }
  };

  static generateHexColorString = () => {
    const possibleColors = [
      "#59AB83",
      "#79A470",
      "#AA5CBB",
      "#5CB15F",
      "#6888B5",
      "#B48377",
      "#90A2BF",
      "#6D5CB3",
      "#93816B",
      "#876C8B",
      "#895460",
      "#8CA169",
      "#8B7168",
      "#935269",
      "#6F8ABE",
      "#C7C761",
      "#7069B8",
      "#B3B686",
      "#858FAE",
      "#A898B0",
      "#ACA471",
      "#6B8499",
      "#8367C5",
      "#52B0C4",
      "#B38379",
      "#66A2AB",
      "#BD5D9A",
      "#AE7264",
      "#80915E",
      "#A0535A",
      "#9B8661",
      "#597F65",
      "#C29476",
      "#6D6E57",
      "#6C6984",
      "#7F6E64",
      "#918D5F",
      "#7DBFC5",
      "#AF9D5E",
      "#699795",
      "#A4829F",
      "#75B486",
      "#8E6156",
      "#988563",
      "#76719A",
      "#855EAF",
      "#C1A16A",
      "#C0B2BD",
      "#789C6E",
    ];
    const string =
      possibleColors[Math.floor(Math.random() * possibleColors.length)];
    return string;
  };
}

export default Helpers;
