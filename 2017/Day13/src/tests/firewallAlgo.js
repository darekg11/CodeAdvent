const assert = require("assert");
const firewallAlgo = require("../firewallAlgo");

describe("parseInput", () => {
  it("should return { 1: 1, 22, 120 } for `[1: 1, 22: 120]`", () => {
    const result = firewallAlgo.parseInput(["1: 1", "22: 120"]);
    assert.equal(result["1"], 1);
    assert.equal(result["22"], 120);
  });
});

describe("runSimulation", () => {
  it("should return 24 for test input", () => {
    const dataObject = firewallAlgo.parseInput([
      "0: 3",
      "1: 2",
      "4: 4",
      "6: 4"
    ]);
    const result = firewallAlgo.runSimulation(dataObject);
    assert.equal(result, 24);
  });
});

describe("calculateDelayToRunWithoutDetection", () => {
  it("should return 10 for test input", () => {
    const dataObject = firewallAlgo.parseInput([
      "0: 3",
      "1: 2",
      "4: 4",
      "6: 4"
    ]);
    const result = firewallAlgo.calculateDelayToRunWithoutDetection(dataObject);
    assert.equal(result, 10);
  });
});
