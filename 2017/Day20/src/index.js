const lineReader = require("readline");
const fs = require("fs");
const particlesAlgo = require("./particlesAlgo");
const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const particles = particlesAlgo.parseInput(lines);
  const closestParticleIndex = particlesAlgo.simulateParticles(
    particles,
    10000
  );
  const particlesCountAfterRemovingCollidingParticless = particlesAlgo.removeCollisions(
    particles,
    10000
  );
  console.log(closestParticleIndex);
  console.log(particlesCountAfterRemovingCollidingParticless);
});
