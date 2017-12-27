const assert = require("assert");
const danceAlgo = require("../danceAlgo");

describe("parseInput", () => {
  it("should return all three different operations for three different inputs", () => {
    const input = "x15/10,ph/c,x3/14,s1,pf/b,x12/0,s20,x2/3";
    const result = danceAlgo.parseInput(input);

    assert.equal(result.length, 8);
    assert.equal(result[0].operation, "EXCHANGE");
    assert.equal(result[0].firstArgument, 15);
    assert.equal(result[0].secondArgument, 10);

    assert.equal(result[1].operation, "PARTNER");
    assert.equal(result[1].firstArgument, "h");
    assert.equal(result[1].secondArgument, "c");

    assert.equal(result[2].operation, "EXCHANGE");
    assert.equal(result[2].firstArgument, 3);
    assert.equal(result[2].secondArgument, 14);

    assert.equal(result[3].operation, "SPIN");
    assert.equal(result[3].firstArgument, 1);

    assert.equal(result[4].operation, "PARTNER");
    assert.equal(result[4].firstArgument, "f");
    assert.equal(result[4].secondArgument, "b");

    assert.equal(result[5].operation, "EXCHANGE");
    assert.equal(result[5].firstArgument, 12);
    assert.equal(result[5].secondArgument, 0);

    assert.equal(result[6].operation, "SPIN");
    assert.equal(result[6].firstArgument, 20);

    assert.equal(result[7].operation, "EXCHANGE");
    assert.equal(result[7].firstArgument, 2);
    assert.equal(result[7].secondArgument, 3);
  });
});

describe("spin", () => {
  it("should move only last element when spinIdex is 1", () => {
    const spinOperation = {
      operation: "SPIN",
      firstArgument: 1
    };
    const danceState = "abcdef";

    const result = danceAlgo.spin(danceState, spinOperation);

    assert.equal(danceState.length, 6);
    assert.equal(danceState[0], "a");
    assert.equal(danceState[1], "b");
    assert.equal(danceState[2], "c");
    assert.equal(danceState[3], "d");
    assert.equal(danceState[4], "e");
    assert.equal(danceState[5], "f");

    assert.equal(result.length, 6);
    assert.equal(result[0], "f");
    assert.equal(result[1], "a");
    assert.equal(result[2], "b");
    assert.equal(result[3], "c");
    assert.equal(result[4], "d");
    assert.equal(result[5], "e");
  });

  it("should move only last 3 elements when spinIdex is 3", () => {
    const spinOperation = {
      operation: "SPIN",
      firstArgument: 3
    };
    const danceState = "abcdef";

    const result = danceAlgo.spin(danceState, spinOperation);

    assert.equal(danceState.length, 6);
    assert.equal(danceState[0], "a");
    assert.equal(danceState[1], "b");
    assert.equal(danceState[2], "c");
    assert.equal(danceState[3], "d");
    assert.equal(danceState[4], "e");
    assert.equal(danceState[5], "f");

    assert.equal(result.length, 6);
    assert.equal(result[0], "d");
    assert.equal(result[1], "e");
    assert.equal(result[2], "f");
    assert.equal(result[3], "a");
    assert.equal(result[4], "b");
    assert.equal(result[5], "c");
  });
});

describe("exchange", () => {
  it("should swap two elements and leave input not modified", () => {
    const exchangeOperation = {
      operation: "EXCHANGE",
      firstArgument: 1,
      secondArgument: 2
    };
    const danceState = "abcdef";

    const result = danceAlgo.exchange(danceState, exchangeOperation);

    assert.equal(danceState.length, 6);
    assert.equal(danceState[0], "a");
    assert.equal(danceState[1], "b");
    assert.equal(danceState[2], "c");
    assert.equal(danceState[3], "d");
    assert.equal(danceState[4], "e");
    assert.equal(danceState[5], "f");

    assert.equal(result.length, 6);
    assert.equal(result[0], "a");
    assert.equal(result[1], "c");
    assert.equal(result[2], "b");
    assert.equal(result[3], "d");
    assert.equal(result[4], "e");
    assert.equal(result[5], "f");
  });
});

describe("partner", () => {
  it("should swap two elements and leave input not modified", () => {
    const partnerOperation = {
      operation: "PARTNER",
      firstArgument: "d",
      secondArgument: "a"
    };
    const danceState = "abcdef";

    const result = danceAlgo.partner(danceState, partnerOperation);

    assert.equal(danceState.length, 6);
    assert.equal(danceState[0], "a");
    assert.equal(danceState[1], "b");
    assert.equal(danceState[2], "c");
    assert.equal(danceState[3], "d");
    assert.equal(danceState[4], "e");
    assert.equal(danceState[5], "f");

    assert.equal(result.length, 6);
    assert.equal(result[0], "d");
    assert.equal(result[1], "b");
    assert.equal(result[2], "c");
    assert.equal(result[3], "a");
    assert.equal(result[4], "e");
    assert.equal(result[5], "f");
  });
});
