const assert = require("assert");
const hexAlgo = require("../hexAlgo");

describe("calculateMinimumAmmountOfSteps", () => {
  it("should return 3 steps for [ne,ne,ne]", () => {
    const result = hexAlgo.calculateMinimumAmmountOfSteps(["ne", "ne", "ne"]);
    assert.equal(result.minimumSteps, 3);
  });

  it("should return 0 steps for [ne,ne,sw,sw]", () => {
    const result = hexAlgo.calculateMinimumAmmountOfSteps([
      "ne",
      "ne",
      "sw",
      "sw"
    ]);
    assert.equal(result.minimumSteps, 0);
  });

  it("should return 2 steps for [ne,ne,s,s]", () => {
    const result = hexAlgo.calculateMinimumAmmountOfSteps([
      "ne",
      "ne",
      "s",
      "s"
    ]);
    assert.equal(result.minimumSteps, 2);
  });

  it("should return 3 steps for [se,sw,se,sw,sw]", () => {
    const result = hexAlgo.calculateMinimumAmmountOfSteps([
      "se",
      "sw",
      "se",
      "sw",
      "sw"
    ]);
    assert.equal(result.minimumSteps, 3);
  });
});
