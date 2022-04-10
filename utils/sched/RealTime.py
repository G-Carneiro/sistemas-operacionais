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
        self.absolute_deadline: float = period
        self.next_occurrence: float = 0
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
        self._time_line = []

    def rate_monotonic(self, final_time: float) -> None:
        priority_tasks: List[Task] = sorted(self._tasks, key=lambda x: x.period)

        while (self._actual_time < final_time):
            self._scheduling(priority_tasks)

        return None

    def earliest_deadline_first(self, final_time: float) -> None:
        while (self._actual_time < final_time):
            priority_tasks: List[Task] = sorted(self._tasks, key=lambda x: x.absolute_deadline)
            self._scheduling(priority_tasks)

        return None

    def _scheduling(self, priority_tasks: List[Task]) -> None:
        for i in range(len(priority_tasks)):
            task: Task = priority_tasks[i]
            if (task.next_occurrence <= self._actual_time):
                actual_task = task
                actual_task_id: int = i
                break
        else:
            self._time_line += [self._actual_time, None]
            next_occurrence = min([task.next_occurrence for task in self._tasks])
            self._idle_periods.append((self._actual_time, next_occurrence))
            self._actual_time = next_occurrence
            return None

        execution_time: float = actual_task.get_remaining_computation_time()
        new_time: float = self._actual_time + execution_time
        self._time_line += [self._actual_time, actual_task]

        for i in range(actual_task_id):
            next_occurrence = priority_tasks[i].next_occurrence
            if (new_time > next_occurrence):
                execution_time = next_occurrence - self._actual_time
                new_time = next_occurrence

        for i in range(actual_task_id + 1, len(priority_tasks)):
            task = priority_tasks[i]
            next_occurrence = task.next_occurrence
            if (new_time >= next_occurrence + task.deadline):
                task.next_occurrence += task.deadline
                task.deadline_misses.append(task.next_occurrence)
                task.att_remaining_computation_time(task.get_remaining_computation_time())

        actual_task.att_remaining_computation_time(execution_time)
        if (actual_task.get_remaining_computation_time() == actual_task.get_computation_time()):
            actual_task.next_occurrence = min(self._actual_time, actual_task.next_occurrence) \
                                          + actual_task.deadline
            actual_task.absolute_deadline += actual_task.deadline
        else:
            actual_task.preemptions.append(new_time)

        self._scheduling_periods[actual_task].append((self._actual_time, new_time))
        self._actual_time = new_time

        return None

    def show_results(self) -> None:
        deadline_misses: int = 0
        for task in self._tasks:
            deadline_misses += len(task.deadline_misses)
            print(f"A tarefa {task.name} é \n"
                  f"- Escalonada {len(self._scheduling_periods[task])} vezes em {self._scheduling_periods[task]} \n"
                  f"- Preemptada {len(task.preemptions)} vezes em {task.preemptions} \n"
                  f"- Tem {len(task.deadline_misses)} perdas de deadline em {task.deadline_misses}\n")

        print(f"Total de perdas de deadline: {deadline_misses} \n"
              f"Períodos ociosos: {self._idle_periods} \n"
              f"Timeline: \n"
              f"{self._time_line}")

        return None


a = Task("A", computation_time=5, period=10)
b = Task("B", computation_time=2, period=4)
c = Task("C", computation_time=100, period=350)
sched = PeriodicTasks([a, b])
sched.rate_monotonic(30)
sched.show_results()
