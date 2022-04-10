from typing import Dict, List, Optional


class NFU:
    def __init__(self,
                 num_page_frames: int = 4,
                 num_virtual_pages: int = 8,
                 num_counter_bits: int = 4
                 ) -> None:
        self._num_page_frames = num_page_frames
        self._num_virtual_pages = num_virtual_pages
        self._num_counter_bits = num_counter_bits
        self._counter: Dict[int, int] = {}
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
                self._counter[page] = (self._counter[page] + 1) % (2**self._num_counter_bits)
            except KeyError:
                self._counter[page] = 1

        print(self._counter)

    def binary_input(self) -> None:
        pass

    def del_frames(self, num_frames: int, referenced_pages: List[int]) -> None:
        if num_frames <= 0:
            return None
        for _ in range(num_frames):
            lower: float = float("inf")
            del_key: Optional[int] = None
            for key, value in self._counter.items():
                if (key not in referenced_pages) and (value < lower):
                    lower = value
                    del_key = key

            del self._counter[del_key]

        return None


# a = NFU()
# a.input_referenced_pages([6, 7])
# a.input_referenced_pages([6, 7])
# a.input_referenced_pages([4, 6, 7])
# a.input_referenced_pages([1, 4, 6])
# a.input_referenced_pages([2, 6, 7])
# a.input_referenced_pages([6, 7])
# a.input_referenced_pages([4, 7])
# a.input_referenced_pages([4, 5, 7])
# a.input_referenced_pages([0])
# a.input_referenced_pages([4, 7])

b = NFU()
b.input_referenced_pages([1])
b.input_referenced_pages([3])
b.input_referenced_pages([2])
b.input_referenced_pages([7])
b.input_referenced_pages([1, 2, 3])
b.input_referenced_pages([1, 3, 5])
b.input_referenced_pages([1, 2, 3])
b.input_referenced_pages([3, 6])
b.input_referenced_pages([1, 3, 7])
b.input_referenced_pages([2, 7])
