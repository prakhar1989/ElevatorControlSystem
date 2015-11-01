from heapq import heappush, heappop

"""
The Elevator class is used to model the elevator.  At any point
in time, four instance variables - floor, goal, direction and
requestQueue represent its state. The requestQueue is a priority
queue that is a min-heap over the target stopping points.
"""

class Elevator:
    def __init__(self, id):
        self.id = id
        self.goal = 0
        self.floor = 0
        self.requestQueue = [] # a priority queue
        self.direction = 1

    def __repr__(self):
        return "Elevator #{0}. Going from {1} to {2}".format(self.id, self.floor, self.goal)

    def step(self):
        """ moves the simluation one time unit ahead for the elevator.
        This method updates the current floor and the goal (if required) """
        if not self.requestQueue:
            return
        self.floor += self.direction
        if self.floor == self.goal:
            heappop(self.requestQueue)
            if self.requestQueue: # more requests to go
                self.goal = self.direction * self.requestQueue[0]

    def getStatus(self):
        return (self.id, self.floor, self.goal)

    def update(self, floor, goal):
        """  clears the state of the elevator """
        self.floor = floor
        self.goal = goal
        self.direction = 1 if self.floor < self.goal else -1
        self.requestQueue = []
        self.addRequest(floor, goal)

    def getPendingRequestCount(self):
        return len(self.requestQueue)

    def addRequest(self, floor, goal):
        """ adds a new request to the elevator's request queue """
        # the first request in the elevator sets the direction
        if self.getPendingRequestCount() == 0:
            self.direction = 1 if floor < goal else -1
            self.goal = goal * self.direction

        # update the queue with the goal request
        newGoal = self.direction * goal
        if newGoal not in self.requestQueue:
            heappush(self.requestQueue, newGoal)

        # update the queue with the floor request
        newFloor = self.direction * floor
        if self.floor != floor and newFloor not in self.requestQueue:
            heappush(self.requestQueue, newFloor)

        # update the goal and if a smaller one exists
        if self.requestQueue[0] < self.direction * self.goal:
            self.goal = self.direction * self.requestQueue[0]
