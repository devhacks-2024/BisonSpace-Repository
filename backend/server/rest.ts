import bodyParser from "body-parser";
import { Express } from "express";

const rest = (app: Express) => {
  app.use(bodyParser.json());
  app.get("/", (req, res) => {
    res.send("Hello world");
  });
};

export default rest;
