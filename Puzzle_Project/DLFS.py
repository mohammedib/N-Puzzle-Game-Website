
from queue import LifoQueue as Stack
from .Node import Node
from .Search import Search
import time
class DLFS(Search):

    pathCost = 0            ##
    numProcessedNodes = 0   ##
    maxStoredNodes = 0      ##
    timeTaken = 0           ##
    searchCanceled = False

    def __init__(self , max_stored=0):
        self.max_stored = max_stored


    def DLFS(self,initial_state , Depth ):   
        start_node = Node(initial_state, None, None,0)
        start = time.time()         ##
        if start_node.goal_test().all():
            return start_node.find_solution()
            
        frontier = Stack() ## List Stack
        frontier.put(start_node)
        explored = set()
        print("\nInitial State ---------- Depth: {0}".format(start_node.depth))
        while not (frontier.empty()):
            if DLFS.searchCanceled :
                print("canceled!")
                return
            self.max_stored = max(self.max_stored ,frontier.qsize()+len(explored))
            node = frontier.get()

            if node.goal_test().all():
                print("***************GOAL STATE FOUND*******************")
                print("\n")
                print(node.display())
                DLFS.pathCost=node.depth                   ##
                DLFS.maxStoredNodes=self.max_stored        ##
                DLFS.numProcessedNodes=node.num_processed  ##
                DLFS.timeTaken = time.time() - start       ##
                return node.find_solution()
            if ( node.depth < Depth and tuple(node.state) not in explored):
                explored.add(tuple(node.state))
                children = node.generate_child()
                for child in children:
                    if DLFS.searchCanceled :
                        print("canceled!")
                        return
                    if tuple(child.state) not in explored:
                            frontier.put(child)

        return None