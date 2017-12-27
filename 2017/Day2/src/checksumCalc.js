const calculateCheckSumInRowMaxMinDifference = tableRow => {
  let rowChecksum = 0;
  let rowMinimalValue = tableRow[0] || 0;
  let rowMaximumValue = tableRow[0] || 0;

  tableRow.forEach(element => {
    if (element < rowMinimalValue) {
      rowMinimalValue = element;
    }
    if (element > rowMaximumValue) {
      rowMaximumValue = element;
    }
  });
  return rowMaximumValue - rowMinimalValue;
};

const calculateChecksumMinMaxEachRow = table => {
  let checkSum = 0;

  table.forEach(singleRow => {
    checkSum += calculateCheckSumInRowMaxMinDifference(singleRow);
  });
  return checkSum;
};

const calculateRowDividePairPerIndex = (tableRow, indexToCheck) => {
  const indexValue = tableRow[indexToCheck];
  for (let rowCnt = 0; rowCnt < tableRow.length; rowCnt += 1) {
    if (indexToCheck === rowCnt) {
      continue;
    }
    if (indexValue % tableRow[rowCnt] === 0) {
      return indexValue / tableRow[rowCnt];
    }
  }
  return 0;
};

const calculateRowDividePair = tableRow => {
  let rowCheckSum = 0;
  for (let rowCnt = 0; rowCnt < tableRow.length; rowCnt += 1) {
    const checkSumTemp = calculateRowDividePairPerIndex(tableRow, rowCnt);
    if (checkSumTemp !== 0) {
      rowCheckSum = checkSumTemp;
    }
  }
  return rowCheckSum;
};

calculateChecksumEvenlyDivisible = table => {
  let checkSum = 0;
  table.forEach(singleRow => {
    checkSum += calculateRowDividePair(singleRow);
  });
  return checkSum;
};

exports.calculateChecksumMinMaxEachRow = calculateChecksumMinMaxEachRow;
exports.calculateChecksumEvenlyDivisible = calculateChecksumEvenlyDivisible;
