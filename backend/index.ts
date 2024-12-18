const express = require("express");
const app = express();

const port = 5000;

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.get("/userLogin", (req, res) => {
  res.send("Here is the code");
});

app.listen(port, () => {
  console.log(`Listening on port: http//:localhost:${port}/`);
});
