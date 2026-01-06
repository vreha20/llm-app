def extract_claims(backstory_text):
    """
    Converts backstory text into atomic factual claims.
    """
    claims = []

    sentences = backstory_text.split(".")
    for s in sentences:
        s = s.strip()
        if len(s) > 5:
            claims.append(s.lower())

    return claims


if __name__ == "__main__":
    with open("backstory.txt", "r") as f:
        text = f.read()

    claims = extract_claims(text)
    for c in claims:
        print("-", c)
