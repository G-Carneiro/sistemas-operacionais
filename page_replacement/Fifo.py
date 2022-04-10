from typing import Dict, List, Optional


class Fifo:
    def __init__(self,
                 num_page_frames: int = 4,
                 num_virtual_pages: int = 8,
                 num_counter_bits: int = 4
                 ) -> None:
        self._num_page_frames = num_page_frames
        self._num_virtual_pages = num_virtual_pages
        self._num_counter_bits = num_counter_bits
        self._counter: List[int] = []
        self._page_frames: List[Optional[int]] = []

    def input_referenced_pages(self, referenced_pages: List[int]) -> None:
        for page in referenced_pages:
            if page not in self._counter:
                self._counter.append(page)
                if (len(self._counter) > self._num_page_frames):
                    self._counter.pop(0)

            print(page, self._counter)

        return None


f = Fifo()
f.input_referenced_pages([0, 1, 7, 2, 3, 2, 7, 6, 5, 7, 2])
