from datetime import datetime

def format_commit_message(author, message, timestamp):
    formatted_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return f"[{formatted_time}] {author}: {message}"

def word_count(text):
    return len(text.strip().split())