#!/usr/bin/python3


def lowestPositiveInt(A):

    A.sort()

    index = -1
    try:
        index = A.index(1)
    except ValueError:
        return 1

    # Remove all negatives and zero if 1 is found
    # if index >= 0:
    A = A[index:]
    length = len(A)

    i = 1
    found = 0
    while i < length and found == 0:
        if A[i] > (A[i-1]+1):
            found = A[i-1]+1
        i = i+1

    if found > 0:
        return found
    else:
        return A[length-1]+1


def main():
    sample1 = [-1, -3, -47, -10, 0, 27, 27, 0, 1, 1]
    sample2 = [0, 1, 2, 3, 7, 25, -12, -14, -17, 4, 4]
    sample3 = [1, 1, 5, 27, -100, -234, 3, 2, 3, 4, 4]

    print("Sample 1: {}".format(lowestPositiveInt(sample1)))
    print("Sample 2: {}".format(lowestPositiveInt(sample2)))
    print("Sample 3: {}".format(lowestPositiveInt(sample3)))


main()
