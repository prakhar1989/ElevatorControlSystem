from elevator import Elevator
from collections import deque

"""
The ElevatorControlSystem class is used to model the control system.
This class exposes the public methods (API) for interaction with the user.
"""

class ElevatorControlSystem:
    def __init__(self, floors=100, elevator_count=16):
        """ constructor that initializes state of the system. A queue
        is used to maintain a list of requests that were not assigned
        to an elevator. A list of references to the child elevators is
        also maintianed.
        """
        self.floors = floors
        self.elevator_count = elevator_count
        self.elevators = [Elevator(i) for i in range(self.elevator_count)]
        self.toBeAssigned = deque()

    def status(self):
        return [e.getStatus() for e in self.elevators]

    def step(self):
        """ steps the simulation one time unit for the all the elevators
        Additionally, assigns pending requests to the closest elevator that
        is free.
        """
        for e in self.elevators:
            e.step()

        if self.toBeAssigned: # if there are pending
            floor, destination = self.toBeAssigned[0]
            # start search for closest free elevator
            availableElevators = []
            for e in self.elevators:
                if e.getPendingRequestCount() == 0:
                    diff = abs(e.floor - floor)
                    availableElevators.append((diff, e))
            if availableElevators:
                _, e = min(availableElevators)
                self.toBeAssigned.popleft()
                e.addRequest(floor, destination)

    def update(self, id, floor, goal):
        """ clears the state of the elevator with id - id and updates its
        state with new values """
        e = self.elevators[id]
        e.update(floor, goal)

    def pickup(self, floor, direction, destination):
        """ handles a pickup request from the client. works by searching
        for an elevator that is going in the same direction and then finding
        the closest one amongst them. In case, no elevators are found, the request
        is added to a FIFO queue to be handed later by a free elevator."""
        elevators = [e for e in self.elevators if e.direction == direction]
        candidates = []
        for e in elevators:
            diff = direction * (floor - e.floor)
            if diff >= 0:
                candidates.append((diff, e.id))
        if candidates:
            _, id = min(candidates)
            e = self.elevators[id]
            e.addRequest(floor, destination)
        else:
            # no elevators available to serve, so add this is a FIFO queue
            self.toBeAssigned.append((floor, destination))
