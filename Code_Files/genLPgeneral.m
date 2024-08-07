function ToLPMat = genLPgeneral(Polyominoes, PolyominoCount, Board, fileLocation)
%ToLPMat = genLPgeneral(Polyominoes, PolyominoCount, Board, fileLocation)
%   
%   Polyominoes is a list of matrices where each matrix is one of the
%   polyominoes used to tile the board
%   PolyominoCount is a vector which lists the number of copies of each 
%   polyomino in Polyominoes to use
%   Board is a matrix representation of the board, where it has the same
%   number of cells as the board and ones everywhere except for where
%   blockers are located
%   fileLocation is the location where the LP file will be stored
%
%   This function first finds all the symmetries of the polyominoes given.
%   Then it finds the possible placements for the polyominoes on the given
%   board. After saving all such placements, a matrix ToLPMat is generated
%   along with a vector ToLPObj. These are fed into the function
%   polyomino_lp_write and used to generate an LP file which CPLEX can
%   read.
%
%   The file polyomino_lp_write was created by John Burkardt and can be
%   found at https://people.math.sc.edu/Burkardt/m_src/polyominoes/polyomino_lp_write.html


%Plan: First find all rotations/reflections of each polyomino, probably
%store them as vectors not matrices, then start placing them on the board.
%Save the working ones, then build matrix, then make LP file.

%Assuming board is 1 where you can place 0 where you can't

BoardH = size(Board,1);
BoardW = size(Board,2);

BoardPlacer = 1 - Board;

PNum = size(Polyominoes,3);

PlacementArrays = cell(1,PNum * 8);

ShiftVec = zeros(1,8 * PNum);

PCount = zeros(1,PNum);

for i = 1 : PNum

CurPoly = RotRefPoly(Polyominoes(:,:,i));
CurLen = size(CurPoly,3);


    for j = 1 : CurLen

        CurRotRef = CurPoly(:,:,j);
        CurRotRef( ~any(CurRotRef,2), : ) = [];
        CurRotRef( :, ~any(CurRotRef,1) ) = [];

        CurH = size(CurRotRef,1);
        CurW = size(CurRotRef,2);

        PossPlaceNum = (BoardH - CurH + 1 ) * (BoardW - CurW + 1);

        if (PossPlaceNum <= 0)

         %   RCount(i) = RCount(i) + 1;

        else

        PCount(i) = PCount(i) + 1;

        PlacementArrays{8*(i-1) + j} = zeros(BoardH,BoardW,PossPlaceNum);

        Shift = 0;

        for k = 1 : PossPlaceNum
        
            CheckPlace = zeros(BoardH,BoardW);

            Div = BoardW - CurW + 1;

            col = mod(k,Div) + 1;
            row = floor((k-1)/Div) + 1;
            
            CheckPlace(row:(row + CurH - 1),col:(col + CurW - 1)) = CurRotRef;

            Checker = BoardPlacer + CheckPlace;

            if (isempty(find(Checker==2)))

                PlacementArrays{8*(i-1) + j}(:,:,(k - Shift)) = CheckPlace;

            else

            Shift = Shift + 1;

            end

            ShiftVec(8*(i-1) + j) = Shift;
            
        end

        PlacementArrays{8*(i-1)+j}(:,:,(PossPlaceNum - Shift + 1):end) = [];

        end

    end

end

nList2 = zeros(1,PNum);

PlacementArrays = PlacementArrays(~cellfun(@isempty,PlacementArrays));

SymLen = length(PlacementArrays);

nList = cellfun('size',PlacementArrays,3);

n = sum(nList);

LLoc = 1;

for i = 1 : PNum

    LEnd = LLoc + PCount(i);

    nList2(i) = sum(nList(LLoc:(LEnd - 1)));

    LLoc = LEnd;

end

BSCount = BoardH * BoardW;

ToLPMat = zeros((BSCount + PNum),n);

BinLoc = 1;

for i = 1 : PNum

    BP = BinLoc + nList2(i);

    ToLPMat((BSCount + i),BinLoc:(BP - 1)) = 1;
    
    BinLoc = BP;

end

BigLoc = 1;

for i = 1 : SymLen

    for j = 1 : size(PlacementArrays{i},3)

        PlacementArrays{i}(:,:,j);

        ToLPMat(1:BSCount,BigLoc) = reshape(PlacementArrays{i}(:,:,j)',[],1);

        BigLoc = BigLoc + 1;

    end

end

if (size(PolyominoCount,1) == 1)

    PolyominoCount = PolyominoCount';

end

ToLPObj = [ reshape(Board',[],1) ; PolyominoCount ];

fileLocation = convertCharsToStrings(fileLocation);

polyomino_lp_write(fileLocation,'Solving a Polyomino Tiling Problem',size(ToLPMat,1),size(ToLPMat,2),ToLPMat,ToLPObj);

end
