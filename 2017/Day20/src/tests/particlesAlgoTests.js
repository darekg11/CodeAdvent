const particlesAlgo = require("../particlesAlgo");
const assert = require("assert");

describe("parseSingleLine", () => {
  it("p=<2366,784,-597>, v=<-12,-41,50>, a=<-5,1,-2>", () => {
    const result = particlesAlgo.parseSingleLine(
      "p=<2366,784,-597>, v=<-12,-41,50>, a=<-5,1,-2>"
    );

    assert.equal(result.position.x, 2366);
    assert.equal(result.position.y, 784);
    assert.equal(result.position.z, -597);
    assert.equal(result.velocity.x, -12);
    assert.equal(result.velocity.y, -41);
    assert.equal(result.velocity.z, 50);
    assert.equal(result.acceleration.x, -5);
    assert.equal(result.acceleration.y, 1);
    assert.equal(result.acceleration.z, -2);
  });
});
