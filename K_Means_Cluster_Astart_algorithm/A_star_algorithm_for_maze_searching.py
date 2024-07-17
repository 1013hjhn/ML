import heapq
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--maze", required = True, help = "maze filename")
parser.add_argument("-p", "--path", required = True, help = "path filename")
parser.add_argument("-n", "--nodes", required = True, help = "nodes filename")
args = parser.parse_args()

def read_maze(file_path):
    with open(file_path, 'r') as file:
        dimensions = file.readline()  # Read the dimensions line and discard it
        maze = [list(map(int, line.strip().split())) for line in file.readlines()]
    return maze

def write_output(maze, path, nodes, student_id):
    path_maze = [row.copy() for row in maze]
    nodes_maze = [row.copy() for row in maze]

    for p in path:
        path_maze[p[0]][p[1]] = 2
    
    for n in nodes:
        nodes_maze[n[0]][n[1]] = 3

    with open(args.path, 'w') as file:
        file.write(str(student_id) + '\n')
        for row in path_maze:
            file.write(''.join(map(str, row)) + '\n')

    with open(args.nodes, 'w') as file:
        file.write(str(student_id) + '\n')
        for row in nodes_maze:
            file.write(''.join(map(str, row)) + '\n')

def a_star_algorithm(maze, start, goal):

    def heuristic(node):
        h_value = 0
        h = 3  
        
        if h == 1:
            h_value = 0
        elif h == 2:
            h_value = height - node[0] + width - node[1]
        elif h == 3:
            h_value = math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
        
        return h_value

    h = heuristic
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    start_g = 0
    start_h = h(start)
    start_node = (start, start_g, start_h)
    open_list = [start_node]
    closed_list = set()
    
    previous = {}
    path = []
    nodes = []
    
    while open_list:
        current = heapq.heappop(open_list)
        current_loc = current[0]
    
        if current_loc == goal:
            path = []
            while current_loc in previous:
                path.append(current_loc)
                current_loc = previous[current_loc]
            path.append(start)
            path.reverse()
            closed_list.add(goal)
            return path, list(closed_list)
    
        closed_list.add(current_loc)
    
        for delta_row, delta_col in directions:
            neighbor = (current_loc[0] + delta_row, current_loc[1] + delta_col)
    
            if (neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(maze) or neighbor[1] >= len(maze[0]) or
                    maze[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_list):
                continue
    
            neighbor_g = current[1] + 1
            neighbor_node = None
    
            for node in open_list:
                if node[0] == neighbor:
                    neighbor_node = node
                    break
    
            if neighbor_node is None:
                neighbor_node = (neighbor, float('inf'), float('inf'))
    
            if neighbor_g >= neighbor_node[1]:
                continue
    
            previous[neighbor] = current_loc
            heapq.heappush(open_list, (neighbor, neighbor_g, neighbor_g + h(neighbor)))

    return path, nodes

maze_file = args.maze
maze = read_maze(maze_file)
start = (0, 0)
goal = (len(maze) - 1, len(maze[0]) - 1)
path, nodes = a_star_algorithm(maze, start, goal)
output = write_output(maze, path, nodes, 20813439)