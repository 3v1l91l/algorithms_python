def sort(sortList):
    """
    Sort list item in an ascending order

    :param sortList: list to be sorted
    :return: sorted list
    """

    for i in range(0, len(sortList)):
        iMin = i

        for j in range(i+1, len(sortList)):
            if sortList[iMin] > sortList[j]:
                iMin = j

        if sortList[i] != sortList[iMin]:
            sortList[i], sortList[iMin] = sortList[iMin], sortList[i]

    return sortList