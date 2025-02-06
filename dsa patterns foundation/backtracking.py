def backtrack(path, choices):
    if valid(path):
        res.append(path[:])  # Make a copy of path

    for choice in choices:
        if choice in path: 
            continue  # Skip invalid choices

        path.append(choice)
        backtrack(path, choices)
        path.pop()  # Backtrack
