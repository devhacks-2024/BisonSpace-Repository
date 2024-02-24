import http from "http";
import express from "express";
import dotenv from "dotenv";
import connectToDatabase from "./lib/mongoconnect";
import rest from "./server/rest";
import { Server } from "socket.io";
import socketApi from "./server/socket";
// import createCourses from "./test";

dotenv.config();

try {
  connectToDatabase();
  // createCourses();

  const app = express();
  let io;

  rest(app);
  const httpServer = http.createServer(app);
  io = new Server(httpServer);
  socketApi(io);

  httpServer.listen(process.env.HTTP_PORT, () => {
    console.log(
      "\x1b[32m%s\x1b[0m",
      `[+] HTTP server running on port ${process.env.HTTP_PORT}`
    );
  });
} catch (error) {
  console.log("[x] failed to start server");
}
