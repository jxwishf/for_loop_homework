def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    for i in range(n + 1):
        result += str(i) + " "
    return result.strip()  