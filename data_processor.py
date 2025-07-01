def parse_commits(commits):
    author_count = {}
    for commit in commits:
        author = commit.get("author", "unknown")
        author_count[author] = author_count.get(author, 0) + 1
    return author_count

def calculate_severity(scores):
    return {
        "low": scores.count("low"),
        "medium": scores.count("medium"),
        "high": scores.count("high"),
    }
