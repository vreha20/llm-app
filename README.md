## Purpose
This module parses hypothetical character backstories into atomic claims,
checks them against narrative constraints extracted from a novel,
and produces a binary consistency decision.

## Components
- claim_extractor.py: backstory → claims
- violation_checker.py: claims vs constraints
- decision.py: final consistency label
