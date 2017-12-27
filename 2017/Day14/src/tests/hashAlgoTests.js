const assert = require("assert");
const hashAlgo = require("../hashAlgo");

describe("getIndexWrappingList", () => {
  it("should return 0 for accessing 6 index for 6 length array", () => {
    const result = hashAlgo.getIndexWrappingList(6, 6);
    assert.equal(result, 0);
  });

  it("should return 2 for accessing 8 index for 6 length array", () => {
    const result = hashAlgo.getIndexWrappingList(8, 6);
    assert.equal(result, 2);
  });

  it("should return 1 for accessing 25 index for 6 length array", () => {
    const result = hashAlgo.getIndexWrappingList(25, 6);
    assert.equal(result, 1);
  });

  it("should return 1 for accessing 1 index for 6 length array", () => {
    const result = hashAlgo.getIndexWrappingList(1, 6);
    assert.equal(result, 1);
  });
});

describe("substringListWithWrapping", () => {
  it("should return [1,2,3,4] for indexStart 0, endIndex 3", () => {
    const result = hashAlgo.substringListWithWrapping([1, 2, 3, 4], 0, 3);
    assert.equal(result.length, 4);
    assert.equal(result[0], 1);
    assert.equal(result[1], 2);
    assert.equal(result[2], 3);
    assert.equal(result[3], 4);
  });

  it("should return [2,3] for indexStart 1, endIndex 2", () => {
    const result = hashAlgo.substringListWithWrapping([1, 2, 3, 4], 1, 2);
    assert.equal(result.length, 2);
    assert.equal(result[0], 2);
    assert.equal(result[1], 3);
  });

  it("should return [3,4,1,2] for indexStart 2, endIndex 1", () => {
    const result = hashAlgo.substringListWithWrapping([1, 2, 3, 4], 2, 1);
    assert.equal(result.length, 4);
    assert.equal(result[0], 3);
    assert.equal(result[1], 4);
    assert.equal(result[2], 1);
    assert.equal(result[3], 2);
  });

  it("should return [4] for indexStart 3, endIndex 3", () => {
    const result = hashAlgo.substringListWithWrapping([1, 2, 3, 4], 3, 3);
    assert.equal(result.length, 1);
    assert.equal(result[0], 4);
  });
});

describe("insertSubListToList", () => {
  it("should return [1,2,3,4] as original, [1,2,3,4] as replacement for indexStart 0, endIndex 3", () => {
    const result = hashAlgo.insertSubListToList(
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      0,
      3
    );
    assert.equal(result.length, 4);
    assert.equal(result[0], 1);
    assert.equal(result[1], 2);
    assert.equal(result[2], 3);
    assert.equal(result[3], 4);
  });

  it("should return [1,2,3,4] as original, [3] as replacement for indexStart 2, endIndex 2", () => {
    const result = hashAlgo.insertSubListToList([1, 2, 3, 4], [3], 2, 2);
    assert.equal(result.length, 4);
    assert.equal(result[0], 1);
    assert.equal(result[1], 2);
    assert.equal(result[2], 3);
    assert.equal(result[3], 4);
  });

  it("should return [3,4,1,2], [1,2,3,4] as original, [1,2,3,4] as replacement for indexStart 2, endIndex 1", () => {
    const result = hashAlgo.insertSubListToList(
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      2,
      1
    );
    assert.equal(result.length, 4);
    assert.equal(result[0], 3);
    assert.equal(result[1], 4);
    assert.equal(result[2], 1);
    assert.equal(result[3], 2);
  });
});

describe("hashInput", () => {
  it("should return 4114 for input [165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153] hashing values [0...255]", () => {
    const hashingValues = [...Array(256).keys()];
    const result = hashAlgo.hashInput(
      hashingValues,
      [165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153],
      1
    );
    const multiplication = result[0] * result[1];
    assert.equal(multiplication, 4114);
  });
});

describe("Calculate hex hash", () => {
  it("should return `a2582a3a0e66e6e86e3812dcb672a272` as 64 rounds for empty input", () => {
    const hashingValues = [...Array(256).keys()];
    const stringInputAsciiCodes = ""
      .split("")
      .map(singlElement => singlElement.charCodeAt())
      .concat([17, 31, 73, 47, 23]);
    const result = hashAlgo.hashInput(hashingValues, stringInputAsciiCodes, 64);
    const denseHash = hashAlgo.calculateDenseHash(result);
    const hexValue = hashAlgo.getHexRepresentation(denseHash);
    assert.equal(hexValue, "a2582a3a0e66e6e86e3812dcb672a272");
  });

  it("should return `33efeb34ea91902bb2f59c9920caa6cd` as 64 rounds for AoC 2017", () => {
    const hashingValues = [...Array(256).keys()];
    const stringInputAsciiCodes = "AoC 2017"
      .split("")
      .map(singlElement => singlElement.charCodeAt())
      .concat([17, 31, 73, 47, 23]);
    const result = hashAlgo.hashInput(hashingValues, stringInputAsciiCodes, 64);
    const denseHash = hashAlgo.calculateDenseHash(result);
    const hexValue = hashAlgo.getHexRepresentation(denseHash);
    assert.equal(hexValue, "33efeb34ea91902bb2f59c9920caa6cd");
  });

  it("should return `3efbe78a8d82f29979031a4aa0b16a9d` as 64 rounds for 1,2,3", () => {
    const hashingValues = [...Array(256).keys()];
    const stringInputAsciiCodes = "1,2,3"
      .split("")
      .map(singlElement => singlElement.charCodeAt())
      .concat([17, 31, 73, 47, 23]);
    const result = hashAlgo.hashInput(hashingValues, stringInputAsciiCodes, 64);
    const denseHash = hashAlgo.calculateDenseHash(result);
    const hexValue = hashAlgo.getHexRepresentation(denseHash);
    assert.equal(hexValue, "3efbe78a8d82f29979031a4aa0b16a9d");
  });

  it("should return `63960835bcdc130f0b66d7ff4f6a5a8e` as 64 rounds for 1,2,4", () => {
    const hashingValues = [...Array(256).keys()];
    const stringInputAsciiCodes = "1,2,4"
      .split("")
      .map(singlElement => singlElement.charCodeAt())
      .concat([17, 31, 73, 47, 23]);
    const result = hashAlgo.hashInput(hashingValues, stringInputAsciiCodes, 64);
    const denseHash = hashAlgo.calculateDenseHash(result);
    const hexValue = hashAlgo.getHexRepresentation(denseHash);
    assert.equal(hexValue, "63960835bcdc130f0b66d7ff4f6a5a8e");
  });

  it("should return `2f8c3d2100fdd57cec130d928b0fd2dd` as 64 rounds for 165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153", () => {
    const hashingValues = [...Array(256).keys()];
    const stringInputAsciiCodes = "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153"
      .split("")
      .map(singlElement => singlElement.charCodeAt())
      .concat([17, 31, 73, 47, 23]);
    const result = hashAlgo.hashInput(hashingValues, stringInputAsciiCodes, 64);
    const denseHash = hashAlgo.calculateDenseHash(result);
    const hexValue = hashAlgo.getHexRepresentation(denseHash);
    assert.equal(hexValue, "2f8c3d2100fdd57cec130d928b0fd2dd");
  });
});
