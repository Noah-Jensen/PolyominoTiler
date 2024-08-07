import matlab.engine
import cplex
from itertools import combinations
from pathlib import Path

#Functions to generate and solve LP files for the desired board situation.

# PartitionVector is the BoardPartition which will be iterated on
# SectionsBlockerVector is the list of currently generated sections
# SectionSizeVector is a list of the dimensions of each section Lambda then Delta then c
# NumberOfSections is the number of sections based on the total dimension of the board
# Polyominoes is a matlab object which contains matrices for all polyominoes that will be used to tile the board
# PolyominoCount is a the number of each polyomino that will be used
# BoardSize is a list of the dimensions of the board. Here we're assuming a rectangular board
# Count tells you which iteration of the loop it is when there is no solution.
# FolderName is the name for where everything will be stored
# TotalBlockersOnBoard is the total number of blockers placed on the board
# NumberOfBlockers is the number of blockers in that current section
# SectionSize are the dimensions of the current section
# SubFolderName is name of the folder within FolderName where the unsolvable outputs are saved
# BlockerPlacements is a list of where blockers are placed in the current section

eng = matlab.engine.start_matlab()
eng.cd(r'<Matlab Code Folder Location>',nargout=0)

c = cplex.Cplex()

LPFolderLocation = "<Folder where you want your LP file stored>"
OutputLoc = "<Folder where you want the solution files stored>"
Count = 0

def GenerateSection(TotalBlockersOnBoard,NumberOfBlockers,SectionSize): 

    SectionCount = SectionSize[0] * SectionSize[1]

    for section in combinations(list(range(1,(SectionCount+1))),NumberOfBlockers):
        section = list(section) + list([0] * (TotalBlockersOnBoard - NumberOfBlockers))
        yield section



def Solver(Polyominoes,PolyominoCount,BoardSize,FolderName,SubfolderName,BlockerPlacements,Count):

    eng.genLPgeneral(Polyominoes,PolyominoCount,eng.blockerBoard(BoardSize[0],BoardSize[1],BlockerPlacements),LPFolderLocation + "\\" + FolderName + "\\rewrittenfile.lp",nargout=0) 

    c.read(LPFolderLocation + "\\" + FolderName + "\\rewrittenfile.lp")
    c.solve()

    print(c.solution.get_status())

    if(Path(OutputLoc + "\\" + FolderName + "\\" + SubfolderName).is_dir()):
        pass
    else:
        Path(OutputLoc + "\\" + FolderName + "\\" + SubfolderName).mkdir(parents=True, exist_ok=True)

    if (c.solution.get_status()!=101):

        with open(OutputLoc + "\\" + FolderName + "\\" + SubfolderName + "\\Dice Pattern " + str(Count) +".txt", "w") as f:
            f.write("This pattern is unsolvable. It uses these blocker locations:")
            for DiceNum in range(0,len(BlockerPlacements)):
                f.write("\nBlocker Placement " + str(DiceNum) + " : " + str(BlockerPlacements[DiceNum])) 

            f.write("\nWith these entries from each respectively")



def GeneralPartition(PartitionVector,SectionsBlockerVector,SectionSizeVector,NumberOfSections,Polyominoes,PolyominoCount,BoardSize,Count,FolderName):

    for ValidCheck in range(NumberOfSections):
        if(PartitionVector[ValidCheck]>(SectionSizeVector[ValidCheck][0] * SectionSizeVector[ValidCheck][1])):
            raise ValueError('At least one of your sections has too many blockers! The first one is in position ' + str(ValidCheck))
        else:
            pass

    TotalBlockersOnBoard = sum(PartitionVector)
    Iterator = len(SectionsBlockerVector)
    NumberOfBlockers = PartitionVector[Iterator]
    SectionSize = SectionSizeVector[Iterator]


    for section in GenerateSection(TotalBlockersOnBoard,NumberOfBlockers,SectionSize):

        if (len(SectionsBlockerVector) >= (NumberOfSections - 1)):
            Count += 1

            BlockerPlacements = eng.SectionBuilder(SectionsBlockerVector,[eng.SectionGenerator(section,SectionSize)],BoardSize[0],BoardSize[1],TotalBlockersOnBoard) 
            SubfolderName = str(PartitionVector[0])

            for SubfolderNamer in range(1,len(PartitionVector)):
                SubfolderName = SubfolderName + str(PartitionVector[SubfolderNamer])

            Solver(Polyominoes,PolyominoCount,BoardSize,FolderName,SubfolderName,BlockerPlacements,Count)

            print(PartitionVector)

        else:

            Count = GeneralPartition(PartitionVector,SectionsBlockerVector + [eng.SectionGenerator(section,SectionSize)],SectionSizeVector,NumberOfSections,Polyominoes,PolyominoCount,BoardSize,Count,FolderName) 

    return Count

