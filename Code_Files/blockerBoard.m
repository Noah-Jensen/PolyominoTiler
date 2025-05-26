function Board = blockerBoard(Height,Width,BlockerPos)
%Board = blockerBoard(Height,Width,BlockerPos)
%   
%   Takes in the Height and Width of the board and BlockerPos, a vector
%   containing the locations of the blockers. It then creates a
%   HeightxWidth matrix of ones with zeros where blockers are located.

if (iscell(BlockerPos))

    BlockerPos = cell2mat(BlockerPos);

end

Len = length(BlockerPos);

Positions = zeros(Len/2, 2);

Positions(:,1) = BlockerPos(1 : 2 : Len - 1);
Positions(:,2) = BlockerPos(2 : 2 : Len);

Board = ones(Height,Width);

for i = 1 : (Len / 2)

    Board(Positions(i,1),Positions(i,2)) = 0;

end

end
