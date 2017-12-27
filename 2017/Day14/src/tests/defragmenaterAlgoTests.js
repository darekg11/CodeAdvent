const assert = require("assert");
const defragmenterAlgo = require("../defragmenterAlgo");

describe("countGroups", () => {
  it("should return 1242 for test input", done => {
    const binaryValues = [];
    for (let cnt = 0; cnt < 128; cnt += 1) {
      const binary = defragmenterAlgo.getBinaryValue("flqrgnkx", cnt);
      binaryValues.push(binary);
    }
    const result = defragmenterAlgo.countGroups(binaryValues);
    assert.equal(result, 1242);
    done();
  }).timeout(10000);
});
