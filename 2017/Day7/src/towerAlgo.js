const _ = require("lodash");

const parseInput = fileLines => {
  const towerRelations = [];
  const towerWeights = [];
  fileLines.forEach(singleLine => {
    const splittedLine = singleLine.split(" ");
    const hasSubTowers = splittedLine.length > 2;
    towerWeights.push({
      towerName: splittedLine[0],
      weight: Number(splittedLine[1].substring(1, splittedLine[1].length - 1))
    });
    if (hasSubTowers) {
      const subTowers = [];
      for (let cnt = 3; cnt < splittedLine.length - 1; cnt += 1) {
        subTowers.push(
          splittedLine[cnt].substring(0, splittedLine[cnt].length - 1)
        );
      }
      subTowers.push(splittedLine[splittedLine.length - 1]);
      towerRelations.push({
        towerName: splittedLine[0],
        subTowers
      });
    } else {
      towerRelations.push({
        towerName: splittedLine[0],
        subTowers: []
      });
    }
  });
  return {
    towerRelations,
    towerWeights
  };
};

const findBottomTower = towerRelations => {
  let allTowerNames = towerRelations.map(
    singleTowerRelation => singleTowerRelation.towerName
  );
  towerRelations.forEach(towerRelation => {
    if (towerRelation.subTowers.length > 0) {
      towerRelation.subTowers.forEach(singleSubTower => {
        _.remove(allTowerNames, singleTower => {
          return singleSubTower === singleTower;
        });
      });
    }
  });
  return allTowerNames[0];
};

const calculateTowerTotalWeight = (tower, towersWeight, towerRelations) => {
  const foundTowerRootWeight = towersWeight.find(singleTower => {
    return singleTower.towerName === tower;
  });
  let towerTotalWeigth = foundTowerRootWeight.weight;

  const selectedTowerSubtowers = towerRelations.find(singleRelation => {
    return singleRelation.towerName === tower;
  }).subTowers;

  if (selectedTowerSubtowers.length > 0) {
    selectedTowerSubtowers.forEach(singleSubTower => {
      towerTotalWeigth += calculateTowerTotalWeight(
        singleSubTower,
        towersWeight,
        towerRelations
      );
    });
  }
  return towerTotalWeigth;
};

const findRootUnbalancedTower = (tower, towersWeight, towerRelations) => {
  const subTowers = towerRelations.find(
    singleRelation => singleRelation.towerName === tower
  ).subTowers;
  const subTowersWeights = [];
  for (let cnt = 0; cnt < subTowers.length; cnt += 1) {
    subTowersWeights.push(
      calculateTowerTotalWeight(subTowers[cnt], towersWeight, towerRelations)
    );
  }
  const difference = _.max(subTowersWeights) - _.min(subTowersWeights);
  if (difference === 0) {
    return tower;
  } else {
    const unbalancedValue = _.chain(subTowersWeights)
      .countBy()
      .toPairs()
      .minBy(_.last)
      .value()[0];
    const unbalancedTowerIndex = subTowersWeights.findIndex(
      value => value == unbalancedValue
    );
    const unbalancedTowerName = subTowers[unbalancedTowerIndex];
    return findRootUnbalancedTower(
      unbalancedTowerName,
      towersWeight,
      towerRelations
    );
  }
};

const findDifferenceToBalanceTower = (towersWeight, towerRelations) => {
  for (let cnt = 0; cnt < towerRelations.length; cnt += 1) {
    const singleTowerInfo = towerRelations[cnt];
    if (singleTowerInfo.subTowers.length > 0) {
      const subTowers = singleTowerInfo.subTowers;
      const subTowersWeights = [];
      for (let innerCnt = 0; innerCnt < subTowers.length; innerCnt += 1) {
        subTowersWeights.push(
          calculateTowerTotalWeight(
            subTowers[innerCnt],
            towersWeight,
            towerRelations
          )
        );
      }
      const difference =
        subTowers.length === 0
          ? 0
          : _.max(subTowersWeights) - _.min(subTowersWeights);
      if (difference > 0) {
        const unbalancedValue = _.chain(subTowersWeights)
          .countBy()
          .toPairs()
          .minBy(_.last)
          .value()[0];
        const unbalancedTowerIndex = subTowersWeights.findIndex(
          value => value == unbalancedValue
        );
        const unbalancedTowerName = subTowers[unbalancedTowerIndex];
        const rootUnbalancedTower = findRootUnbalancedTower(
          unbalancedTowerName,
          towersWeight,
          towerRelations
        );
        const rootUnbalancedTowerWeight = towersWeight.find(
          towersWeight => towersWeight.towerName === rootUnbalancedTower
        ).weight;
        return rootUnbalancedTowerWeight - difference;
      }
    }
  }
  return 0;
};

exports.calculateTowerTotalWeight = calculateTowerTotalWeight;
exports.findDifferenceToBalanceTower = findDifferenceToBalanceTower;
exports.parseInput = parseInput;
exports.findBottomTower = findBottomTower;
