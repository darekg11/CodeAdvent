const fs = require("fs");
const routeAlgo = require("./routeAlgo");

const input = fs.readFileSync("./input.txt").toString("utf-8");

routeAlgo.findRoute(input);
