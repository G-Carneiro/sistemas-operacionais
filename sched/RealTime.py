import copy
from typing import List, Dict, Tuple, Optional


class Task:
    def __init__(self,
                 name: str,
                 computation_time: float,
                 period: float
                 ) -> None:
        self.name: str = name
        self._computation_time: float = computation_time
        self._remaining_computation_time: float = computation_time
        self.period: float = period
        self.deadline: float = period
        self.deadline_misses: List[float] = []
        self.preemptions: List[float] = []

    def get_period(self) -> float:
        return self.period

    def get_remaining_computation_time(self) -> float:
        return self._remaining_computation_time

    def get_computation_time(self) -> float:
        return self._computation_time

    def att_remaining_computation_time(self, value: float) -> None:
        self._remaining_computation_time -= value
        if (not self._remaining_computation_time):
            self._remaining_computation_time = self._computation_time

        return None

    def __repr__(self) -> str:
        return self.name


class PeriodicTasks:
    def __init__(self, tasks: List[Task], actual_time: float = 0) -> None:
        self._tasks: List[Task] = tasks
        self._actual_time: float = actual_time
        # [(start, end), ...]
        self._scheduling_periods: Dict[Task, List[Tuple[float, float]]] = {task: [] for task in tasks}
        self._idle_periods: List[Tuple[float, float]] = []

    def rate_monotonic(self, final_time: float) -> list:
        priority_tasks: List[Task] = sorted(self._tasks, key=lambda x: x.period)
        next_occurrences: Dict[Task, float] = {task: 0 for task in self._tasks}
        time_line = []

        while (self._actual_time < final_time):
            for i in range(len(priority_tasks)):
                task: Task = priority_tasks[i]
                if (next_occurrences[task] <= self._actual_time):
                    actual_task = task
                    actual_task_id: int = i
                    break
            else:
                time_line += [self._actual_time, None]
                next_occurrence = min(next_occurrences.values())
                self._idle_periods.append((self._actual_time, next_occurrence))
                self._actual_time = next_occurrence
                continue

            execution_time: float = actual_task.get_remaining_computation_time()
            new_time: float = self._actual_time + execution_time
            time_line += [self._actual_time, actual_task]

            for i in range(actual_task_id):
                next_occurrence = next_occurrences[priority_tasks[i]]
                if (new_time > next_occurrence):
                    execution_time = next_occurrence - self._actual_time
                    new_time = next_occurrence

            for i in range(actual_task_id + 1, len(priority_tasks)):
                task = priority_tasks[i]
                next_occurrence = next_occurrences[task]
                if (new_time >= next_occurrence + task.deadline):
                    next_occurrences[task] += task.deadline
                    task.deadline_misses.append(next_occurrences[task])
                    task.att_remaining_computation_time(task.get_remaining_computation_time())

            actual_task.att_remaining_computation_time(execution_time)
            if (actual_task.get_remaining_computation_time() == actual_task.get_computation_time()):
                next_occurrences[actual_task] = min(self._actual_time, next_occurrences[actual_task]) \
                                                + actual_task.deadline
            else:
                actual_task.preemptions.append(new_time)

            self._scheduling_periods[actual_task].append((self._actual_time, new_time))
            self._actual_time = new_time

        return time_line

    def earliest_deadline_first(self) -> None:
        pass


a = Task("A", computation_time=20, period=100)
b = Task("B", computation_time=40, period=150)
c = Task("C", computation_time=100, period=350)
sched = PeriodicTasks([a, b, c])
print(sched.rate_monotonic(360))
