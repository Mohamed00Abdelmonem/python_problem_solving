def gridChallenge(grid):
    # Write your code here
    sorted_row = ["".join(sorted(i)) for i in grid]
    for col in range(len(grid[0])):
        current_col = [row[col] for row in sorted_row]
        if current_col != sorted(current_col):
              return "NO"

    return 'YES'
    

print(gridChallenge(["cbad", "sagg", "afgga"]))
