def decide(score, threshold=5):
    """
    Returns:
    1 -> consistent
    0 -> inconsistent
    """
    if score > threshold:
        return 0
    return 1


if __name__ == "__main__":
    print(decide(3))  # expected 1
    print(decide(8))  # expected 0
