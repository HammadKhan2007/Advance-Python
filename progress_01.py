"""A small example for tracking daily Python practice progress."""


def practice_summary(topic: str, minutes: int) -> str:
    """Return a readable summary of a practice session."""
    return f"Practiced {topic} for {minutes} minutes."


if __name__ == "__main__":
    print(practice_summary("functions", 30))
