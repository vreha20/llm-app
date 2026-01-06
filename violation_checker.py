def check_violations(claims, constraints):
    violations = []
    score = 0

    for claim in claims:
        for c in constraints:

            # Psychological contradiction
            if "fear of water" in claim and c["constraint_type"] == "psychological_fear":
                violations.append(("soft", claim))
                score += 2

            # Commitment contradiction
            if "avoid leadership" in claim and c["constraint_type"] == "commitment":
                violations.append(("hard", claim))
                score += 5

            # Moral contradiction
            if "non-violence" in claim and c["constraint_type"] == "strong_negation":
                violations.append(("soft", claim))
                score += 2

    return violations, score
