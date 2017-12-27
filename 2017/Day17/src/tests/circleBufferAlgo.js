const assert = require("assert");
const circleBuffer = require("../circleBufferAlgo");

describe("startBuffering", () => {
  it("should return 638 for test input", () => {
    const result = circleBuffer.startBuffering(3);
    assert.equal(result, 638);
  });

  it("should return 1912 for input", () => {
    const result = circleBuffer.startBuffering(355);
    assert.equal(result, 1912);
  });
});

describe("findValueAfterZero", () => {
  it("should return 21066990 for input", () => {
    const result = circleBuffer.findValueAfterZero(355);
    assert.equal(result, 21066990);
  });
});
