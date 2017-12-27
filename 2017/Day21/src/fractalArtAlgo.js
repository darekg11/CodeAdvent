const _ = require("lodash");

const parseSingeLine = singleLine => {
  let pattern = {
    input: [],
    output: []
  };
  const splittedByDelimiter = singleLine.split(" => ");
  const inputSplittedParts = splittedByDelimiter[0].split("/");
  const outputSplittedParts = splittedByDelimiter[1].split("/");
  for (let cnt = 0; cnt < inputSplittedParts.length; cnt += 1) {
    const array = inputSplittedParts[cnt].split("");
    pattern.input.push(array);
  }
  for (let cnt = 0; cnt < outputSplittedParts.length; cnt += 1) {
    const array = outputSplittedParts[cnt].split("");
    pattern.output.push(array);
  }
  return pattern;
};

const parseInput = lines => {
  const patterns = [];
  lines.forEach(singleLine => {
    patterns.push(parseSingeLine(singleLine));
  });
  return patterns;
};

const rotateSquare = square => {
  const rotatedSquare = _.cloneDeep(square);
  for (let row = 0; row < square.length; row += 1) {
    for (let col = 0; col < square[row].length; col += 1) {
      rotatedSquare[col][square.length - 1 - row] = square[row][col];
    }
  }
  return rotatedSquare;
};

const flipUpDownSquare = square => {
  const flippedSquare = _.cloneDeep(square);
  for (let row = 0; row < square.length; row += 1) {
    for (let col = 0; col < square[row].length; col += 1) {
      flippedSquare[square.length - 1 - row][col] = square[row][col];
    }
  }
  return flippedSquare;
};

const flipLeftRight = square => {
  const flippedSquare = _.cloneDeep(square);
  for (let row = 0; row < square.length; row += 1) {
    for (let col = 0; col < square[row].length; col += 1) {
      flippedSquare[row][square.length - 1 - col] = square[row][col];
    }
  }
  return flippedSquare;
};

const divideToSquares = (picture, destinationSize) => {
  const squaresPerRow = picture[0].length / destinationSize;
  const outputSquaresCount =
    picture[0].length * picture[0].length / (destinationSize * destinationSize);
  const squares = [];
  for (let cnt = 0; cnt < outputSquaresCount; cnt += 1) {
    squares.push([]);
  }
  for (let row = 0; row < picture.length; row += 1) {
    for (let col = 0; col < picture[row].length; col += 1) {
      const calculatedRow = Math.floor(row / destinationSize) * squaresPerRow;
      const calculatedColumn = Math.floor(col / destinationSize);
      const desintationSubQuareIndex = calculatedRow + calculatedColumn;
      squares[desintationSubQuareIndex].push(picture[row][col]);
    }
  }
  const squaresSplitted = [];
  for (let cnt = 0; cnt < squares.length; cnt += 1) {
    squaresSplitted.push(_.chunk(squares[cnt], destinationSize));
  }

  return squaresSplitted.filter(subArray => subArray.length);
};

const reconstructPictureFromSquares = (squares, squaresPerRow, squereSize) => {
  const picture = [];
  const squaresChunked = _.chunk(squares, squaresPerRow);
  for (let cnt = 0; cnt < squaresChunked.length; cnt += 1) {
    for (let rowCnt = 0; rowCnt < squereSize; rowCnt += 1) {
      let newRow = [];
      for (
        let squeresCnt = 0;
        squeresCnt < squaresChunked[cnt].length;
        squeresCnt += 1
      ) {
        newRow = [...newRow, ...squaresChunked[cnt][squeresCnt][rowCnt]];
      }
      picture.push(newRow);
    }
  }
  return picture;
};

const areArraysEqual = (first, second) => {
  const firstFlatten = _.flatten(first);
  const secondFlatten = _.flatten(second);
  return _.isEqual(firstFlatten, secondFlatten);
};

const findPatternMatch = (square, patterns) => {
  for (let cnt = 0; cnt < patterns.length; cnt += 1) {
    const pattern = patterns[cnt].input;
    const rotate90 = rotateSquare(pattern);
    const rotate180 = rotateSquare(rotate90);
    const rotate270 = rotateSquare(rotate180);
    const patternFlippedUpDown = flipUpDownSquare(pattern);
    const rotate90FlippedUpDown = flipUpDownSquare(rotate90);
    const rotate180FlippedUpDown = flipUpDownSquare(rotate180);
    const rotate270FlippedUpDown = flipUpDownSquare(rotate270);
    const patternFlippedLeftRight = flipLeftRight(pattern);
    const rotate90FlippedLeftRight = flipLeftRight(rotate90);
    const rotate180FlippedLeftRight = flipLeftRight(rotate180);
    const rotate270FlippedLeftRight = flipLeftRight(rotate270);
    const possiblePatterns = [
      pattern,
      rotate90,
      rotate180,
      rotate270,
      patternFlippedUpDown,
      rotate90FlippedUpDown,
      rotate180FlippedUpDown,
      rotate270FlippedUpDown,
      patternFlippedLeftRight,
      rotate90FlippedLeftRight,
      rotate180FlippedLeftRight,
      rotate270FlippedLeftRight
    ];
    for (
      let permutations = 0;
      permutations < possiblePatterns.length;
      permutations += 1
    ) {
      if (areArraysEqual(possiblePatterns[permutations], square)) {
        return patterns[cnt].output;
      }
    }
  }
  return null;
};

const generateFractArt = (patterns, iterations) => {
  let picture = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]];
  for (let cnt = 0; cnt < iterations; cnt += 1) {
    const pictureSize = picture[0].length;
    const destinationSquereSizes = pictureSize % 2 === 0 ? 2 : 3;
    const squares = divideToSquares(picture, destinationSquereSizes);

    for (let squeresCnt = 0; squeresCnt < squares.length; squeresCnt += 1) {
      const newPattern = findPatternMatch(squares[squeresCnt], patterns);
      if (newPattern) {
        squares[squeresCnt] = newPattern;
      } else {
        console.log("NOT FOUND ANY PATTERN, SOMETHING IS FUCKED");
      }
    }
    if (squares.length > 0) {
      picture = reconstructPictureFromSquares(
        squares,
        Math.ceil(squares.length / squares[0].length),
        squares[0].length
      );
    }
  }
  const flattenPicture = _.flatten(picture);
  const leftOnPlaces = flattenPicture.filter(elem => elem === "#");
  return leftOnPlaces.length;
};

exports.parseInput = parseInput;
exports.parseSingeLine = parseSingeLine;
exports.rotateSquare = rotateSquare;
exports.flipUpDownSquare = flipUpDownSquare;
exports.flipLeftRight = flipLeftRight;
exports.divideToSquares = divideToSquares;
exports.reconstructPictureFromSquares = reconstructPictureFromSquares;
exports.generateFractArt = generateFractArt;
