const assert = require("assert");
const towerAlgo = require("../towerAlgo");

describe("parseInput", () => {
  it("should return correct data for test input", () => {
    const result = towerAlgo.parseInput([
      "pbga (66)",
      "xhth (57)",
      "ebii (61)",
      "havc (66)",
      "ktlj (57)",
      "fwft (72) -> ktlj, cntj, xhth",
      "qoyq (66)",
      "padx (45) -> pbga, havc, qoyq",
      "tknk (41) -> ugml, padx, fwft",
      "jptl (61)",
      "ugml (68) -> gyxo, ebii, jptl",
      "gyxo (61)",
      "cntj (57)"
    ]);

    assert.equal(result.towerWeights.length, 13);
    assert.equal(result.towerWeights[0].weight, 66);
    assert.equal(result.towerWeights[0].towerName, "pbga");
    assert.equal(result.towerWeights[1].weight, 57);
    assert.equal(result.towerWeights[1].towerName, "xhth");
    assert.equal(result.towerWeights[2].weight, 61);
    assert.equal(result.towerWeights[2].towerName, "ebii");
    assert.equal(result.towerWeights[3].weight, 66);
    assert.equal(result.towerWeights[3].towerName, "havc");
    assert.equal(result.towerWeights[4].weight, 57);
    assert.equal(result.towerWeights[4].towerName, "ktlj");
    assert.equal(result.towerWeights[5].weight, 72);
    assert.equal(result.towerWeights[5].towerName, "fwft");
    assert.equal(result.towerWeights[6].weight, 66);
    assert.equal(result.towerWeights[6].towerName, "qoyq");
    assert.equal(result.towerWeights[7].weight, 45);
    assert.equal(result.towerWeights[7].towerName, "padx");
    assert.equal(result.towerWeights[8].weight, 41);
    assert.equal(result.towerWeights[8].towerName, "tknk");
    assert.equal(result.towerWeights[9].weight, 61);
    assert.equal(result.towerWeights[9].towerName, "jptl");
    assert.equal(result.towerWeights[10].weight, 68);
    assert.equal(result.towerWeights[10].towerName, "ugml");
    assert.equal(result.towerWeights[11].weight, 61);
    assert.equal(result.towerWeights[11].towerName, "gyxo");
    assert.equal(result.towerWeights[12].weight, 57);
    assert.equal(result.towerWeights[12].towerName, "cntj");

    assert.equal(result.towerRelations.length, 13);
    assert.equal(result.towerRelations[0].subTowers.length, 0);
    assert.equal(result.towerRelations[0].towerName, "pbga");
    assert.equal(result.towerRelations[1].subTowers.length, 0);
    assert.equal(result.towerRelations[1].towerName, "xhth");
    assert.equal(result.towerRelations[2].subTowers.length, 0);
    assert.equal(result.towerRelations[2].towerName, "ebii");
    assert.equal(result.towerRelations[3].subTowers.length, 0);
    assert.equal(result.towerRelations[3].towerName, "havc");
    assert.equal(result.towerRelations[4].subTowers.length, 0);
    assert.equal(result.towerRelations[4].towerName, "ktlj");

    assert.equal(result.towerRelations[5].subTowers.length, 3);
    assert.equal(result.towerRelations[5].subTowers[0], "ktlj");
    assert.equal(result.towerRelations[5].subTowers[1], "cntj");
    assert.equal(result.towerRelations[5].subTowers[2], "xhth");
    assert.equal(result.towerRelations[5].towerName, "fwft");

    assert.equal(result.towerRelations[6].subTowers.length, 0);
    assert.equal(result.towerRelations[6].towerName, "qoyq");

    assert.equal(result.towerRelations[7].subTowers.length, 3);
    assert.equal(result.towerRelations[7].subTowers[0], "pbga");
    assert.equal(result.towerRelations[7].subTowers[1], "havc");
    assert.equal(result.towerRelations[7].subTowers[2], "qoyq");
    assert.equal(result.towerRelations[7].towerName, "padx");

    assert.equal(result.towerRelations[8].subTowers.length, 3);
    assert.equal(result.towerRelations[8].subTowers[0], "ugml");
    assert.equal(result.towerRelations[8].subTowers[1], "padx");
    assert.equal(result.towerRelations[8].subTowers[2], "fwft");
    assert.equal(result.towerRelations[8].towerName, "tknk");

    assert.equal(result.towerRelations[9].subTowers.length, 0);
    assert.equal(result.towerRelations[9].towerName, "jptl");

    assert.equal(result.towerRelations[10].subTowers.length, 3);
    assert.equal(result.towerRelations[10].subTowers[0], "gyxo");
    assert.equal(result.towerRelations[10].subTowers[1], "ebii");
    assert.equal(result.towerRelations[10].subTowers[2], "jptl");
    assert.equal(result.towerRelations[10].towerName, "ugml");

    assert.equal(result.towerRelations[11].subTowers.length, 0);
    assert.equal(result.towerRelations[11].towerName, "gyxo");

    assert.equal(result.towerRelations[12].subTowers.length, 0);
    assert.equal(result.towerRelations[12].towerName, "cntj");
  });
});

describe("findBottomTower", () => {
  it("should return tknk for test input", () => {
    const towerRelations = towerAlgo.parseInput([
      "pbga (66)",
      "xhth (57)",
      "ebii (61)",
      "havc (66)",
      "ktlj (57)",
      "fwft (72) -> ktlj, cntj, xhth",
      "qoyq (66)",
      "padx (45) -> pbga, havc, qoyq",
      "tknk (41) -> ugml, padx, fwft",
      "jptl (61)",
      "ugml (68) -> gyxo, ebii, jptl",
      "gyxo (61)",
      "cntj (57)"
    ]).towerRelations;

    const result = towerAlgo.findBottomTower(towerRelations);

    assert.equal(result, "tknk");
  });
});

describe("calculateTowerTotalWeight", () => {
  it("should return 66 for single tower without subtowers", () => {
    const testTower = "test";

    const towerWeights = [
      {
        towerName: "test",
        weight: 66
      }
    ];

    const towerRelations = [
      {
        towerName: "test",
        subTowers: []
      }
    ];

    const result = towerAlgo.calculateTowerTotalWeight(
      testTower,
      towerWeights,
      towerRelations
    );
    assert.equal(result, 66);
  });

  it("should return 243 for tower with subtowers", () => {
    const testTower = "fwft";

    const towerWeights = [
      {
        towerName: "fwft",
        weight: 72
      },
      {
        towerName: "ktlj",
        weight: 57
      },
      {
        towerName: "cntj",
        weight: 57
      },
      {
        towerName: "xhth",
        weight: 57
      }
    ];

    const towerRelations = [
      {
        towerName: "fwft",
        subTowers: ["ktlj", "cntj", "xhth"]
      },
      {
        towerName: "ktlj",
        subTowers: 0
      },
      {
        towerName: "cntj",
        subTowers: 0
      },
      {
        towerName: "xhth",
        subTowers: 0
      }
    ];

    const result = towerAlgo.calculateTowerTotalWeight(
      testTower,
      towerWeights,
      towerRelations
    );
    assert.equal(result, 243);
  });

  it("should return 778 for tower with mutliple subtowers", () => {
    const testTower = "tknk";

    const towerWeights = [
      {
        towerName: "tknk",
        weight: 41
      },
      {
        towerName: "ugml",
        weight: 68
      },
      {
        towerName: "padx",
        weight: 45
      },
      {
        towerName: "fwft",
        weight: 72
      },
      {
        towerName: "gyxo",
        weight: 61
      },
      {
        towerName: "ebii",
        weight: 61
      },
      {
        towerName: "jptl",
        weight: 61
      },
      {
        towerName: "pbga",
        weight: 66
      },
      {
        towerName: "havc",
        weight: 66
      },
      {
        towerName: "qoyq",
        weight: 66
      },
      {
        towerName: "ktlj",
        weight: 57
      },
      {
        towerName: "cntj",
        weight: 57
      },
      {
        towerName: "xhth",
        weight: 57
      }
    ];

    const towerRelations = [
      {
        towerName: "fwft",
        subTowers: ["ktlj", "cntj", "xhth"]
      },
      {
        towerName: "ktlj",
        subTowers: []
      },
      {
        towerName: "cntj",
        subTowers: []
      },
      {
        towerName: "xhth",
        subTowers: []
      },
      {
        towerName: "padx",
        subTowers: ["pbga", "havc", "qoyq"]
      },
      {
        towerName: "pbga",
        subTowers: []
      },
      {
        towerName: "havc",
        subTowers: []
      },
      {
        towerName: "qoyq",
        subTowers: []
      },
      {
        towerName: "tknk",
        subTowers: ["ugml", "padx", "fwft"]
      },
      {
        towerName: "jptl",
        subTowers: []
      },
      {
        towerName: "ebii",
        subTowers: []
      },
      {
        towerName: "ugml",
        subTowers: ["gyxo", "ebii", "jptl"]
      },
      {
        towerName: "gyxo",
        subTowers: []
      }
    ];

    const result = towerAlgo.calculateTowerTotalWeight(
      testTower,
      towerWeights,
      towerRelations
    );
    assert.equal(result, 778);
  });
});

describe("findDifferenceToBalanceTower", () => {
  it("should return 0 for single tower without subtowers", () => {
    const towerWeights = [
      {
        towerName: "test",
        weight: 66
      }
    ];

    const towerRelations = [
      {
        towerName: "test",
        subTowers: []
      }
    ];

    const result = towerAlgo.findDifferenceToBalanceTower(
      towerWeights,
      towerRelations
    );
    assert.equal(result, 0);
  });

  it("should return 0 for tower with subtowers", () => {
    const towerWeights = [
      {
        towerName: "fwft",
        weight: 72
      },
      {
        towerName: "ktlj",
        weight: 57
      },
      {
        towerName: "cntj",
        weight: 57
      },
      {
        towerName: "xhth",
        weight: 57
      }
    ];

    const towerRelations = [
      {
        towerName: "fwft",
        subTowers: ["ktlj", "cntj", "xhth"]
      },
      {
        towerName: "ktlj",
        subTowers: 0
      },
      {
        towerName: "cntj",
        subTowers: 0
      },
      {
        towerName: "xhth",
        subTowers: 0
      }
    ];

    const result = towerAlgo.findDifferenceToBalanceTower(
      towerWeights,
      towerRelations
    );
    assert.equal(result, 0);
  });

  it("should return 60 for tower with mutliple subtowers", () => {
    const towerWeights = [
      {
        towerName: "tknk",
        weight: 41
      },
      {
        towerName: "ugml",
        weight: 68
      },
      {
        towerName: "padx",
        weight: 45
      },
      {
        towerName: "fwft",
        weight: 72
      },
      {
        towerName: "gyxo",
        weight: 61
      },
      {
        towerName: "ebii",
        weight: 61
      },
      {
        towerName: "jptl",
        weight: 61
      },
      {
        towerName: "pbga",
        weight: 66
      },
      {
        towerName: "havc",
        weight: 66
      },
      {
        towerName: "qoyq",
        weight: 66
      },
      {
        towerName: "ktlj",
        weight: 57
      },
      {
        towerName: "cntj",
        weight: 57
      },
      {
        towerName: "xhth",
        weight: 57
      }
    ];

    const towerRelations = [
      {
        towerName: "fwft",
        subTowers: ["ktlj", "cntj", "xhth"]
      },
      {
        towerName: "ktlj",
        subTowers: []
      },
      {
        towerName: "cntj",
        subTowers: []
      },
      {
        towerName: "xhth",
        subTowers: []
      },
      {
        towerName: "padx",
        subTowers: ["pbga", "havc", "qoyq"]
      },
      {
        towerName: "pbga",
        subTowers: []
      },
      {
        towerName: "havc",
        subTowers: []
      },
      {
        towerName: "qoyq",
        subTowers: []
      },
      {
        towerName: "tknk",
        subTowers: ["ugml", "padx", "fwft"]
      },
      {
        towerName: "jptl",
        subTowers: []
      },
      {
        towerName: "ebii",
        subTowers: []
      },
      {
        towerName: "ugml",
        subTowers: ["gyxo", "ebii", "jptl"]
      },
      {
        towerName: "gyxo",
        subTowers: []
      }
    ];

    const result = towerAlgo.findDifferenceToBalanceTower(
      towerWeights,
      towerRelations
    );
    assert.equal(result, 60);
  });
});
