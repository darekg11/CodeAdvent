const assert = require("assert");
const passpahraseAlgo = require("../passphraseAlgo");

describe("isPassPhraseCorrect", () => {
  it("should return true for each word unique in passphrase", () => {
    const result = passpahraseAlgo.isPassPhraseCorrect(
      "ww ee dd xx c aa aaa a"
    );

    assert.equal(result, true);
  });

  it("should return false when there are duplicated words", () => {
    const result = passpahraseAlgo.isPassPhraseCorrect(
      "ww ww dd xx c aa aaa a"
    );

    assert.equal(result, false);
  });

  it("should return false when there are duplicated words at the begging and ending", () => {
    const result = passpahraseAlgo.isPassPhraseCorrect(
      "ww ss dd xx c aa aaa ww"
    );

    assert.equal(result, false);
  });

  it("should return false when there are multiple duplicated words", () => {
    const result = passpahraseAlgo.isPassPhraseCorrect(
      "ww ww dd xx dd aa aaa xx"
    );

    assert.equal(result, false);
  });

  it("should return false when there is only single unique word", () => {
    const result = passpahraseAlgo.isPassPhraseCorrect("ww ww ww ww ww ww ww");

    assert.equal(result, false);
  });
});

describe("isPassPhraseCorrectAnagrams", () => {
  it("should return false when all words are the same", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "ww ww ww ww ww"
    );

    assert.equal(result, false);
  });

  it("should return false when two words are anagrams", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "ws sw dd aa cc"
    );

    assert.equal(result, false);
  });

  it("should return false when anagrams are at the begging and end", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams("ws dd aa ws");

    assert.equal(result, false);
  });

  it("should return true when every word is different", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "ws yy dd aa cc"
    );

    assert.equal(result, true);
  });

  it("should return true when word is different by length having common beggining", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "ws wsy dd ydd cc"
    );

    assert.equal(result, true);
  });

  it("should return true for 'abcde fghij' ", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams("abcde fghij");

    assert.equal(result, true);
  });

  it("should return false for 'abcde xyz ecdab ", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "abcde xyz ecdab"
    );

    assert.equal(result, false);
  });

  it("should return true for 'a ab abc abd abf abj' ", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "a ab abc abd abf abj"
    );

    assert.equal(result, true);
  });

  it("should return true for 'iiii oiii ooii oooi oooo' ", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "iiii oiii ooii oooi oooo"
    );

    assert.equal(result, true);
  });

  it("should return false for 'oiii ioii iioi iiio' ", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams(
      "oiii ioii iioi iiio"
    );

    assert.equal(result, false);
  });

  it("should return true for 'dG Fe' - having the same ascii sum", () => {
    const result = passpahraseAlgo.isPassPhraseCorrectAnagrams("dG Fe");

    assert.equal(result, true);
  });
});
