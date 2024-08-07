import SymmetrySolverGeneral
import matlab.engine
import BoardPartitions
import SectionSizeGenerator

#Template to solve all VxH boards with N blockers using PolyominoCount number of polyominoes from Polyominoes

#Make sure to change lines 22, 26, and 27 in SymmetrySolverGeneral.py to your desired folder locations.

eng = matlab.engine.start_matlab()
eng.cd(r'<Matlab Code Folder Location>', nargout=0)

Polyomiones = eng.Polyominoes()
PolyominoCount = eng.PolyominoLimit()

V = 0 #Vertical Height Of The Board
H = 0 #Horizontal Width Of The Board
N = 0 #Number Of Blockers To Be Placed
[Sections, NumberOfSections] = SectionSizeGenerator.SectionSizeGenerator(V,H)

for partition in BoardPartitions.Partitioner(V,H,N):
    SymmetrySolverGeneral.GeneralPartition(partition,[],Sections,NumberOfSections,Polyomiones,PolyominoCount,[V,H],0,"<Desired folder name where unsolved boards will be stored>")
