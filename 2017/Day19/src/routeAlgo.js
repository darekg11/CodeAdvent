const _ = require("lodash");

const UP = "UP";
const DOWN = "DOWN";
const RIGHT = "RIGHT";
const LEFT = "LEFT";

const findRoute = input => {
  const grid = input.split("\n").map(singleRow => singleRow.split(""));
  let direction = DOWN;
  let x = grid[0].indexOf("|");
  let y = 0;
  let steps = 0;
  let letters = [];

  while (true) {
    switch (direction) {
      case UP: {
        y -= 1;
        break;
      }
      case DOWN: {
        y += 1;
        break;
      }
      case RIGHT: {
        x += 1;
        break;
      }
      case LEFT: {
        x -= 1;
        break;
      }
    }
    steps += 1;
    if (grid[y][x] >= "A" && grid[y][x] <= "Z") {
      letters.push(grid[y][x]);
    }
    if (grid[y][x] == "+") {
      if (grid[y + 1][x] == "|" && direction !== UP) {
        direction = DOWN;
      } else if (grid[y - 1][x] == "|" && direction !== DOWN) {
        direction = UP;
      } else if (grid[y][x + 1] == "-" && direction !== LEFT) {
        direction = RIGHT;
      } else if (grid[y][x - 1] == "-" && direction !== RIGHT) {
        direction = LEFT;
      }
    }
    if (grid[y][x] == " ") {
      break;
    }
  }
  console.log(letters.join(""));
  console.log(steps);
};

exports.findRoute = findRoute;
