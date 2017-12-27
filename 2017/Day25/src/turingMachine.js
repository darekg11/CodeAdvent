const _ = require("lodash");

const STATE_A = "A";
const STATE_B = "B";
const STATE_C = "C";
const STATE_D = "D";
const STATE_E = "E";
const STATE_F = "F";

const executeTuringMachine = steps => {
  let currentState = STATE_A;
  let cursor = 0;
  const tape = {};
  let checksum = 0;

  for (let cnt = 0; cnt < steps; cnt += 1) {
    switch (currentState) {
      case STATE_A: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor += 1;
          currentState = STATE_B;
        } else {
          tape[cursor] = 0;
          checksum -= 1;
          cursor -= 1;
          currentState = STATE_E;
        }
        break;
      }
      case STATE_B: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor -= 1;
          currentState = STATE_C;
        } else {
          tape[cursor] = 0;
          checksum -= 1;
          cursor += 1;
          currentState = STATE_A;
        }
        break;
      }
      case STATE_C: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor -= 1;
          currentState = STATE_D;
        } else {
          tape[cursor] = 0;
          checksum -= 1;
          cursor += 1;
          currentState = STATE_C;
        }
        break;
      }
      case STATE_D: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor -= 1;
          currentState = STATE_E;
        } else {
          tape[cursor] = 0;
          checksum -= 1;
          cursor -= 1;
          currentState = STATE_F;
        }
        break;
      }
      case STATE_E: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor -= 1;
          currentState = STATE_A;
        } else {
          tape[cursor] = 1;
          cursor -= 1;
          currentState = STATE_C;
        }
        break;
      }
      case STATE_F: {
        if (!tape[cursor]) {
          tape[cursor] = 1;
          checksum += 1;
          cursor -= 1;
          currentState = STATE_E;
        } else {
          tape[cursor] = 1;
          cursor += 1;
          currentState = STATE_A;
        }
        break;
      }
    }
  }
  return checksum;
};

exports.executeTuringMachine = executeTuringMachine;
