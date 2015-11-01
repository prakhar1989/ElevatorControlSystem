Elevator System
===

### Design
The design of the project is split amongst two primary classes - an `Elevator` class that models each elevator and `ElevatorControlSystem` that models the system as a whole. A client interacts with the APIs exposed by the `ElevatorControlSystem` system which then dispatches requests correctly to the elevators.

The crux of the design is that the `ElevatorControlSystem` decides which elevator to choose in response to a `pickup` request and then calls `addRequest` on the elevator object. The elevator then serves each of the requests which it has been handed over the `ElevatorControlSystem`.

To decide on the elevator, the `ElevatorControlSystem` first identifies all the elevators that are going in the same direction as the request and the picks the closest one to the floor of pickup request. In case the `ElevatorControlSystem` is not able to find any elevator (e.g. all elevators are heading up from the 5th floor and a pickup request such as `pickup(2, 1, 4)` arrives), it adds the request to its FIFO queue which is served by the first elevator that gets free.

Once an elevator, is assigned a request, it adds the request to its priority queue. The min-heap is used to keep track of the next nearest destination. This ensures that the elevator stops at each required floor on just once, thereby making it more efficient than an elevator that works purely in a FIFO fashion. In this way, the elevator behaves like a real-world one in which stops are made all along the route (as long as they are in the same direction).

An important aspect of the design is the signature of the `pickup` method, which apart from floor and direction, also expects a destination. This has been done, primarily to simply the design. In the absence of a destination paramter, the elevator would be required to stop at the pickup floor and then explicity wait for information about the destination. Hence, clubbing both the floor pickup request and destination simplies the time simulation.
Another important point to note is that the `ElevatorControlSystem` **does not** use the destination to assign an elevator to a pickup request, hence behaving similar to a real-life implementation. The destination is only used to change the selected elevators request queue.

#### Interface
The interface has been kept identical to the specfication provided for all the methods except `pickup` that has been amended to add another parameter to indicate the destination of the pickup request.

```python
def status(): 
    # returns a list of 3-tuple status for each elevator

def update(id, floor, goal): 
    # updates the floor and goal of the elevator with id

def step(): 
    # advances the time by one unit in the simulation

def pickup(floor, direction, destination): 
    # adds a pick up request into the system and assigns a elevator to handle it
```

#### Assumptions
The key assumption that design relies on is that it users of the system get on and off the elevator instantaneously. This means that when an elevator reaches a destination, the next clock tick (or step) directly results in moving the elevator towards its next goal - this is only possible when the above assumption holds.

#### Shortcomings


### Tests
```
$ python -m tests.test_elevator
$ python -m tests.test_system
```
