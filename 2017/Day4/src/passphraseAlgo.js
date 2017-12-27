const isPassPhraseCorrect = passphrase => {
  const uniqueWordsInPassPhrase = [];
  const wordsInPassphrase = passphrase.split(" ");

  for (let cnt = 0; cnt < wordsInPassphrase.length; cnt += 1) {
    const singleWord = wordsInPassphrase[cnt];
    if (uniqueWordsInPassPhrase.includes(singleWord)) {
      return false;
    }
    uniqueWordsInPassPhrase.push(singleWord);
  }
  return true;
};

const areWordsAnagrams = (firstWord, secondWord) => {
  if (firstWord.length !== secondWord.length) {
    return false;
  }
  const firstWordSorted = [...firstWord]
    .sort((a, b) => a.localeCompare(b))
    .join("");
  const secondWordSorted = [...secondWord]
    .sort((a, b) => a.localeCompare(b))
    .join("");
  return firstWordSorted === secondWordSorted;
};

const isPassPhraseCorrectAnagrams = passphrase => {
  const wordsInPassphrase = passphrase.split(" ");
  for (let cnt = 0; cnt < wordsInPassphrase.length; cnt += 1) {
    const currentWordToCheck = wordsInPassphrase[cnt];
    for (
      let innerCnt = cnt + 1;
      innerCnt < wordsInPassphrase.length;
      innerCnt += 1
    ) {
      const wordToCheckForSimilarity = wordsInPassphrase[innerCnt];
      if (areWordsAnagrams(currentWordToCheck, wordToCheckForSimilarity)) {
        return false;
      }
    }
  }
  return true;
};

exports.isPassPhraseCorrect = isPassPhraseCorrect;
exports.isPassPhraseCorrectAnagrams = isPassPhraseCorrectAnagrams;
