const assert = require("assert");
const memoryAllocAlgo = require("../memoryAllocAlgo");

describe("countRequiredCyclesToFindDuplicatedSequence", () => {
  it("should return 5 for [0, 2, 7, 0]", () => {
    const result = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequence([
      0,
      2,
      7,
      0
    ]);

    assert.equal(result, 5);
  });

  it("should return 3156 for [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]", () => {
    const result = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequence([
      2,
      8,
      8,
      5,
      4,
      2,
      3,
      1,
      5,
      5,
      1,
      2,
      15,
      13,
      5,
      14
    ]);

    assert.equal(result, 3156);
  });
});

describe("countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate", () => {
  it("should return 4 for [0, 2, 7, 0]", () => {
    const result = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate(
      [0, 2, 7, 0]
    );

    assert.equal(result, 4);
  });

  it("should return 1610 for [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]", () => {
    const result = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate(
      [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    );

    assert.equal(result, 1610);
  });
});
