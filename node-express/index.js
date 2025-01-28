import express from "express";

const app = express();
const port = 8014;

app.get("/", (req, res) => {
  res.send("Shinomiyaa ( •̀ ω •́ )✧");
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
