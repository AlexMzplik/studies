import express from "express";
import http from "http";

const app = express();
const server = http.Server(app);
const port = 3000;
server.listen(port, () => {
  console.log(`Simple chat started at ${port}`);
});
