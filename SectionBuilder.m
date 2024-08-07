function [BlockerPlacements] = SectionBuilder(SectionsBlockerVector,LastSection,BoardVertical,BoardHorizontal,NumberOfBlockers)
%[BlockerPlacements] = SectionBuilder(SectionsBlockerVector,LastSection,BoardVertical,BoardHorizontal,NumberOfBlockers)
%   
%   SectionsBlockerVector is a list of matrices corresponding to sections
%   on the board
%   LastSection is the last section that is generated
%   BoardVertical and BoardHorizontal are the Height and Width of the board
%   respectively
%   NumberOfBlockers is the number of blockers on the board.
%
%   This function generates a matrix using the sections it takes as input,
%   then creates the vector BlockerPlacements from this matrix. This vector
%   corresponds to the locations of each of the blockers on the board.

BlockerPlacements = cell(1,NumberOfBlockers);

SectionsVector = SectionsBlockerVector;

Vertical = double(BoardVertical);
Horizontal = double(BoardHorizontal);

Board = zeros(Vertical,Horizontal);

VHalf = floor(Vertical/2);
HHalf = floor(Horizontal/2);

CaseTest = length(SectionsVector) + 1;

switch CaseTest

    case 9
        Board(1:VHalf,1:HHalf) = SectionsVector{1};
        Board(1:VHalf,(HHalf+2):end) = SectionsVector{2};
        Board((VHalf+2):end,1:HHalf) = SectionsVector{4};
        Board((VHalf+2):end,(HHalf+2):end) = SectionsVector{3};
        Board(1:(VHalf),HHalf+1) = SectionsVector{5};
        Board(VHalf+1,(HHalf+2):end) = SectionsVector{6};
        Board((VHalf+2):end,HHalf+1) = SectionsVector{7};
        Board(VHalf+1,1:HHalf) = SectionsVector{8};
        Board(VHalf+1,HHalf+1) = LastSection{1};

    case 6

        if(mod(Vertical,2)==0) %This has a horizontal middle

        Board(1:VHalf,1:HHalf) = SectionsVector{1};
        Board(1:VHalf,(HHalf+2):end) = SectionsVector{2};
        Board((VHalf+1):end,(HHalf+2):end) = SectionsVector{3};
        Board((VHalf+1):end,1:HHalf) = SectionsVector{4};
        Board(1:VHalf,HHalf+1) = SectionsVector{5};
        Board((VHalf+1):end,HHalf+1) = LastSection{1};

        elseif(mod(Vertical,2)==1) %This has a vertical middle

        Board(1:VHalf,1:HHalf) = SectionsVector{1};
        Board(1:VHalf,(HHalf+1):end) = SectionsVector{2};
        Board((VHalf+2):end,(HHalf+1):end) = SectionsVector{3};
        Board((VHalf+2):end,1:HHalf) = SectionsVector{4};
        Board(VHalf+1,1:HHalf) = SectionsVector{5};
        Board(VHalf+1,(HHalf+1):end) = LastSection{1};

        else

            print("Something went wrong. You somehow modded a whole number out by 2 and didn't get 0 or 1")
            quit

        end

    case 4

        Board(1:VHalf,1:HHalf) = SectionsVector{1};
        Board(1:VHalf,(HHalf+1):end) = SectionsVector{2};
        Board((VHalf+1):end,(HHalf+1):end) = SectionsVector{3};
        Board((VHalf+1):end,1:HHalf) = LastSection{1};

    case 3

        if(Vertical==1) %Horizontal Middle

        Board(1,1:HHalf) = SectionsVector{1};
        Board(1,(HHalf+2):end) = SectionsVector{2};
        Board(1,HHalf+1) = LastSection{1};

        elseif(Vertical>1) %Vertical Middle

        Board(1:VHalf,1) = SectionsVector{1};
        Board((VHalf+2):end,1) = SectionsVector{2};
        Board(VHalf+1,1) = LastSection{1};

        else

            print("Something went very wrong. How did you do this? You have a non-positive vertical length or a decimal vertical.")
            quit

        end

    case 2

        if(Vertical==1) %Horizontal Pieces

            Board(1,1:HHalf) = SectionsVector{1};
            Board(1,(HHalf+1):end) = LastSection{1};

        elseif(Vertical>1) %Vertical pieces

            Board(1:VHalf,1) = SectionsVector{1};
            Board((VHalf+1):end,1) = LastSection{1};

        else

            print("Somehow you broke it. the vertical should only be able to be a positive integer.")
            quit

        end

end

Locator = find(Board') - 1;

for i = 1:NumberOfBlockers

    col = mod(Locator(i),Horizontal) + 1;
    row = floor(Locator(i)/Horizontal) + 1;


    BlockerPlacements{i} = [row col];

end

end