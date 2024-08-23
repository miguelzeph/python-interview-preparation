# Objective

Pick the packages from the heaviest to the lightest one.

## Instructions

You work in an automated factory that controls a robotic arm to move packages. The arm can pick packages from the conveyor belts to form a stack of packages.

The packages are sorted from the heaviest to the lightest on each of the conveyor belts. Your objective is to pick the heaviest package among the 3 conveyor belts to move it on a stack.

Implement the moethod solve(weight_0, weight_1, weight_2) that takes 3 integer arguments. these values represent the weight of the packages available on the conveyor belts with respective index 0, 1, and 2. For example, weight_0 = 80, weight_1 = 100 and weight_2 = 90, then the expected answer is 1. In case of equality, any correct answer is accepted.


## Input

- N, the number of temperatures to analyse (optional). This will be nonzero.
- The N temperatures expressed as integers ranging from -273 to 5526.


## Output

Output the temperature closest to 0. `If two temperatures are equally close, take the positive one. For instance, if the temperatures are -5 and 5, output 5.`

