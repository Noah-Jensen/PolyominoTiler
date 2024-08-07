#Function to generate the list input into SymmetrySolverGeneral.GeneralPartition

def SectionSizeGenerator(BoardVertical,BoardHorizontal):
    
    VerticalHalf = (BoardVertical - (BoardVertical % 2))/2
    HorizontalHalf = (BoardHorizontal - (BoardHorizontal % 2))/2

    CornerSection = [VerticalHalf,HorizontalHalf]

    VerticalMiddleSection = [VerticalHalf,BoardHorizontal % 2]
    HorizontalMiddleSection = [BoardVertical % 2,HorizontalHalf]
    Center = [BoardVertical % 2,BoardHorizontal % 2]

    SectionSizes = [CornerSection,CornerSection,CornerSection,CornerSection,VerticalMiddleSection,HorizontalMiddleSection,VerticalMiddleSection,HorizontalMiddleSection,Center]

    SectionSizes = [Size for Size in SectionSizes if ((Size[0]!=0) and (Size[1]!=0))]

    return [SectionSizes, len(SectionSizes)]
