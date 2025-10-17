from tiles import TilesNode
from queue import PriorityQueue


def heuristic(node: TilesNode) -> int:
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    countHeu = 0
    for i in range(0,4):
        for k in range(0,4):
            if goal_state[i][k] != node.state[i][k]:
                countHeu = countHEU + 1
    return countHeu
    """
    Evaluate the heuristic value of the current node.
    This implementation simply counts the number of misplaced tiles.

    Returns
    -------
    heuristic_value : int
        The heuristic value of the current node.
    """
    raise NotImplementedError("Implement this function as part of the assignment.")


def AStar(root, heuristic: callable) -> TilesNode or None:  # type: ignore
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    # HINT: PriorityQueue.put() takes a tuple as input
    # To sort the queue items, it uses the first element of each tuple
    # If the first elements are equal, it uses the second element, and so on
    # You may implement a counter to resolve ties
    explored = set()
    g_score = {root: 0}
    f_score = {root: heuristic(root)}

    while not unexplored.empty():
        raise NotImplementedError(
            "Implement the rest of this function as part of the assignment."
        )

    return None  # return None if no path was found
