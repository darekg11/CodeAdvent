const assert = require("assert");
const memoryAlgoSolver = require("../memoryAlgoSolver");

describe("getDistanceSpiralingOutwardUp", () => {
  it("should return 0 steps for cell number 1", () => {
    const result = memoryAlgoSolver.getDistanceSpiralingOutwardUp(1);

    assert.equal(result, 0);
  });

  it("should return 3 steps for cell number 12", () => {
    const result = memoryAlgoSolver.getDistanceSpiralingOutwardUp(12);

    assert.equal(result, 3);
  });

  it("should return 2 steps for cell number 23", () => {
    const result = memoryAlgoSolver.getDistanceSpiralingOutwardUp(23);

    assert.equal(result, 2);
  });

  it("should return 31 steps for cell number 1024", () => {
    const result = memoryAlgoSolver.getDistanceSpiralingOutwardUp(1024);

    assert.equal(result, 31);
  });

  it("should return 371 for cell number 368078", () => {
    const result = memoryAlgoSolver.getDistanceSpiralingOutwardUp(368078);

    assert.equal(result, 371);
  });
});

describe("getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell", () => {
  it("should return 10 as first value larger than 5", () => {
    const result = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
      5
    );

    assert.equal(result, 10);
  });

  it("should return 133 as first value larger than 122", () => {
    const result = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
      122
    );

    assert.equal(result, 133);
  });

  it("should return 142 as first value larger than 140", () => {
    const result = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
      140
    );

    assert.equal(result, 142);
  });

  it("should return 806 as first value larger than 800", () => {
    const result = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
      800
    );

    assert.equal(result, 806);
  });

  it("should return 369601 as first value larger than 368078", () => {
    const result = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
      368078
    );

    assert.equal(result, 369601);
  });
});
