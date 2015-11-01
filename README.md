Elevator System
===

### Design
The design of the project is split amongst two primary classes - an `Elevator` class that models each elevator and `ElevatorControlSystem` that models the system as a whole. A client interacts with the APIs exposed by the `ElevatorControlSystem` system which then dispatches requests correctly to the elevators.

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


#### Shortcomings


### Tests
```
$ python -m tests.test_elevator
$ python -m tests.test_system
```
