# MINI MINESWEEPER GAME
#### Video Demo:  <https://youtu.be/hD7DXCakGPc>
#### A short version of minesweeper game:
Minesweeper is a classical puzzle game, that we can play on windows. It consists of a matrix of blocks with some hidden mines behind some random blocks in it. To play this game, we select a block to show what is behind it. If we see a number ***n*** in it, that means there are exactly n mines in the eight directions around it. To win the game we have to unhide all cells without pressing any mine. This project contains only two modules: project.py which consider a basic version of this game and test_project.py

## project.py
This module conatains exactly five function beside main function:
- remaining_cells() function
- matrix_print() function
- visual_mat() function
- hidden_mat() function
- look_around() function

### **main() function**
In main function, the program prompts the player to select a level to play the game or 0 to close it; choosing the wrong level will reprompt the player to choose again.
- ***Easy level***: 9x9 blocks with 10 mines
- ***Medium level***: 16x16 block with 40 mines

For programming this game, two matrices will be created
- ***Visual matrix***: a blocks matrix which appear to player.
- ***Hidden matrix***: matrix with the actual mine places. The location of those mines are choosing randomly each time.

At first, and while the game is still on, the visual matrix will appear with a prompt to input **correct** row and column numbers from this matrix separated by space. Each try from player will show the visual matrix after showing what is behind the selected cell. There are three possibilities:
* If the player chooses a mine, the game will end with a failing message with the visual matrix after exposing the remaining mines places.
* If the player chooses a cell next to a mine, the game will show the visual matrix after replacing the block with a number, representing how many surrounding mines for this cell.
* If the player chooses a cell with no mines around it, the game will show the visual matrix after replacing the block with an empty cell, and all nearby empty cells until we reach cells which are close to the mine/s.

After discovering all right cells, the game will end with a success message.

### **remaining_cells() function**
    Definition and Usage
        The remaining_cells() function takes the current block matrix and returns the number of cells which contain blocks

### **matrix_print function**
    Definition and Usage
        The matrix_print() function is a very classic function which take a matrix as an argument and print its elements in matrix form without brackets

### **visual_mat function**
    Definition and Usage
        The visual_mat() function takes a length of desired matrix as an argument and returned a two-dimensional matrix
    Syntax
        visual_mat(object)
    Parameter Values
        object	Required. An object. Must be a non-negative integer
The resulting matrix which appear to the player is a  matrix with inner block cells and numbers of row and columns  shown in both sides. According to my sample: there are two difficalty level in the game:
- ***Easy level***: 9x9 blocks
- ***Medium level***: 16x16 block
the difference of those matrices shown at printing as the column number take one or two digit so i used a conditional if statement to write different spaces

### **hidden_mat function**
    Definition and Usage
        The hidden_mat() function return a two-dimensional matrix containing mine in specified locations
    Syntax
        hidden_mat(L,loc)
    Parameter Values
        L	Required. Must be a non-negative integer
        loc Required. An iterable, with zero or more items
here, we generate a LxL hidden matrix consisting of mines located in specific locations given as a second argument, and calculate the value of neighboring cells. The value of cells which are not surrounding by any mine is zero


### **look_around function**
    Definition and Usage
        The look_around() function returns a set consisting of 8 locations of neighboring cells if exist
    Syntax
        look_around(matrix,row,col)
    Parameter Values
        matrix	Required. a 2-diemsional matrix
        row Required. nonnegative integer represents the row number of current cell
        col Required. nonnegative integer represents the column number of current cell
Here, there are some corner cases when the cell is at boundary do the returning cells are not always eight



## test_project.py
This module contains exactly 10 function to test the three following functions:
- remaining_cells() function
- hidden_mat() function
- look_around() function
no test function here for printing function or for formating block function