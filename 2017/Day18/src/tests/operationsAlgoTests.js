const assert = require("assert");
const operationsAlgo = require("../operationsAlgo");

describe("executeProgram", () => {
  it("should return 4 for test input", () => {
    const result = operationsAlgo.executeProgram([
      "set a 1",
      "add a 2",
      "mul a a",
      "mod a 5",
      "snd a",
      "set a 0",
      "rcv a",
      "jgz a -1",
      "set a 1",
      "jgz a -2"
    ]);

    assert.equal(result, 4);
  });
});

describe("executeProgramTwiceAtTheSameTime", () => {
  it("should return 3 for test input", () => {
    const result = operationsAlgo.executeProgramTwiceAtTheSameTime([
      "snd 1",
      "snd 2",
      "snd p",
      "rcv a",
      "rcv b",
      "rcv c",
      "rcv d"
    ]);

    assert.equal(result, 3);
  });
});
