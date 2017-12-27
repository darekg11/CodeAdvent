const _ = require("lodash");

const parseSingleLine = singleLine => {
  const splittedBySpace = singleLine.split(" ");
  const positionPart = splittedBySpace[0].substring(3).slice(0, -2);
  const velocityPart = splittedBySpace[1].substring(3).slice(0, -2);
  const accelerationPart = splittedBySpace[2].substring(3).slice(0, -1);

  const positionValues = positionPart.split(",").map(Number);
  const velocityValues = velocityPart.split(",").map(Number);
  const accelerationValues = accelerationPart.split(",").map(Number);

  return {
    position: {
      x: positionValues[0],
      y: positionValues[1],
      z: positionValues[2]
    },
    velocity: {
      x: velocityValues[0],
      y: velocityValues[1],
      z: velocityValues[2]
    },
    acceleration: {
      x: accelerationValues[0],
      y: accelerationValues[1],
      z: accelerationValues[2]
    }
  };
};

const parseInput = lines => {
  const particles = [];
  lines.forEach(singleLine => {
    particles.push(parseSingleLine(singleLine));
  });
  return particles;
};

const simulateParticle = particle => {
  particle.velocity.x += particle.acceleration.x;
  particle.velocity.y += particle.acceleration.y;
  particle.velocity.z += particle.acceleration.z;
  particle.position.x += particle.velocity.x;
  particle.position.y += particle.velocity.y;
  particle.position.z += particle.velocity.z;
};

const calculateParticleDistance = particle => {
  return (
    Math.abs(particle.position.x) +
    Math.abs(particle.position.y) +
    Math.abs(particle.position.z)
  );
};

const simulateParticles = (particles, rounds) => {
  const particlesCopy = _.cloneDeep(particles);
  let smallestDistance = Number.MAX_SAFE_INTEGER;
  let smallestDistanceParticle = 0;
  for (let cnt = 0; cnt < rounds; cnt += 1) {
    for (
      let particleCnt = 0;
      particleCnt < particlesCopy.length;
      particleCnt += 1
    ) {
      const particle = particlesCopy[particleCnt];
      simulateParticle(particle);
    }
    const distances = particlesCopy.map(calculateParticleDistance);
    smallestDistance = _.min(distances);
    smallestDistanceParticle = _.indexOf(distances, smallestDistance);
  }
  return smallestDistanceParticle;
};

const removeCollisions = (particles, rounds) => {
  let particlesCopy = _.cloneDeep(particles);
  for (let cnt = 0; cnt < rounds; cnt += 1) {
    for (
      let particleCnt = 0;
      particleCnt < particlesCopy.length;
      particleCnt += 1
    ) {
      const particle = particlesCopy[particleCnt];
      simulateParticle(particle);
    }
    const groupedByDistance = _.groupBy(particlesCopy, singleParticle => {
      return (
        "X" +
        singleParticle.position.x +
        "Y" +
        singleParticle.position.y +
        "Z" +
        singleParticle.position.z
      );
    });
    const particlesThatDoNotCollide = _.pickBy(
      groupedByDistance,
      (value, key) => {
        return value.length === 1;
      }
    );
    particlesCopy = [].concat.apply([], _.values(particlesThatDoNotCollide));
    //wyjeb wszystkie te ktore maja values.length > 1
  }
  return particlesCopy.length;
};

exports.parseInput = parseInput;
exports.parseSingleLine = parseSingleLine;
exports.simulateParticles = simulateParticles;
exports.removeCollisions = removeCollisions;
