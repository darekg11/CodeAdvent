const infectionAlgo = require("../infectionAlgo");
const assert = require("assert");

describe("createIntialGridFromMap", () => {
  it("3x3 test input", () => {
    const result = infectionAlgo.createInitialGridFromMap([
      [0, 0, 1],
      [1, 0, 0],
      [0, 0, 0]
    ]);

    assert.equal(result["-1,-1"], 0);
    assert.equal(result["0,-1"], 0);
    assert.equal(result["1,-1"], 1);
    assert.equal(result["-1,0"], 1);
    assert.equal(result["0,0"], 0);
    assert.equal(result["1,0"], 0);
    assert.equal(result["-1,1"], 0);
    assert.equal(result["0,1"], 0);
    assert.equal(result["1,1"], 0);
  });

  it("4x4 test input", () => {
    const result = infectionAlgo.createInitialGridFromMap([
      [0, 0, 1, 1],
      [1, 0, 1, 0],
      [0, 0, 0, 0],
      [1, 1, 1, 1]
    ]);

    assert.equal(result["-2,-2"], 0);
    assert.equal(result["-1,-2"], 0);
    assert.equal(result["0,-2"], 1);
    assert.equal(result["1,-2"], 1);

    assert.equal(result["-2,-1"], 1);
    assert.equal(result["-1,-1"], 0);
    assert.equal(result["0,-1"], 1);
    assert.equal(result["1,-1"], 0);

    assert.equal(result["-2,0"], 0);
    assert.equal(result["-1,0"], 0);
    assert.equal(result["0,0"], 0);
    assert.equal(result["1,0"], 0);

    assert.equal(result["-2,1"], 1);
    assert.equal(result["-1,1"], 1);
    assert.equal(result["0,1"], 1);
    assert.equal(result["1,1"], 1);
  });
});

describe("solveFirstPart", () => {
  it("should return 5587 for test input after 10000 bursts", () => {
    const initialMap = infectionAlgo.parseInput(["..#", "#..", "..."]);
    const result = infectionAlgo.solveFirstPart(initialMap, 10000);
    assert.equal(result, 5587);
  });
});

describe("solveSecondPart", () => {
  it("should return 2511944 for test input after 10000000 bursts", callback => {
    const initialMap = infectionAlgo.parseInput(["..#", "#..", "..."]);
    const result = infectionAlgo.solveSecondPart(initialMap, 10000000);
    assert.equal(result, 2511944);
    callback();
  }).timeout(20000);
});
