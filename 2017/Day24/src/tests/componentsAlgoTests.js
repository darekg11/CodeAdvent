const assert = require("assert");
const componentsAlgo = require("../componentsAlgo");

describe("bridgeInfo", () => {
  it("should return 31 as strongest bridge and 19 as strongest longest bridge for test input", () => {
    const components = componentsAlgo.parseInput([
      "0/2",
      "2/2",
      "2/3",
      "3/4",
      "3/5",
      "0/1",
      "10/1",
      "9/10"
    ]);
    const result = componentsAlgo.bridgeInfo(components);
    assert.equal(result.strongest, 31);
    assert.equal(result.strongestLongestBridge, 19);
  });
});
