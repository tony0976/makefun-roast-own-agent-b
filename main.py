# The sting is the gap between asking and doing: it asked, then built
# the wrong thing with total confidence, and delivered it proudly.
"""Writes one roast of the AI agent it runs on to /output/entry.txt."""
import os

TEXT = "My agent asked what I wanted, then spent an hour confidently building the wrong thing and presented it like a rescue dog with a dead bird."

# Rule: the roast must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
