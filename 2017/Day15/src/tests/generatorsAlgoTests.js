const assert = require("assert");
const generatorsAlgo = require("../generatorsAlgo");

describe("runGenerator", () => {
  it("should return 588 for test inpit", done => {
    const result = generatorsAlgo.runGenerator(65, 8921, 16807, 48271);
    assert.equal(result, 588);
    done();
  }).timeout(2000000);

  it("should return 592 for input", done => {
    const result = generatorsAlgo.runGenerator(277, 349, 16807, 48271);
    assert.equal(result, 592);
    done();
  }).timeout(2000000);
});

describe("runPickyGenerator", () => {
  it("should return 309 for test inpit", done => {
    const result = generatorsAlgo.runPickyGenerator(65, 8921, 16807, 48271);
    assert.equal(result, 309);
    done();
  }).timeout(2000000);

  it("should return 320 for input", done => {
    const result = generatorsAlgo.runPickyGenerator(277, 349, 16807, 48271);
    assert.equal(result, 320);
    done();
  }).timeout(2000000);
});
