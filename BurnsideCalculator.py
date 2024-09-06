#BoardType determines the type of board given the number of horizontal and vertical cells in the board.
#combin is n choose k, where if k is not a non-negative integer, it returns zero, otherwise it returns comb(n,k)
#BurnsideCalculator uses the formulas from "An Approach to Classifying Game Boards with Blocked Cells" to calculate the
#   number of equivalence classes for a Horizontal x Vertical board with BlockerNumber blockers.

from math import comb
from math import floor

def BoardType(Horizontal,Vertical):

    Hmod = Horizontal % 2
    Vmod = Vertical % 2

    if(Horizontal==Vertical): #square

        if (Hmod == 0): #even
            
            TypeVar = "EvenSquare"

        else:

            TypeVar = "OddSquare"

    else:

        if ((Horizontal == 1) or (Vertical == 1)):

            TypeVar = "Line"

        elif((Hmod == 1) and (Vmod == 1)):

            TypeVar = "OddRectangle"

        elif((Hmod == 0) and (Vmod == 0)):

            TypeVar = "EvenRectangle"

        elif(((Hmod == 1) or (Vmod == 1)) and (Hmod != Vmod)):

            TypeVar = "EvenOddRectangle"

        else:

            TypeVar = "Invalid"


    return TypeVar


def combin(n,k):

    if ((k-floor(k)) != 0):
        return 0
    else:
        return comb(int(n),int(k))


def BurnsideCalculator(Horizontal,Vertical,BlockerNumber):

    typeBoard = BoardType(Horizontal,Vertical)

    r = BlockerNumber

    if(typeBoard == "EvenSquare"):

        k = Horizontal / 2

        ks = k * k

        rotZero = combin((4 * ks),r)
        rotNinety = combin(ks,(r / 4))
        rotHV = combin((2 * ks),(r / 2))
        refDiags = 0

        for t in range(int(min((r+1),(2 * k+1)))):

            refDiags += combin((2 * k), t) * combin((2 * ks - k), ((r - t) / 2))

        equivClassNum = (1 / 8) * (rotZero + 2 * rotNinety + 3 * rotHV + 2 * refDiags)
    
    elif(typeBoard == "OddSquare"):

        k = (Horizontal - 1) / 2

        kpo = k + 1
        kkpo = k * kpo
        tkkpo = 2 * kkpo
        tkpo = kpo + k
        ktkpo = k * tkpo
        tkpos = tkpo * tkpo

        rotZero = combin(tkpos,r)
        rotNinety = combin(kkpo,(r / 4)) + combin(kkpo, ((r - 1) / 4))
        rotOneeighty = combin(tkkpo,floor(r / 2))
        refHV = 0
        refDiags = 0

        for t in range(int(min((r+1),(2*k + 2)))):

            rmtdt = (r - t) / 2

            refHV += combin(tkpo,t) * combin(ktkpo, rmtdt)
            refDiags += combin(tkpo,t) * combin(ktkpo,rmtdt)

        equivClassNum = (1 / 8) * (rotZero + 2 * rotNinety + rotOneeighty + 2 * refHV + 2 * refDiags)


    elif(typeBoard == "EvenRectangle"):

        k = Horizontal / 2
        l = Vertical / 2

        tkl = 2 * k * l

        rotZero = combin((2 * tkl),r)
        refHV = combin(tkl,(r / 2))

        equivClassNum = (1 / 4) * (rotZero + 3 * (refHV))

    elif(typeBoard == "OddRectangle"):

        k = (Horizontal - 1) / 2
        l = (Vertical - 1) / 2

        tkpo = 2 * k + 1
        tlpo = 2 * l + 1
        kl = k * l
        tklpl = 2 * kl + l
        tklpk = 2 * kl + k

        rotZero = combin((tkpo * tlpo),r)
        rotOneeighty = combin((2 * kl + k + l),floor(r / 2))
        refH = 0
        refV = 0

        for t in range(int(min((r + 1),(2 * k + 2)))):

            refV += combin(tkpo,t) * combin(tklpl,((r - t) / 2))

        for t in range(int(min((r + 1),(2 * l + 2)))):

            refH += combin(tlpo,t) * combin(tklpk,((r - t) / 2))

        equivClassNum = (1 / 4) * (rotZero + rotOneeighty + refH + refV)

    elif(typeBoard == "EvenOddRectangle"):

        if((Horizontal % 2) == 0):

            k = Horizontal / 2
            l = (Vertical - 1) / 2

        else:

            k = Vertical / 2
            l = (Horizontal - 1) / 2

        ktlpo = k * (2 * l + 1)
        tk = 2 * k
        tkl = tk * l

        rotZero = combin((2 * ktlpo),r)
        rotOneeighty = combin(ktlpo,(r / 2))
        refV = 0

        for t in range(int(min((r + 1),(tk + 1)))):

            refV += combin(tk, t) * combin(tkl, ((r - t) / 2))

        equivClassNum = (1 / 4) * (rotZero + 2 * rotOneeighty + refV)

    elif(typeBoard == "Line"):

        if(Horizontal == 1):
            length = Vertical
        else:
            length = Horizontal

        if((length % 2) == 0):

            k = length / 2

            rotZero = combin((2 * k),r)
            refV = combin(k,(r / 2))

        else:

            k = (length - 1) / 2

            rotZero = combin((2 * k + 1), r)
            refV = combin(k,floor(r / 2))

        equivClassNum = (1 / 2) * (rotZero + refV)
    
    else:
        raise ValueError('BoardType returned an invalid board type, meaning the Horizontal and Vertical input values were not natural numbers greater than 0')

    return equivClassNum

#print(BurnsideCalculator(5,7,5)) count for burnside count for 5 x 7 with 5 blockers.
