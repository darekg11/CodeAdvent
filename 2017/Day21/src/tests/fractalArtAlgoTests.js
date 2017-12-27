const fractalArtAlgo = require("../fractalArtAlgo");
const assert = require("assert");

describe("parseSingleLine", () => {
  it("../.. => .##/..#/##.", () => {
    const result = fractalArtAlgo.parseSingeLine("../.. => .##/..#/##.");

    assert.equal(result.input[0].length, 2);
    assert.equal(result.input[1].length, 2);
    assert.equal(result.input[0][0], ".");
    assert.equal(result.input[0][1], ".");
    assert.equal(result.input[1][0], ".");
    assert.equal(result.input[1][1], ".");

    assert.equal(result.output[0].length, 3);
    assert.equal(result.output[1].length, 3);
    assert.equal(result.output[2].length, 3);
    assert.equal(result.output[0][0], ".");
    assert.equal(result.output[0][1], "#");
    assert.equal(result.output[0][2], "#");

    assert.equal(result.output[1][0], ".");
    assert.equal(result.output[1][1], ".");
    assert.equal(result.output[1][2], "#");

    assert.equal(result.output[2][0], "#");
    assert.equal(result.output[2][1], "#");
    assert.equal(result.output[2][2], ".");
  });

  it("##/## => .##/.##/#.#", () => {
    const result = fractalArtAlgo.parseSingeLine("##/## => .##/.##/#.#");

    assert.equal(result.input[0].length, 2);
    assert.equal(result.input[1].length, 2);
    assert.equal(result.input[0][0], "#");
    assert.equal(result.input[0][1], "#");
    assert.equal(result.input[1][0], "#");
    assert.equal(result.input[1][1], "#");

    assert.equal(result.output[0].length, 3);
    assert.equal(result.output[1].length, 3);
    assert.equal(result.output[2].length, 3);
    assert.equal(result.output[0][0], ".");
    assert.equal(result.output[0][1], "#");
    assert.equal(result.output[0][2], "#");

    assert.equal(result.output[1][0], ".");
    assert.equal(result.output[1][1], "#");
    assert.equal(result.output[1][2], "#");

    assert.equal(result.output[2][0], "#");
    assert.equal(result.output[2][1], ".");
    assert.equal(result.output[2][2], "#");
  });

  it("..#/.../#.. => .#../#.##/..../..#.", () => {
    const result = fractalArtAlgo.parseSingeLine(
      "..#/.../#.. => .#../#.##/..../..#."
    );

    assert.equal(result.input[0].length, 3);
    assert.equal(result.input[1].length, 3);
    assert.equal(result.input[2].length, 3);
    assert.equal(result.input[0][0], ".");
    assert.equal(result.input[0][1], ".");
    assert.equal(result.input[0][2], "#");

    assert.equal(result.input[1][0], ".");
    assert.equal(result.input[1][1], ".");
    assert.equal(result.input[1][2], ".");

    assert.equal(result.input[2][0], "#");
    assert.equal(result.input[2][1], ".");
    assert.equal(result.input[2][2], ".");

    assert.equal(result.output[0].length, 4);
    assert.equal(result.output[1].length, 4);
    assert.equal(result.output[2].length, 4);
    assert.equal(result.output[3].length, 4);

    assert.equal(result.output[0][0], ".");
    assert.equal(result.output[0][1], "#");
    assert.equal(result.output[0][2], ".");
    assert.equal(result.output[0][3], ".");

    assert.equal(result.output[1][0], "#");
    assert.equal(result.output[1][1], ".");
    assert.equal(result.output[1][2], "#");
    assert.equal(result.output[1][3], "#");

    assert.equal(result.output[2][0], ".");
    assert.equal(result.output[2][1], ".");
    assert.equal(result.output[2][2], ".");
    assert.equal(result.output[2][3], ".");

    assert.equal(result.output[3][0], ".");
    assert.equal(result.output[3][1], ".");
    assert.equal(result.output[3][2], "#");
    assert.equal(result.output[3][3], ".");
  });
});

describe("rotate", () => {
  it("rotating 90 right sided", () => {
    const result = fractalArtAlgo.rotateSquare([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 7);
    assert.equal(result[0][1], 4);
    assert.equal(result[0][2], 1);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 8);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 2);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 9);
    assert.equal(result[2][1], 6);
    assert.equal(result[2][2], 3);
  });

  it("rotating 180 right sided", () => {
    let result = fractalArtAlgo.rotateSquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

    result = fractalArtAlgo.rotateSquare(result);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 9);
    assert.equal(result[0][1], 8);
    assert.equal(result[0][2], 7);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 6);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 4);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 3);
    assert.equal(result[2][1], 2);
    assert.equal(result[2][2], 1);
  });

  it("rotating 270 right sided", () => {
    let result = fractalArtAlgo.rotateSquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

    result = fractalArtAlgo.rotateSquare(result);
    result = fractalArtAlgo.rotateSquare(result);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 3);
    assert.equal(result[0][1], 6);
    assert.equal(result[0][2], 9);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 2);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 8);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 1);
    assert.equal(result[2][1], 4);
    assert.equal(result[2][2], 7);
  });

  it("rotating 360 right sided", () => {
    let result = fractalArtAlgo.rotateSquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

    result = fractalArtAlgo.rotateSquare(result);
    result = fractalArtAlgo.rotateSquare(result);
    result = fractalArtAlgo.rotateSquare(result);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 1);
    assert.equal(result[0][1], 2);
    assert.equal(result[0][2], 3);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 4);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 6);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 7);
    assert.equal(result[2][1], 8);
    assert.equal(result[2][2], 9);
  });
});

describe("flipUpDownSquare", () => {
  it("flip once", () => {
    const result = fractalArtAlgo.flipUpDownSquare([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]
    ]);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 10);
    assert.equal(result[0][1], 11);
    assert.equal(result[0][2], 12);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 7);
    assert.equal(result[1][1], 8);
    assert.equal(result[1][2], 9);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 4);
    assert.equal(result[2][1], 5);
    assert.equal(result[2][2], 6);

    assert.equal(result[3].length, 3);
    assert.equal(result[3][0], 1);
    assert.equal(result[3][1], 2);
    assert.equal(result[3][2], 3);
  });

  it("flip twice", () => {
    let result = fractalArtAlgo.flipUpDownSquare([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]
    ]);

    result = fractalArtAlgo.flipUpDownSquare(result);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 1);
    assert.equal(result[0][1], 2);
    assert.equal(result[0][2], 3);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 4);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 6);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 7);
    assert.equal(result[2][1], 8);
    assert.equal(result[2][2], 9);

    assert.equal(result[3].length, 3);
    assert.equal(result[3][0], 10);
    assert.equal(result[3][1], 11);
    assert.equal(result[3][2], 12);
  });
});

describe("flipLeftRight", () => {
  it("flip once", () => {
    const result = fractalArtAlgo.flipLeftRight([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]
    ]);

    assert.equal(result[0].length, 4);
    assert.equal(result[0][0], 4);
    assert.equal(result[0][1], 3);
    assert.equal(result[0][2], 2);
    assert.equal(result[0][3], 1);

    assert.equal(result[1].length, 4);
    assert.equal(result[1][0], 8);
    assert.equal(result[1][1], 7);
    assert.equal(result[1][2], 6);
    assert.equal(result[1][3], 5);

    assert.equal(result[2].length, 4);
    assert.equal(result[2][0], 12);
    assert.equal(result[2][1], 11);
    assert.equal(result[2][2], 10);
    assert.equal(result[2][3], 9);

    assert.equal(result[3].length, 4);
    assert.equal(result[3][0], 16);
    assert.equal(result[3][1], 15);
    assert.equal(result[3][2], 14);
    assert.equal(result[3][3], 13);
  });

  it("flip twice", () => {
    let result = fractalArtAlgo.flipLeftRight([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]
    ]);
    result = fractalArtAlgo.flipLeftRight(result);

    assert.equal(result[0].length, 4);
    assert.equal(result[0][0], 1);
    assert.equal(result[0][1], 2);
    assert.equal(result[0][2], 3);
    assert.equal(result[0][3], 4);

    assert.equal(result[1].length, 4);
    assert.equal(result[1][0], 5);
    assert.equal(result[1][1], 6);
    assert.equal(result[1][2], 7);
    assert.equal(result[1][3], 8);

    assert.equal(result[2].length, 4);
    assert.equal(result[2][0], 9);
    assert.equal(result[2][1], 10);
    assert.equal(result[2][2], 11);
    assert.equal(result[2][3], 12);

    assert.equal(result[3].length, 4);
    assert.equal(result[3][0], 13);
    assert.equal(result[3][1], 14);
    assert.equal(result[3][2], 15);
    assert.equal(result[3][3], 16);
  });
});

describe("divideToSquares", () => {
  it("2x2, divide to 2x2 blocks", () => {
    const squares = fractalArtAlgo.divideToSquares([[1, 2], [3, 4]], 2);

    assert.equal(squares.length, 1);
    assert.equal(squares[0][0][0], 1);
    assert.equal(squares[0][0][1], 2);
    assert.equal(squares[0][1][0], 3);
    assert.equal(squares[0][1][1], 4);
  });

  it("3x3, divide to 3x3 blocks", () => {
    const squares = fractalArtAlgo.divideToSquares(
      [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
      3
    );

    assert.equal(squares.length, 1);
    assert.equal(squares[0][0][0], 1);
    assert.equal(squares[0][0][1], 2);
    assert.equal(squares[0][0][2], 3);
    assert.equal(squares[0][1][0], 4);
    assert.equal(squares[0][1][1], 5);
    assert.equal(squares[0][1][2], 6);
    assert.equal(squares[0][2][0], 7);
    assert.equal(squares[0][2][1], 8);
    assert.equal(squares[0][2][2], 9);
  });

  it("4x4, divide to 2x2 blocks", () => {
    const squares = fractalArtAlgo.divideToSquares(
      [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
      2
    );

    assert.equal(squares.length, 4);
    assert.equal(squares[0][0][0], 0);
    assert.equal(squares[0][0][1], 1);
    assert.equal(squares[0][1][0], 4);
    assert.equal(squares[0][1][1], 5);

    assert.equal(squares[1][0][0], 2);
    assert.equal(squares[1][0][1], 3);
    assert.equal(squares[1][1][0], 6);
    assert.equal(squares[1][1][1], 7);

    assert.equal(squares[2][0][0], 8);
    assert.equal(squares[2][0][1], 9);
    assert.equal(squares[2][1][0], 12);
    assert.equal(squares[2][1][1], 13);

    assert.equal(squares[3][0][0], 10);
    assert.equal(squares[3][0][1], 11);
    assert.equal(squares[3][1][0], 14);
    assert.equal(squares[3][1][1], 15);
  });

  it("6x6, divide to 3x3 blocks", () => {
    const squares = fractalArtAlgo.divideToSquares(
      [
        [0, 1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10, 11],
        [12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35]
      ],
      3
    );

    assert.equal(squares.length, 4);
    assert.equal(squares[0][0][0], 0);
    assert.equal(squares[0][0][1], 1);
    assert.equal(squares[0][0][2], 2);
    assert.equal(squares[0][1][0], 6);
    assert.equal(squares[0][1][1], 7);
    assert.equal(squares[0][1][2], 8);
    assert.equal(squares[0][2][0], 12);
    assert.equal(squares[0][2][1], 13);
    assert.equal(squares[0][2][2], 14);

    assert.equal(squares[1][0][0], 3);
    assert.equal(squares[1][0][1], 4);
    assert.equal(squares[1][0][2], 5);
    assert.equal(squares[1][1][0], 9);
    assert.equal(squares[1][1][1], 10);
    assert.equal(squares[1][1][2], 11);
    assert.equal(squares[1][2][0], 15);
    assert.equal(squares[1][2][1], 16);
    assert.equal(squares[1][2][2], 17);

    assert.equal(squares[2][0][0], 18);
    assert.equal(squares[2][0][1], 19);
    assert.equal(squares[2][0][2], 20);
    assert.equal(squares[2][1][0], 24);
    assert.equal(squares[2][1][1], 25);
    assert.equal(squares[2][1][2], 26);
    assert.equal(squares[2][2][0], 30);
    assert.equal(squares[2][2][1], 31);
    assert.equal(squares[2][2][2], 32);

    assert.equal(squares[3][0][0], 21);
    assert.equal(squares[3][0][1], 22);
    assert.equal(squares[3][0][2], 23);
    assert.equal(squares[3][1][0], 27);
    assert.equal(squares[3][1][1], 28);
    assert.equal(squares[3][1][2], 29);
    assert.equal(squares[3][2][0], 33);
    assert.equal(squares[3][2][1], 34);
    assert.equal(squares[3][2][2], 35);
  });

  it("8x8, divide to 2x2 blocks", () => {
    const squares = fractalArtAlgo.divideToSquares(
      [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29, 30, 31],
        [32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47],
        [48, 49, 50, 51, 52, 53, 54, 55],
        [56, 57, 58, 59, 60, 61, 62, 63]
      ],
      2
    );

    assert.equal(squares.length, 16);
    assert.equal(squares[0][0][0], 0);
    assert.equal(squares[0][0][1], 1);
    assert.equal(squares[0][1][0], 8);
    assert.equal(squares[0][1][1], 9);

    assert.equal(squares[1][0][0], 2);
    assert.equal(squares[1][0][1], 3);
    assert.equal(squares[1][1][0], 10);
    assert.equal(squares[1][1][1], 11);

    assert.equal(squares[2][0][0], 4);
    assert.equal(squares[2][0][1], 5);
    assert.equal(squares[2][1][0], 12);
    assert.equal(squares[2][1][1], 13);

    assert.equal(squares[3][0][0], 6);
    assert.equal(squares[3][0][1], 7);
    assert.equal(squares[3][1][0], 14);
    assert.equal(squares[3][1][1], 15);

    assert.equal(squares[4][0][0], 16);
    assert.equal(squares[4][0][1], 17);
    assert.equal(squares[4][1][0], 24);
    assert.equal(squares[4][1][1], 25);

    assert.equal(squares[5][0][0], 18);
    assert.equal(squares[5][0][1], 19);
    assert.equal(squares[5][1][0], 26);
    assert.equal(squares[5][1][1], 27);

    assert.equal(squares[6][0][0], 20);
    assert.equal(squares[6][0][1], 21);
    assert.equal(squares[6][1][0], 28);
    assert.equal(squares[6][1][1], 29);

    assert.equal(squares[7][0][0], 22);
    assert.equal(squares[7][0][1], 23);
    assert.equal(squares[7][1][0], 30);
    assert.equal(squares[7][1][1], 31);

    assert.equal(squares[8][0][0], 32);
    assert.equal(squares[8][0][1], 33);
    assert.equal(squares[8][1][0], 40);
    assert.equal(squares[8][1][1], 41);

    assert.equal(squares[9][0][0], 34);
    assert.equal(squares[9][0][1], 35);
    assert.equal(squares[9][1][0], 42);
    assert.equal(squares[9][1][1], 43);

    assert.equal(squares[10][0][0], 36);
    assert.equal(squares[10][0][1], 37);
    assert.equal(squares[10][1][0], 44);
    assert.equal(squares[10][1][1], 45);

    assert.equal(squares[11][0][0], 38);
    assert.equal(squares[11][0][1], 39);
    assert.equal(squares[11][1][0], 46);
    assert.equal(squares[11][1][1], 47);

    assert.equal(squares[12][0][0], 48);
    assert.equal(squares[12][0][1], 49);
    assert.equal(squares[12][1][0], 56);
    assert.equal(squares[12][1][1], 57);

    assert.equal(squares[13][0][0], 50);
    assert.equal(squares[13][0][1], 51);
    assert.equal(squares[13][1][0], 58);
    assert.equal(squares[13][1][1], 59);

    assert.equal(squares[14][0][0], 52);
    assert.equal(squares[14][0][1], 53);
    assert.equal(squares[14][1][0], 60);
    assert.equal(squares[14][1][1], 61);

    assert.equal(squares[15][0][0], 54);
    assert.equal(squares[15][0][1], 55);
    assert.equal(squares[15][1][0], 62);
    assert.equal(squares[15][1][1], 63);
  });
});

describe("reconstructPictureFromSqueres", () => {
  it("2x2 divided to 2x2 blocks as single squere", () => {
    const squeres = [[[1, 2], [4, 5]]];
    const result = fractalArtAlgo.reconstructPictureFromSquares(squeres, 1, 2);

    assert.equal(result[0].length, 2);
    assert.equal(result[0][0], 1);
    assert.equal(result[0][1], 2);

    assert.equal(result[1].length, 2);
    assert.equal(result[1][0], 4);
    assert.equal(result[1][1], 5);
  });

  it("3x3, divided to 3x3 blocks as single squere", () => {
    const squeres = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]];
    const result = fractalArtAlgo.reconstructPictureFromSquares(squeres, 1, 3);

    assert.equal(result[0].length, 3);
    assert.equal(result[0][0], 1);
    assert.equal(result[0][1], 2);
    assert.equal(result[0][2], 3);

    assert.equal(result[1].length, 3);
    assert.equal(result[1][0], 4);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 6);

    assert.equal(result[2].length, 3);
    assert.equal(result[2][0], 7);
    assert.equal(result[2][1], 8);
    assert.equal(result[2][2], 9);
  });

  it("4x4, divided to 2x2 blocks", () => {
    const squeres = [
      [[0, 1], [4, 5]],
      [[2, 3], [6, 7]],
      [[8, 9], [12, 13]],
      [[10, 11], [14, 15]]
    ];
    const result = fractalArtAlgo.reconstructPictureFromSquares(squeres, 2, 2);

    assert.equal(result[0].length, 4);
    assert.equal(result[0][0], 0);
    assert.equal(result[0][1], 1);
    assert.equal(result[0][2], 2);
    assert.equal(result[0][3], 3);

    assert.equal(result[1].length, 4);
    assert.equal(result[1][0], 4);
    assert.equal(result[1][1], 5);
    assert.equal(result[1][2], 6);
    assert.equal(result[1][3], 7);

    assert.equal(result[2].length, 4);
    assert.equal(result[2][0], 8);
    assert.equal(result[2][1], 9);
    assert.equal(result[2][2], 10);
    assert.equal(result[2][3], 11);

    assert.equal(result[3].length, 4);
    assert.equal(result[3][0], 12);
    assert.equal(result[3][1], 13);
    assert.equal(result[3][2], 14);
    assert.equal(result[3][3], 15);
  });

  it("6x6, divided to 3x3 blocks", () => {
    const squeres = [
      [[0, 1, 2], [6, 7, 8], [12, 13, 14]],
      [[3, 4, 5], [9, 10, 11], [15, 16, 17]],
      [[18, 19, 20], [24, 25, 26], [30, 31, 32]],
      [[21, 22, 23], [27, 28, 29], [33, 34, 35]]
    ];
    const result = fractalArtAlgo.reconstructPictureFromSquares(squeres, 2, 3);

    assert.equal(result.length, 6);

    assert.equal(result[0].length, 6);
    assert.equal(result[0][0], 0);
    assert.equal(result[0][1], 1);
    assert.equal(result[0][2], 2);
    assert.equal(result[0][3], 3);
    assert.equal(result[0][4], 4);
    assert.equal(result[0][5], 5);

    assert.equal(result[1].length, 6);
    assert.equal(result[1][0], 6);
    assert.equal(result[1][1], 7);
    assert.equal(result[1][2], 8);
    assert.equal(result[1][3], 9);
    assert.equal(result[1][4], 10);
    assert.equal(result[1][5], 11);

    assert.equal(result[2].length, 6);
    assert.equal(result[2][0], 12);
    assert.equal(result[2][1], 13);
    assert.equal(result[2][2], 14);
    assert.equal(result[2][3], 15);
    assert.equal(result[2][4], 16);
    assert.equal(result[2][5], 17);

    assert.equal(result[3].length, 6);
    assert.equal(result[3][0], 18);
    assert.equal(result[3][1], 19);
    assert.equal(result[3][2], 20);
    assert.equal(result[3][3], 21);
    assert.equal(result[3][4], 22);
    assert.equal(result[3][5], 23);

    assert.equal(result[4].length, 6);
    assert.equal(result[4][0], 24);
    assert.equal(result[4][1], 25);
    assert.equal(result[4][2], 26);
    assert.equal(result[4][3], 27);
    assert.equal(result[4][4], 28);
    assert.equal(result[4][5], 29);

    assert.equal(result[5].length, 6);
    assert.equal(result[5][0], 30);
    assert.equal(result[5][1], 31);
    assert.equal(result[5][2], 32);
    assert.equal(result[5][3], 33);
    assert.equal(result[5][4], 34);
    assert.equal(result[5][5], 35);
  });
});

describe("generateFractArt", () => {
  it("should return 12 for test input", () => {
    const patterns = fractalArtAlgo.parseInput([
      "../.# => ##./#../...",
      ".#./..#/### => #..#/..../..../#..#"
    ]);

    const result = fractalArtAlgo.generateFractArt(patterns, 2);

    assert.equal(result, 12);
  });
});
