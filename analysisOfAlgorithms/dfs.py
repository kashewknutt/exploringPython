from collections import deque

# Define the directions of movement (up, down, left, right)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def dfs(start, end):
    # Create a stack for DFS
    stack = [(start, "")]
    
    # Create a set to store visited states
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while stack:
        current_state, path = stack.pop()
        
        # If the end state is reached, return the path
        if current_state == end:
            return path
        
        # Find the position of the empty space (0)
        x, y = [(ix, iy) for ix, row in enumerate(current_state) for iy, i in enumerate(row) if i == 0][0]

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny):
                # Swap the zero with the adjacent element
                new_state = [row[:] for row in current_state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                
                # Convert the state to a tuple for immutability and hashing
                state_tuple = tuple(map(tuple, new_state))
                
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    
                    # Determine the direction moved and update the path
                    direction = ''
                    if dx == -1 and dy == 0:
                        direction = 'Up'
                    elif dx == 1 and dy == 0:
                        direction = 'Down'
                    elif dx == 0 and dy == -1:
                        direction = 'Left'
                    elif dx == 0 and dy == 1:
                        direction = 'Right'
                    
                    stack.append((new_state, path + direction + " "))
                    #print(stack[-1])
    
    return "No solution found"

# Example start and end states
start_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

end_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

# Run DFS to find the path
result = dfs(start_state, end_state)

# Print the result
print("Path to solution:", result)
