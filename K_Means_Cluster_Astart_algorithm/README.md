## Running Instructions
1. Requires a maze file
2. Need to specify the path output file
3. Need to specify the nodes output file

Way to run: `py 2081349_problem2.py -m maze.txt -p path.txt -n nodes.txt`

- `-m maze.txt` takes `maze.txt` as the input file
- `-p path.txt` output the paths to a file called `path.txt`
- `-n nodes.txt` output the nodes to a file called `nodes.txt`


## Path Output File


22111

12221

10121

10021

11122

## Node Output File


33111

13331

13131

13331

11133

## Path and Node Output Explanation
0 means you can move to that position

1 means that there is a wall at that position

2 in solution path means the positions we move to so that we reach our goal

3 in the node matrix means expanded nodes, a 3 means that node has been expanded.