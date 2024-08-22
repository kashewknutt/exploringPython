from collections import deque

# Define the directions of movement (up, down, left, right)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRECTION_NAMES = ["Right", "Left", "Down", "Up"]

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def bfs(start, end):
    # Create a queue for BFS
    queue = deque([(start, [], [])])
    
    # Create a set to store visited states
    visited = set()
    visited.add(tuple(map(tuple, start)))

    while queue:
        current_state, path, directions = queue.popleft()
        
        # If the end state is reached, return the path and directions
        if current_state == end:
            return path + [current_state], directions
        
        # Find the position of the empty space (0)
        x, y = [(ix, iy) for ix, row in enumerate(current_state) for iy, i in enumerate(row) if i == 0][0]

        for i, (dx, dy) in enumerate(DIRECTIONS):
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny):
                # Swap the zero with the adjacent element
                new_state = [row[:] for row in current_state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                
                # Convert the state to a tuple for immutability and hashing
                state_tuple = tuple(map(tuple, new_state))
                
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    
                    # Append the new state and direction to the path
                    queue.append((new_state, path + [current_state], directions + [DIRECTION_NAMES[i]]))
    
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

# Run BFS to find the path
final_path, directions = bfs(start_state, end_state)

# Print the result
if isinstance(final_path, list):
    print("Shortest Path (in matrix configurations with directions):")
    for step, (state, direction) in enumerate(zip(final_path[1:], directions), 1):
        print(f"Step {step}: Move {direction}")
        for row in state:
            print(row)
        print()
else:
    print(final_path)
