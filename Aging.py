from typing import Dict, List, Optional


class Aging:
    def __init__(self,
                 num_page_frames: int = 4,
                 num_virtual_pages: int = 8,
                 num_counter_bits: int = 4
                 ) -> None:
        self._num_page_frames = num_page_frames
        self._num_virtual_pages = num_virtual_pages
        self._num_counter_bits = num_counter_bits
        self._counter: Dict[int, str] = {}
        self._page_frames: List[Optional[int]] = []

    def input_referenced_pages(self, referenced_pages: List[int]) -> None:
        count: int = 0
        for page in referenced_pages:
            if page not in self._counter.keys():
                count += 1

        if (count + len(self._counter)) > self._num_page_frames:
            self.del_frames((count + len(self._counter)) % self._num_page_frames, referenced_pages)

        for page in referenced_pages:
            try:
                self._counter[page] = "1" + self._counter[page][:-1]
            except KeyError:
                self._counter[page] = "1" + "0" * (self._num_counter_bits - 1)

        for page in self._counter.keys():
            if page not in referenced_pages:
                self._counter[page] = "0" + self._counter[page][:-1]

        print(f"{referenced_pages} \t-> {self._counter}")

    def binary_input(self) -> None:
        pass

    def del_frames(self, num_frames: int, referenced_pages: List[int]) -> None:
        if num_frames <= 0:
            return None
        for _ in range(num_frames):
            lower: float = float("inf")
            del_key: Optional[int] = None
            for key, value in self._counter.items():
                value = int(value, 2)
                if (key not in referenced_pages) and (value < lower):
                    lower = value
                    del_key = key

            del self._counter[del_key]

        return None


# a = Aging()
# a.input_referenced_pages([6, 7])
# a.input_referenced_pages([6, 7])
# a.input_referenced_pages([4, 6, 7])
# a.input_referenced_pages([1, 6])
# a.input_referenced_pages([1, 2, 6, 7])
# a.input_referenced_pages([2, 6, 7])
# a.input_referenced_pages([2, 3, 7])
# a.input_referenced_pages([2, 5, 7])
# a.input_referenced_pages([3, 7])
# a.input_referenced_pages([4, 7])

b = Aging()
b.input_referenced_pages([1])
b.input_referenced_pages([3])
b.input_referenced_pages([2])
b.input_referenced_pages([7])
b.input_referenced_pages([1, 2, 3])
b.input_referenced_pages([1, 3, 5])
b.input_referenced_pages([1, 2, 3])
b.input_referenced_pages([3, 6])
b.input_referenced_pages([1, 3, 7])
b.input_referenced_pages([4, 2, 7])
