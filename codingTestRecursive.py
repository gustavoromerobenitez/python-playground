#!/usr/bin/python3

def lowestPositiveIntRec(A):

    print("Checking {}".format(A))

    length = len(A)

    if length == 1:
        print("Returning 0")
        return 0

    if length == 2:
        if A[1] > A[0]+1:
            print("Returning {}".format(A[0]+1))
            return A[0]+1
        else:
            print("Returning 0")
            return 0
    else:  # Length > 2
        leftA = A[0:int(length/2)]
        rightA = A[int(length/2):length]
        gap = [leftA[len(leftA)-1], rightA[0]]
        lowestLeft = lowestPositiveIntRec(leftA)
        if lowestLeft == 0:
            lowestValueInGap = lowestPositiveIntRec(gap)
            if lowestValueInGap == 0:
                lowestRight = lowestPositiveIntRec(rightA)
                if lowestRight == 0:
                    print("Returning 0")
                    return 0
                else:
                    print("Returning {}".format(lowestRight))
                    return lowestRight
            else:
                print("Returning {}".format(lowestValueInGap))
                return lowestValueInGap
        else:
            print("Returning {}".format(lowestLeft))
            return lowestLeft


def lowestPositiveInt(A):

    A.sort()

    try:
        index = A.index(1)
    except ValueError:
        return 1

    # Remove all negatives and zero if 1 is found
    A = A[index:]

    lowest = lowestPositiveIntRec(A)
    if lowest == 0:
        return A[len(A)-1]+1
    else:
        return lowest


def main():
    sample1 = [-1, -3, -47, -10, 0, 27, 3, 2, 27]
    sample2 = [0, 1, 2, 3, 7, 25, -12, -14, -17]
    sample3 = [1, 1, 2, 3, 3, 4, -10, -27, 42]

    print("Sample 1: {}".format(lowestPositiveInt(sample1)))
    print("Sample 2: {}".format(lowestPositiveInt(sample2)))
    print("Sample 3: {}".format(lowestPositiveInt(sample3)))


main()
