#Function to generate the list input into SymmetrySolverGeneral.GeneralPartition

def SectionSizeGenerator(BoardVertical,BoardHorizontal):
    
    VerticalHalf = int((BoardVertical - (BoardVertical % 2))/2)
    HorizontalHalf = int((BoardHorizontal - (BoardHorizontal % 2))/2)

    CornerSection = [VerticalHalf,HorizontalHalf]

    VerticalMiddleSection = [VerticalHalf,int(BoardHorizontal % 2)]
    HorizontalMiddleSection = [int(BoardVertical % 2),HorizontalHalf]
    Center = [int(BoardVertical % 2),int(BoardHorizontal % 2)]

    SectionSizes = [CornerSection,CornerSection,CornerSection,CornerSection,VerticalMiddleSection,HorizontalMiddleSection,VerticalMiddleSection,HorizontalMiddleSection,Center]

    SectionSizes = [Size for Size in SectionSizes if ((Size[0]!=0) and (Size[1]!=0))]

    return [SectionSizes, len(SectionSizes)]
