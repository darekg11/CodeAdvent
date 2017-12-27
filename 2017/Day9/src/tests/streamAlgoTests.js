const assert = require("assert");
const streamAlgo = require("../streamAlgo");

describe("countInputGroupScore", () => {
  it("should return 1 for single group with no garbage", () => {
    const input = "{}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 1);
  });

  it("should return 6 for single triple nested empty group", () => {
    const input = "{{{}}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 6);
  });

  it("should return 5 for single group with two seprate groups", () => {
    const input = "{{},{}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 5);
  });

  it("should return 16 for big nested input", () => {
    const input = "{{{},{},{{}}}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 16);
  });

  it("should return 1 for single group that has only garbage", () => {
    const input = "{<a>,<a>,<a>,<a>}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 1);
  });

  it("should return 9 for single group that has only multiple groups with garbage", () => {
    const input = "{{<ab>},{<ab>},{<ab>},{<ab>}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 9);
  });

  it("should return 9 for single group that has only multiple groups with garbage including escape character", () => {
    const input = "{{<!!>},{<!!>},{<!!>},{<!!>}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 9);
  });

  it("should return 3 for single group that has only multiple groups with garbage including escape character before closing garbage section", () => {
    const input = "{{<a!>},{<a!>},{<a!>},{<ab>}}";
    const result = streamAlgo.countInputGroupScore(input);

    assert.equal(result, 3);
  });
});

describe("countGarbageCount", () => {
  it("should return 0 for <>", () => {
    const input = "<>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 0);
  });

  it("should return 17 for <random characters>", () => {
    const input = "<random characters>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 17);
  });

  it("should return 3 for <<<<>", () => {
    const input = "<<<<>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 3);
  });

  it("should return 2 for <{!>}>", () => {
    const input = "<{!>}>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 2);
  });

  it("should return 0 for <!!>", () => {
    const input = "<!!>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 0);
  });

  it("should return 0 for <!!!>>", () => {
    const input = "<!!!>>";
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 0);
  });

  it('should return 10 for <{o"i!a,<{i<a>', () => {
    const input = '<{o"i!a,<{i<a>';
    const result = streamAlgo.countGarbageCount(input);

    assert.equal(result, 10);
  });
});
