from typing import List, Dict


class Disk:
    def __init__(self,
                 displacement_time: float,
                 start_cylinder: int
                 ) -> None:
        self._displacement_time: float = displacement_time
        self._actual_cylinder: int = start_cylinder

    def fcfs(self, required_cylinders: List[int]) -> float:
        total_displacement: int = 0
        for cylinder in required_cylinders:
            total_displacement += abs(self._actual_cylinder - cylinder)
            self._actual_cylinder = cylinder

        return (total_displacement * self._displacement_time)

    def elevator(self, required_cylinders: List[int], ascending: bool = True) -> float:
        total_displacement: int = 0
        biggest_cylinder: int = max(required_cylinders)
        smallest_cylinder: int = min(required_cylinders)
        if ascending:
            total_displacement += biggest_cylinder - self._actual_cylinder
            self._actual_cylinder = smallest_cylinder
        else:
            total_displacement += self._actual_cylinder - smallest_cylinder
            self._actual_cylinder = biggest_cylinder

        total_displacement += biggest_cylinder - smallest_cylinder

        # required_cylinders.sort()
        # for i in range(len(required_cylinders)):
        #     if (required_cylinders[i] >= self._actual_cylinder):
        #         greater_cylinders: List[int] = required_cylinders[i:]
        #         less_cylinders: List[int] = sorted(required_cylinders[:i], reverse=True)
        #         if ascending:
        #             required_cylinders = greater_cylinders + less_cylinders
        #         else:
        #             required_cylinders = less_cylinders + greater_cylinders
        #         break
        #
        # for cylinder in required_cylinders:
        #     total_displacement += abs(self._actual_cylinder - cylinder)
        #     self._actual_cylinder = cylinder

        return (total_displacement * self._displacement_time)

    def ssf(self, required_cylinders: List[int]) -> float:
        total_displacement: int = 0
        while required_cylinders:
            # key = distance, value = cylinder
            distance_between_cylinders: Dict[int, int] = {abs(self._actual_cylinder - cylinder): cylinder
                                                          for cylinder in required_cylinders}
            shortest: int = min(distance_between_cylinders.keys())
            cylinder = distance_between_cylinders[shortest]
            required_cylinders.remove(cylinder)
            total_displacement += shortest
            self._actual_cylinder = cylinder

        return (total_displacement * self._displacement_time)


a = Disk(displacement_time=40, start_cylinder=20)
print(a.fcfs([10, 22, 20, 2, 40, 6, 38]))

b = Disk(displacement_time=31, start_cylinder=20)
print(b.elevator([10, 22, 20, 2, 40, 6, 38]))

c = Disk(displacement_time=25, start_cylinder=20)
print(c.ssf([10, 22, 20, 2, 40, 6, 38]))

