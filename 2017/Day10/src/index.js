const hashAlgo = require("./hashAlgo");
const result = hashAlgo.hashInput(
  [...Array(256).keys()],
  [165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153],
  1
);

console.log(result[0] * result[1]);

const stringInput = "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153";
const stringInputAsciiCodes = stringInput
  .split("")
  .map(singlElement => singlElement.charCodeAt())
  .concat([17, 31, 73, 47, 23]);

const resultMuchRounds = hashAlgo.hashInput(
  [...Array(256).keys()],
  stringInputAsciiCodes,
  64
);

const denseHash = hashAlgo.calculateDenseHash(resultMuchRounds);
const hexValue = hashAlgo.getHexRepresentation(denseHash);

console.log(hexValue);
