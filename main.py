#Breadth-first Search 

class queue:
    def __init__(self):
     self.queue = []

    def enqueue(self,x):
        self.queue.append(x)

        def dequeue(self):
            return self._queue.pop(0)

            def isEmpty(self):
                return len(self._queue) == 0

def retrievePath(nodelist, start, goal):
    #Return the path from start to goal
    if start == goal:
        path = []
        path.append(start)
        return path 
    else:
        previous = nodelist[goal].discovered()
        previous_path = retrievePath(nodelist, start, previous)
        previous_path.append(goal)
        return previous_path

def BFS(nodelist, start, goal):
    to_visit = queue()
    nodelist[start].setSeen()
    to_visit.enqueue(start)
    
    found = False 
    while (not found) and (not to_visit.isEmpty()):
        current = to_visit.dequeue()
        neighbors = nodelist[current].getNeighbors()

    for neighbor in neighbors:
        if nodelist[neighbor].isUnseen():
            nodelist[neighbor].setSeen()
            nodelist[neighbor].discover(current)
            if neighbor == goal:
                found = True
            else:
                to_visit.enqueue(neighbor)
    return retrievePath(nodelist, start, goal)

