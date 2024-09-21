#Possible partitions creates n-tuples with a particular sum of entries.
#Partitioner takes in the sizes of the board (Vertical then Horizontal) and the number of blockers. 
#   After some set up it goes into if statements for each case determined in the paper. Then it uses PossiblePartitions
#   to generate a list of n-tuples and throws out those which fail the conditions for a particular board type
#   given in the paper.

import copy

def PossiblePartitions (NumberIterations,SectionBlockerList,BlockerNumber):

    for i in range(BlockerNumber+1):

        SectionBlockerList[NumberIterations-1] = i

        if ((NumberIterations-1)==0):

            adder = sum(SectionBlockerList)

            if (adder==BlockerNumber):
                
                yield SectionBlockerList
            else:
                pass
                

        else:
            yield from PossiblePartitions(NumberIterations-1,SectionBlockerList,BlockerNumber)

def Partitioner (Vertical, Horizontal, NumberBlockers):

    
    NumberSections = 0

    VParity = Vertical % 2
    HParity = Horizontal % 2

    VerticalHalf = 0
    HorizontalHalf = 0

    if (VParity==1):
        VerticalHalf = (Vertical - 1) / 2
    else:
        VerticalHalf = Vertical / 2

    if (HParity==1):
        HorizontalHalf = (Horizontal - 1) / 2
    else:
        HorizontalHalf = Horizontal / 2

    #Section Areas

    CornerAreas = HorizontalHalf * VerticalHalf
    VerticalStrips = VerticalHalf
    HorizontalStrips = HorizontalHalf

    if(Vertical==1):
        CornerAreas = HorizontalHalf

    if(Horizontal==1):
        CornerAreas = VerticalHalf

    if (HParity == VParity):

        if (HParity == 0): 
            NumberSections = 4

        else: 
            NumberSections = 9

    else:
            NumberSections = 6

    if((Vertical==1) or (Horizontal==1)):

        if(HParity==VParity):
            NumberSections = 3

        else:
            NumberSections = 2

    #Set up Cases for NumberSections

    BoardPartitions = []

    #Possible forms of BoardP depending on NumberSections:
    #[la1,la2,la3,la4,de1,de2,de3,de4,c]
    #[la1,la2,la3,la4,de1,de2]
    #[la1,la2,la3,la4]

    if (NumberSections==4): #EvenEven Board

        if (Horizontal==Vertical):
            for BoardP in PossiblePartitions(4,[0,0,0,0],NumberBlockers):
                if (max(BoardP)>CornerAreas):
                    pass
                elif (BoardP[0]!=max(BoardP)):
                    pass
                elif (BoardP[1]<BoardP[3]):
                    pass
                elif ((BoardP[0]==BoardP[1]) and (BoardP[2]<BoardP[3])):
                    pass
                else:
                    yield BoardP
        
        else: 
            for BoardP in PossiblePartitions(4,[0,0,0,0],NumberBlockers):
                if(max(BoardP)>CornerAreas):
                    pass
                elif(BoardP[0]!=max(BoardP)):
                    pass
                elif((BoardP[0]==BoardP[2]) and (BoardP[1]<BoardP[3])):
                    pass
                elif((BoardP[0]==BoardP[1]) and (BoardP[2]<BoardP[3])):
                    pass
                elif((BoardP[0]==BoardP[3]) and (BoardP[1]<BoardP[2])):
                    pass
                else:
                    yield BoardP

    elif(NumberSections==9): #OddOdd Board

        if(Horizontal==Vertical):
            for BoardP in PossiblePartitions(9,[0,0,0,0,0,0,0,0,0],NumberBlockers):
                Strips = max(BoardP[4],BoardP[5],BoardP[6],BoardP[7])
                Lambdas = max([BoardP[Num] for Num in range(0,4)])
                if(Lambdas>CornerAreas):
                    pass
                elif(Strips>VerticalStrips):
                    pass
                elif(Strips>HorizontalStrips):
                    pass
                elif(BoardP[8]>1):
                    pass
                elif(BoardP[0]!=Lambdas):
                    pass
                elif(BoardP[1]<BoardP[3]): 
                    pass
                elif((BoardP[0]==BoardP[1]) and (BoardP[2]<BoardP[3])):
                    pass
                elif(((BoardP[0]==BoardP[2]) and (BoardP[1]!=BoardP[3])) and ((BoardP[4]<BoardP[5]) or ((BoardP[4]==BoardP[5]) and (BoardP[6]<BoardP[7])))):
                    pass
                elif(((BoardP[1]==BoardP[3]) and (BoardP[0]!=BoardP[2])) and ((BoardP[4]<BoardP[7]) or ((BoardP[4]==BoardP[7]) and (BoardP[5]<BoardP[6])))):
                    pass
                elif((((BoardP[0]==BoardP[1]) and (BoardP[2]==BoardP[3])) and (BoardP[0]!=BoardP[2])) and (BoardP[5]<BoardP[7])):
                    pass
                elif((((BoardP[0]==BoardP[1]) and (BoardP[1]==BoardP[2])) and (BoardP[2]==BoardP[3])) and (((BoardP[4]!=Strips) or (BoardP[5]<BoardP[7])) or ((BoardP[4]==BoardP[5]) and (BoardP[6]<BoardP[7])))):
                    pass
                elif((((BoardP[0]==BoardP[2]) and (BoardP[1]==BoardP[3])) and ((BoardP[4]!=Strips) or ((BoardP[4]==BoardP[5]) and (BoardP[6]<BoardP[7])) or ((BoardP[4]==BoardP[6]) and (BoardP[5]<BoardP[7])) or ((BoardP[4]==BoardP[7]) and (BoardP[5]<BoardP[6]))))):
                    pass
                else:
                    yield BoardP

        else:
            for BoardP in PossiblePartitions(9,[0,0,0,0,0,0,0,0,0],NumberBlockers):
                HStrips = max(BoardP[5],BoardP[7])
                VStrips = max(BoardP[4],BoardP[6])
                Lambdas = max([BoardP[Num] for Num in range(0,4)])
                if(Lambdas>CornerAreas):
                    pass
                elif(VStrips>VerticalStrips):
                    pass
                elif(HStrips>HorizontalStrips):
                    pass
                elif(BoardP[0]!=Lambdas):
                    pass
                elif(BoardP[8]>1):
                    pass
                elif((BoardP[0]==BoardP[2]) and ((BoardP[1]<BoardP[3]) or ((BoardP[1]==BoardP[3]) and ((BoardP[4]<BoardP[6]) or ((BoardP[4]==BoardP[6]) and (BoardP[5]<BoardP[7])))))):
                    pass
                elif((BoardP[0]==BoardP[1]) and ((BoardP[2]<BoardP[3]) or ((BoardP[2]==BoardP[3]) and (BoardP[5]<BoardP[7])))):
                    pass
                elif((BoardP[0]==BoardP[3]) and ((BoardP[1]<BoardP[2]) or ((BoardP[1]==BoardP[2]) and (BoardP[4]<BoardP[6])))):
                    pass
                else:
                    yield BoardP

    elif(NumberSections==6): #EvenOdd Board
        for BoardP in PossiblePartitions(6,[0,0,0,0,0,0],NumberBlockers):
            Strips = max(BoardP[4],BoardP[5])
            Lambdas = max([BoardP[Num] for Num in range(0,4)])
            if(Lambdas>CornerAreas):
                pass
            elif((Strips>VerticalStrips) and (HParity == 1)):
                pass
            elif((Strips>HorizontalStrips) and (HParity == 0)):
                pass
            elif(BoardP[0]!=Lambdas):
                pass
            elif((BoardP[0]==BoardP[2]) and ((BoardP[1]<BoardP[3]) or ((BoardP[1]==BoardP[3]) and (BoardP[4]<BoardP[5])))):
                pass
            elif((BoardP[0]==BoardP[1]) and (BoardP[2]<BoardP[3])):
                pass
            elif((BoardP[0]==BoardP[3]) and ((BoardP[1]<BoardP[2]) or ((BoardP[1]==BoardP[2]) and (BoardP[4]<BoardP[5])))):
                pass
            else:
                yield BoardP

    elif(NumberSections==3):

        for BoardP in PossiblePartitions(3,[0,0,0],NumberBlockers):
            if(BoardP[2]>1):
                pass
            elif(max(BoardP)>CornerAreas):
                pass
            elif(BoardP[1]>BoardP[0]):
                pass
            else:
                yield BoardP

    elif(NumberSections==2):

        for BoardP in PossiblePartitions(2,[0,0],NumberBlockers):
            if(max(BoardP)>CornerAreas):
                pass
            elif(BoardP[1]>BoardP[0]):
                pass
            else:
                yield BoardP

    else:
        pass
