from data_processor import parse_commits, calculate_severity
from utils import format_commit_message

if __name__ == "__main__":
    dummy_commits = [
        {"author": "Alice", "message": "Initial commit", "timestamp": 1719720000},
        {"author": "Bob", "message": "Fix login issue", "timestamp": 1719730000},
        {"author": "Alice", "message": "Refactor dashboard", "timestamp": 1719740000},
    ]

    print("Formatted Commit Messages:\n")
    for c in dummy_commits:
        print(format_commit_message(c["author"], c["message"], c["timestamp"]))

    print("\nCommit Count by Author:\n", parse_commits(dummy_commits))

    dummy_scores = ["low", "high", "medium", "low", "high"]
    print("\nSeverity Summary:\n", calculate_severity(dummy_scores))
