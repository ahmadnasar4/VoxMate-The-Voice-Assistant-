memory_storage = {}

def remember(key, value):
    """Store a memory entry."""
    memory_storage[key] = value
    return f"Remembered that {key} is {value}."

def recall(key):
    """Recall a memory entry."""
    if key in memory_storage:
        return f"I remember that {key} is {memory_storage[key]}."
    else:
        return f"I don't have a memory of {key}."
