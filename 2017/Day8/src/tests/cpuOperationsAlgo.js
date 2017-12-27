const assert = require("assert");
const cpuOperationsAlgo = require("../cpuOperationsAlgo");

describe("parseSingleLine", () => {
  it("should return correct input for 'cpv inc -625 if ke == 0' ", () => {
    const result = cpuOperationsAlgo.parseSingleLine("cpv inc -625 if ke == 0");

    assert.equal(result.condition, "==");
    assert.equal(result.destinationRegister, "cpv");
    assert.equal(result.leftOperandCondition, "ke");
    assert.equal(result.operation, "inc");
    assert.equal(result.rightOperandCondition, "0");
    assert.equal(result.value, -625);
  });

  it("should return correct input for 'pmp dec -432 if sdj <= -648' ", () => {
    const result = cpuOperationsAlgo.parseSingleLine(
      "pmp dec -432 if sdj <= -648"
    );

    assert.equal(result.condition, "<=");
    assert.equal(result.destinationRegister, "pmp");
    assert.equal(result.leftOperandCondition, "sdj");
    assert.equal(result.operation, "dec");
    assert.equal(result.rightOperandCondition, -648);
    assert.equal(result.value, -432);
  });
});

describe("isOperandRegister", () => {
  it("should return true for for string", () => {
    const result = cpuOperationsAlgo.isOperandRegister("deddd");
    assert.equal(result, true);
  });

  it("should return false for for positive number", () => {
    const result = cpuOperationsAlgo.isOperandRegister(22);
    assert.equal(result, false);
  });

  it("should return false for for negative number", () => {
    const result = cpuOperationsAlgo.isOperandRegister(-23311);
    assert.equal(result, false);
  });

  it("should return false for for 0", () => {
    const result = cpuOperationsAlgo.isOperandRegister(0);
    assert.equal(result, false);
  });
});

describe("getValueFromRegister", () => {
  it("should return 0 when register does not exist", () => {
    const registers = {
      ad: 8,
      www: 10
    };
    const result = cpuOperationsAlgo.getValueFromRegister(
      registers,
      "notExist"
    );
    assert.equal(result, 0);
  });

  it("should return register value when register exists", () => {
    const registers = {
      ad: 8,
      www: 10
    };
    const result = cpuOperationsAlgo.getValueFromRegister(registers, "ad");
    assert.equal(result, 8);
  });
});

describe("putValueToRegister", () => {
  it("should correctly put value when register does not exist", () => {
    const registers = {
      ad: 8,
      www: 10
    };
    const result = cpuOperationsAlgo.putValueToRegister(registers, "test", 20);
    assert.equal(result.ad, 8);
    assert.equal(result.www, 10);
    assert.equal(result.test, 20);
  });

  it("should correctly put value when register exists", () => {
    const registers = {
      ad: 8,
      www: 10
    };
    const result = cpuOperationsAlgo.putValueToRegister(registers, "ad", 20);
    assert.equal(result.ad, 20);
    assert.equal(result.www, 10);
  });
});

describe("executeSingleOperation", () => {
  it("should return changed registers when registers have value", () => {
    const registers = {
      a: 5,
      b: 24
    };
    const operation = cpuOperationsAlgo.parseSingleLine("a inc 10 if b > 23");
    const result = cpuOperationsAlgo.executeSingleOperation(
      registers,
      operation
    );
    assert.equal(result.registers.a, 15);
    assert.equal(result.registers.b, 24);
  });

  it("should not execute when condition is not met", () => {
    const registers = {
      a: 5,
      b: 24
    };
    const operation = cpuOperationsAlgo.parseSingleLine("a inc 10 if b > 100");
    const result = cpuOperationsAlgo.executeSingleOperation(
      registers,
      operation
    );
    assert.equal(result.registers.a, 5);
    assert.equal(result.registers.b, 24);
  });

  it("should execute when register does not exist but condition tries to check 0 equality", () => {
    const registers = {
      a: 5,
      b: 24
    };
    const operation = cpuOperationsAlgo.parseSingleLine("a dec 10 if c == 0");
    const result = cpuOperationsAlgo.executeSingleOperation(
      registers,
      operation
    );
    assert.equal(result.registers.a, -5);
    assert.equal(result.registers.b, 24);
  });

  it("should execute when register does not exists and properly increase by descreasing negative value", () => {
    const registers = {
      a: 2
    };
    const operation = cpuOperationsAlgo.parseSingleLine("c dec -10 if a >= 1");
    const result = cpuOperationsAlgo.executeSingleOperation(
      registers,
      operation
    );
    assert.equal(result.registers.a, 2);
    assert.equal(result.registers.c, 10);
  });

  it("should execute when register does not exists and properly decrease by increasing negative value", () => {
    const registers = {
      c: 10
    };
    const operation = cpuOperationsAlgo.parseSingleLine("c inc -20 if c == 10");
    const result = cpuOperationsAlgo.executeSingleOperation(
      registers,
      operation
    );
    assert.equal(result.registers.c, -10);
  });
});

describe("findRegisterWithMaximumValue", () => {
  it("should return maximum value for registers", () => {
    const registers = {
      a: 20,
      b: -55,
      c: 100,
      d: 1988,
      e: 5
    };
    const result = cpuOperationsAlgo.findRegisterWithMaximumValue(registers);
    assert.equal(result, 1988);
  });
});

describe("whole algorithm", () => {
  it("should return 1 for test input", () => {
    const lines = [
      "b inc 5 if a > 1",
      "a inc 1 if b < 5",
      "c dec -10 if a >= 1",
      "c inc -20 if c == 10"
    ];

    const cpuInstructions = cpuOperationsAlgo.parseInput(lines);
    const result = cpuOperationsAlgo.executeProgram(cpuInstructions);
    const maximumValue = cpuOperationsAlgo.findRegisterWithMaximumValue(
      result.registers
    );
    assert.equal(result.highestValueEver, 10);
    assert.equal(maximumValue, 1);
  });
});
