const assert = require("assert");
const offsetJumperAlgo = require("../offsetJumperAlgo");

describe("countRequiredJumpsToExitList", () => {
  it("should return 5 for [0, 3, 0, 1, -3]", () => {
    const result = offsetJumperAlgo.countRequiredJumpsToExitList([
      0,
      3,
      0,
      1,
      -3
    ]);

    assert.equal(result, 5);
  });
});

describe("countRequiredJumpsToExitListWithDecreasing", () => {
  it("should return 10 for [0, 3, 0, 1, -3]", () => {
    const result = offsetJumperAlgo.countRequiredJumpsToExitListWithDecreasing([
      0,
      3,
      0,
      1,
      -3
    ]);

    assert.equal(result, 10);
  });
});
