def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    bedir = []
    for i in list1:
        bedir += [i.title()]


    return list (bedir)

print(main(["alisher,bekzod"]))    