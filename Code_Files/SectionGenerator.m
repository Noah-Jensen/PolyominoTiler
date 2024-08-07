function Section = SectionGenerator(section,SectionSize)
%Section = SectionGenerator(section,SectionSize)
%   
%   section is a vector which contains the locations of blockers
%   SectionSize is the size of the section being generated
%
%   This file generates a matrix with size specified by SectionSize. This
%   matrix will be a binary matrix representing the section generated with
%   ones where a blocker is placed.

NumberBlockers = length(section);

Section = zeros(SectionSize{1},SectionSize{2});

PlacementVector = zeros(SectionSize{1} * SectionSize{2},2);

for r = 1 : SectionSize{1}

    Placer = (1:SectionSize{2}) + (r-1) * SectionSize{2};

    r = double(r);

    PlacementVector(Placer,1) = r * ones(SectionSize{2},1);
    PlacementVector(Placer,2) = 1:SectionSize{2};

end


for i = 1 : NumberBlockers

    if (section{i}==0)

    else

        Section(PlacementVector(section{i},1),PlacementVector(section{i},2)) = 1;

    end

end
