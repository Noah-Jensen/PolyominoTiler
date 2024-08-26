To use this code, download all files in the "Code_Files" directory, along with the file "polyomino_lp_write.m" which is linked at the bottom of this file. Once downloaded, open SolverTemplate.py, SymmetrySolverGeneral.py, Polyominoes.m, and PolyominoLimit.m. 

In SolverTemplate.py on line 11, replace <Matlab Code Folder Location> with the path to the folder on your device that contains all of the matlab files from this project. Then set V, H, and N to numbers relevant to the example you want to run code for. Last, in line 22 replace <Desired folder name where unsolved boards will be stored> with your desired folder name, NOT a path to a folder, just a name.

Next, in SymmetrySolverGeneral.py, replace <Matlab Code Folder Location> in line 24 with the path to the folder where you store the relevant matlab files, in line 28, replace <Folder where you want your LP file stored> with the path to the folder where you want the LP file stored, and in line 29, replace <Folder where you want the solution files stored> with the path to the folder where you want the folder you name in SolverTemplate.py to be located.

In Polyomioes.m, use PolyominoMatrix = zeroes(m,n,r);, or another method, to create a list of r matrices where m is the maximum height of any of your polyominoes and n is the maximum width. Then set PolyominoMatrix(:,:,i) to be a matrix which represents the ith polyomino in your list. In the matrix, 1 is where a cell of the polyomino is located and 0 is where a cell is not located. Place the polyomino in the upper leftmost corner of the matrix. For example, an L-tromino placed in a 4 by 3 matrix could look like: [ 0 1 0 ; 1 1 0 ; 0 0 0 ; 0 0 0 ]. Do this for each polyomino you wish to use.

In PolyominoLimit.m, use PolyominoLimitVector = zeroes(1,r);, then set PolyominoLimitVector(i) to be the maximum number of copies of the ith polyomino you want to allow in tiling your region.

Now, run SolverTemplate.py.

-------------------------------------------------------------------------------------
Code Description


SolverTemplate is a template for using this code on an  m x n  board with r blockers and a set of polyominoes. It uses all of the other files to accomplish this.

Polyominoes is the list of polyominoes used to tile the board.
PolyominoLimit is a vector which determines the number of each polyomino that can be used.

BoardPartitions uses the conditions set forth in the paper to only solve boards in the reduced board partition set.
SectionSizeGenerator is a tool for convenience that creates a list of section sizes.
SymmetrySolverGeneral contains functions which generate and solve LP files to determine if a given board is tileable.

blockerBoard, genLPgeneral, SectionBuilder, and SectionGenerator are all used by SymmetrySolverGeneral.

The file polyomino_lp_write.m is not included here, but is necessary for genLPgeneral to work. It is written by John Burkardt and can be found at https://people.math.sc.edu/Burkardt/m_src/polyominoes/polyomino_lp_write.html
