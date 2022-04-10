from typing import Dict, List, Optional


class LRU:
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
        for page in referenced_pages:
            if (page not in self._counter.keys()) and (len(self._counter) >= self._num_page_frames):
                lru: int = max(self._counter.values())
                for key, value in self._counter.items():
                    if (value == lru):
                        del self._counter[key]
                        break

            self._counter[page] = 0

            for pag in self._counter.keys():
                if pag != page:
                    self._counter[pag] += 1

            print(page, self._counter)

        return None


l = LRU()
l.input_referenced_pages([0, 1, 7, 2, 3, 2, 7, 6, 5, 7, 2])
