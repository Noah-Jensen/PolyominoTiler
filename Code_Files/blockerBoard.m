function Board = blockerBoard(Height,Width,BlockerPos)
%Board = blockerBoard(Height,Width,BlockerPos)
%   
%   Takes in the Height and Width of the board and BlockerPos, a vector
%   containing the locations of the blockers. It then creates a
%   HeightxWidth matrix of ones with zeros where blockers are located.

if (iscell(BlockerPos))

    BlockerPos = cell2mat(BlockerPos);

end

Board = ones(Height,Width);

Board(BlockerPos) = 0;

end
