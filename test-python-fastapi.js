import http from "k6/http";
import { sleep, check } from "k6";

export const options = {
  vus: 20,
  duration: "30s",
};

export default function () {
  const url = "http://localhost:8013";

  const params = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  http.get(url);
}
