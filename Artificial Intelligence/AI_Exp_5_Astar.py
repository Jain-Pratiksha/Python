# Exp 5 A* Search Algorithm
# Name: Pratiksha Jain

# A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final state.
# It is used in various applications, such as maps. In maps the A* algorithm is used to calculate the shortest
# distance between the source (initial state) and the destination (final state).

class Node:
    def __init__(self, val, hval):
        self.val = val  # name of city
        self.hval = hval  # h value (estimates cost)
        self.adjecencies = []  # aadjenceny nodes

    def add(self, adjecencies):
        self.adjecencies = adjecencies  # add aadjenceny nodes Edge (Node, costval)


class Edge:
    def __init__(self, targetNode, costVal):
        self.targetNode = targetNode  # object of node
        self.costVal = costVal  # cost val(actual cost)


def AstarSearch(source, goal):
    # queue to maintain BFS tree
    queue = []

    # set to add visited nodes
    visited_set = set()

    # path to store efficient search path
    path = []

    # append source node in queue
    queue.append(source)

    # append value of a source node in path
    path.append(source.val)

    # flag to check if goal node is found or not
    found = False

    # run while queue is not empty and goal is not found
    while (len(queue) != 0 and found == False):

        # temporary list to store f(n) value of all adjacent nodes
        temp_f_val = []

        # get current node from queue to explore its adjacent nodes
        current = queue[0]

        # check if current node is already explored or visited or not
        if current.val not in visited_set:

            # add current node to visited set
            visited_set.add(current.val)

            # check if current node is goal node or not
            if (current.val == goal.val):

                # make flag to True
                found = True

                # break the search
                break

                # if current not id not goal node
            else:
                # loop through all adjacent child nodes
                for i in current.adjecencies:
                    # find f value for child node F(n) = g(n) + h(n)
                    f = i.costVal + current.hval

                    # append f value in temp f value list
                    temp_f_val.append(f)

                # get index of min f value
                min_index = temp_f_val.index(min(temp_f_val))

                # append child node of current node having less f(n) val in queue to explore next
                queue.append(current.adjecencies[min_index].targetNode)

                # append child node of current node having less f(n) val in path
                path.append(current.adjecencies[min_index].targetNode.val)

            # delete current node from queue after exploring it
            del queue[0]

    # if while loop is stopped because queue is empty
    if (len(queue) == 0):
        print("No path exist")
    else:
        print(path)


# current node for 5 cites
# name of city and h val (estimated value)
n1 = Node("Mumbai", 7);
n2 = Node("Surat", 6);
n3 = Node("Bhopal", 2);
n4 = Node("Jaipur", 1);
n5 = Node("Delhi", 0);

# Mumbai
n1.add([Edge(n2, 100), Edge(n3, 400)])

# Surat
n2.add([Edge(n3, 200), Edge(n4, 500), Edge(n5, 1200)])

# Bhopal
n3.add([Edge(n4, 200)])

# Jaipur
n4.add([Edge(n5, 300)])

# Delhi
n5.add([])

# call A* function by passing start and goal node
AstarSearch(n1, n5);

