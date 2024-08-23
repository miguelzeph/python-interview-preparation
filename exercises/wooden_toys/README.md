# Objective

You make wooden toys in your woodworking shop for the employment of your grandchildren. You have planned a serie of small puzzles, and you would like to automate the writing of the solutions:

## Instructions

Each puzzle is a grid, on which are placed wooden blocks of various shapes. These blocks must be taken out of the game, one after the other, without colliding. You have to determine the order in which they are taken out.

Each block is numbered with a value between 0 and 9. When you enter the number of a block, it will be moved to the right until it is off of the grid.
If several blocks can be exited at the same time, you can choose which one you would like to remove first.

## Implementation

Implement the function `solve(width, height,nb_blocks,grid)`. This function is executed at each round of the game and should return the number of the next block to move.

Input data of the function:

- width: width of the puzzle, in number of cells.
- height: height of the puzzle, in number of cells.
- nb_locks: number of blocks initially present in the puzzle.
- grid: a list of height elements, each of which is a string with a size equal to width.

The parameters width, height, and nb_blocks do not change during the whole game.

The grid parameter represents the current situation of the puzzle. Each of its characters can take on of the following values:

- . (a dot): an empty square.
- X: a wall. They are placed on the first and last line, as well as on the first character of each line, to show that only possible exit is to the right. You cannot move these walls.
- An integer between 0 and nb_blocks-1:a square occupied by a block. The same number can be present several times in the grid, representing a single block that extends over several squares. All cells with the same block number are connected (they are never separated into several isolated groups).

## Output data of the function

An integer, between 0 and nb_blocks-1, representing the number of the block you want to output to the right.


You can only move one block at a time, and each move must always be to the right. A move is made until the end: either until the block is completely out, or until one block collides with another.


## Victory conditions

All blocks are out of the game.

(There is at least one possible block removal order that will yield a solution.)


## Constraints

1 < width < 15

1 < height < 15

1 <= nb_blocks < 10

