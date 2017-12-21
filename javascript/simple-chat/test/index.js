"use restrict";

import http from "http";
import assert from "assert";

import "../lib/app.js";

describe("Testando se o servidor está rodando:", () => {
  it("deveria retornar status code 200", done => {
    http.get("http://localhost:3000", res => {
      assert.equal(200, res.statusCode);
      done();
    });
  });
});
