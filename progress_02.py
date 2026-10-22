"""A simple checklist for continuing Python practice."""


def completed_topics(topics: list[str]) -> int:
    """Count the topics completed in a practice session."""
    return len(topics)


if __name__ == "__main__":
    topics = ["functions", "lists", "dictionaries"]
    print(f"Completed topics: {completed_topics(topics)}")
