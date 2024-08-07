SolverTemplate is a template for using this code on an  m x n  board with r blockers and a set of polyominoes. It uses all of the other files to accomplish this.

Polyominoes is the list of polyominoes used to tile the board.
PolyominoLimit is a vector which determines the number of each polyomino that can be used.

BoardPartitions uses the conditions set forth in the paper to only solve boards in the reduced board partition set.
SectionSizeGenerator is a tool for convenience that creates a list of section sizes.
SymmetrySolverGeneral contains functions which generate and solve LP files to determine if a given board is tileable.

blockerBoard, genLPgeneral, SectionBuilder, and SectionGenerator are all used by SymmetrySolverGeneral.

The file polyomino_lp_write is not included here, but is necessary for genLPgeneral to work. It is written by John Burkardt and can be found at https://people.math.sc.edu/Burkardt/m_src/polyominoes/polyomino_lp_write.html
