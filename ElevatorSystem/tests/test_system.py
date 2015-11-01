import unittest
from system import ElevatorControlSystem

class test_elevator(unittest.TestCase):

    def setUp(self):
        self.ECS = ElevatorControlSystem(floors=20, elevator_count=5)
        ## giving initial state to all elevators
        self.ECS.update(0, 4, 10)
        self.ECS.update(1, 3, 0)
        self.ECS.update(2, 8, 4)
        self.ECS.update(3, 6, 2)
        self.ECS.update(4, 7, 10)

    def test_status_and_update(self):
        expectedStatus = [(0, 4, 10), (1, 3, 0), (2, 8, 4), (3, 6, 2), (4, 7, 10)]
        self.assertEqual(self.ECS.status(), expectedStatus)

    def test_pickup(self):
        # should be assigned to the 1st elevator
        # since it is closest to it and in the same direction
        self.ECS.pickup(5, 1, 11)
        self.assertEqual(self.ECS.status()[0], (0, 4, 5))

        # should be assigned to the 3rd elevator
        self.ECS.pickup(7, -1, 0)
        self.assertEqual(self.ECS.status()[2], (2, 8, 7))

        # shoudl be assigned to the 2nd elevator
        self.ECS.pickup(2, -1, 0)
        self.assertEqual(self.ECS.status()[1], (1, 3, 2))

        # should be assigned to the 5th elevator
        self.ECS.pickup(9, 1, 11)
        self.assertEqual(self.ECS.status()[4], (4, 7, 9))

        # should be assigned to the 4th elevator
        self.ECS.pickup(5, -1, 4)
        self.assertEqual(self.ECS.status()[3], (3, 6, 5))


    def test_step(self):
        expectedStatus = [(0, 4+1, 10), (1, 3-1, 0), (2, 8-1, 4),
                          (3, 6-1, 2), (4, 7+1, 10)]
        self.ECS.step()
        self.assertEqual(expectedStatus, self.ECS.status())

    """ testing the scenario where a request gets added to the
    pending queue and is then assigned when the elevator fulfills
    its current request"""
    def test_to_be_assigned_feature(self):
        ecs = ElevatorControlSystem(floors=20, elevator_count=1)
        ecs.update(0, 3, 0)
        ecs.pickup(2, 1, 10)
        for i in range(3):
            self.assertEqual(len(ecs.toBeAssigned), 1)
            ecs.step()
        # when the elevator gets done with the request
        # the queue should get empty
        self.assertEqual(len(ecs.toBeAssigned), 0)

        # and its goal should change accordingly
        self.assertEqual(ecs.elevators[0].goal, 2)

        # after two moves, the goal should correct change to 10
        ecs.step()
        ecs.step()
        self.assertEqual(ecs.elevators[0].goal, 10)


if __name__ == "__main__":
    unittest.main()
