const lineReader = require("readline");
const fs = require("fs");
const passphraseAlgo = require("./passphraseAlgo");

let validPassphrases = 0;
let validPassphrasesAnagrams = 0;

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", line => {
  if (passphraseAlgo.isPassPhraseCorrect(line)) {
    validPassphrases += 1;
  }
  if (passphraseAlgo.isPassPhraseCorrectAnagrams(line)) {
    validPassphrasesAnagrams += 1;
  }
});

lineReaderInterface.on("close", () => {
  console.log(validPassphrases);
  console.log(validPassphrasesAnagrams);
});
