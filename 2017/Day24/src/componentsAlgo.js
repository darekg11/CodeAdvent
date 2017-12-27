const _ = require("lodash");

const parseSingleLine = singleLine => {
  const splitted = singleLine.split("/");
  const firstPort =
    Number(splitted[0]) < Number(splitted[1])
      ? Number(splitted[0])
      : Number(splitted[1]);
  const secondPort =
    Number(splitted[1]) > Number(splitted[0])
      ? Number(splitted[1])
      : Number(splitted[0]);
  const total = firstPort + secondPort;
  return {
    firstPort,
    secondPort,
    total,
    used: false
  };
};

const parseInput = lines => {
  const components = [];
  lines.forEach(element => {
    components.push(parseSingleLine(element));
  });
  return components;
};

const buildBridges = (bridge, buildingBlocks, port) => {
  let bridges = [];
  for (let cnt = 0; cnt < buildingBlocks.length; cnt += 1) {
    if (
      port === buildingBlocks[cnt].firstPort ||
      port === buildingBlocks[cnt].secondPort
    ) {
      const anotherLayerBridge = {
        strength: bridge.strength + buildingBlocks[cnt].total,
        length: bridge.length + 1
      };
      bridges.push(anotherLayerBridge);
      const leftBuildingPieces = buildingBlocks.slice();
      leftBuildingPieces.splice(cnt, 1);

      bridges = [
        ...bridges,
        ...buildBridges(
          anotherLayerBridge,
          leftBuildingPieces,
          port === buildingBlocks[cnt].firstPort
            ? buildingBlocks[cnt].secondPort
            : buildingBlocks[cnt].firstPort
        )
      ];
    }
  }
  return bridges;
};

const bridgeInfo = componentsIn => {
  const componentsCopy = _.cloneDeep(componentsIn);
  const bridges = buildBridges({ strength: 0, length: 0 }, componentsCopy, 0);
  const strongest = _.maxBy(bridges, "strength");
  const bridgesByLength = _.groupBy(bridges, "length");
  const keyNames = _.keys(bridgesByLength);
  const longestBridgesKeyName = _.chain(bridgesByLength)
    .keys()
    .map(Number)
    .max()
    .value();
  const longestBridges = bridgesByLength[longestBridgesKeyName];
  const longestStrongestBridge = _.maxBy(longestBridges, "strength");
  return {
    strongest: strongest.strength,
    strongestLongestBridge: longestStrongestBridge.strength
  };
};

exports.parseInput = parseInput;
exports.bridgeInfo = bridgeInfo;
