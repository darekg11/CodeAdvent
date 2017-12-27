const assert = require("assert");
const programAlgo = require("../programAlgo");

describe("parseSingleInputLine", () => {
  it("should return { 1: [1] } for `1 <-> 1", () => {
    const result = programAlgo.parseSingleInputLine("1 <-> 1");
    assert.equal(result["1"].length, 1);
    assert.equal(result["1"][0], 1);
  });

  it("should return { 1: [1,2,3,4] } for `1 <-> 1, 2, 3, 4", () => {
    const result = programAlgo.parseSingleInputLine("1 <-> 1, 2, 3, 4");
    assert.equal(result["1"].length, 4);
    assert.equal(result["1"][0], 1);
    assert.equal(result["1"][1], 2);
    assert.equal(result["1"][2], 3);
    assert.equal(result["1"][3], 4);
  });

  it("should return { 109: [1] } for `109 <-> 1", () => {
    const result = programAlgo.parseSingleInputLine("109 <-> 1");
    assert.equal(result["109"].length, 1);
    assert.equal(result["109"][0], 1);
  });
});

describe("parseInput", () => {
  it("should return { 1: [1] } for `1 <-> 1", () => {
    const result = programAlgo.parseInput(["1 <-> 1"]);
    assert.equal(result["1"].length, 1);
    assert.equal(result["1"][0], 1);
  });

  it("should return { 1: [1], 2: [5, 6, 7, 8] } for [`1 <-> 1`, `2 <-> 5, 6, 7, 8`", () => {
    const result = programAlgo.parseInput(["1 <-> 1", "2 <-> 5, 6, 7, 8"]);
    assert.equal(result["1"].length, 1);
    assert.equal(result["1"][0], 1);
    assert.equal(result["2"].length, 4);
    assert.equal(result["2"][0], 5);
    assert.equal(result["2"][1], 6);
    assert.equal(result["2"][2], 7);
    assert.equal(result["2"][3], 8);
  });
});

describe("findNumberOfProgramsCommunicatingWithProgramZero", () => {
  it("should return 6 for test input", () => {
    const result = programAlgo.parseInput([
      "0 <-> 2",
      "1 <-> 1",
      "2 <-> 0, 3, 4",
      "3 <-> 2, 4",
      "4 <-> 2, 3, 6",
      "5 <-> 6",
      "6 <-> 4, 5"
    ]);

    const connections = programAlgo.findNumberOfProgramsCommunicatingWithProgramZero(
      result
    );
    assert.equal(connections, 6);
  });
});

describe("countAllPossibleGroups", () => {
  it("should return 1 for test input", () => {
    const result = programAlgo.parseInput([
      "0 <-> 2",
      "1 <-> 1",
      "2 <-> 0, 3, 4",
      "3 <-> 2, 4",
      "4 <-> 2, 3, 6",
      "5 <-> 6",
      "6 <-> 4, 5"
    ]);

    const connections = programAlgo.countAllPossibleGroups(result);
    assert.equal(connections, 2);
  });
});
