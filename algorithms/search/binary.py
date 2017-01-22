def search(searchList, searchItem):
    """
    Searches for a given search item in a given search list and
    returns its index.

    :param searchList: list of integers
    :param searchItem: integer to search for
    :return: index of the found item or False if not found
    """

    highIndex = len(searchList) -1
    lowIndex = 0

    while lowIndex <= highIndex:
        midIndex = (highIndex + lowIndex) // 2
        midItem = searchList[midIndex]

        if searchItem == midItem:
            return midIndex
        elif searchItem > midItem:
            lowIndex = midIndex + 1
        else:
            highIndex = midIndex - 1
    return False