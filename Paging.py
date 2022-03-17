from typing import Union
from math import log2, ceil


class Paging:
    def __init__(self,
                 page_size: Union[int, str],
                 virtual_address: int,
                 physical_memory: Union[str, int]
                 ) -> None:
        if isinstance(page_size, str):
            aux = page_size.split()
            number: int = int(aux[0])
            magnitude: int = self._get_magnitude(aux[1])
            self._page_size: int = number * magnitude
        else:
            self._page_size: int = page_size

        self._virtual_address: int = virtual_address

        if isinstance(physical_memory, str):
            aux = physical_memory.split()
            number: int = int(aux[0])
            magnitude: int = self._get_magnitude(aux[1])
            self._physical_memory: int = number * magnitude
        else:
            self._physical_memory: int = page_size

        self._number_of_bits_in_page: int = ceil(log2(self._page_size))
        self._number_of_bits_in_memory: int = ceil(log2(self._physical_memory))

    @staticmethod
    def _get_magnitude(magnitude: str) -> int:
        magnitude = magnitude.upper()
        if (magnitude == "KB"):
            return 2**10
        elif (magnitude == "MB"):
            return 2**20
        elif (magnitude == "GB"):
            return 2**30

    def number_of_entry_in_pages_table(self) -> int:
        return 2**self.bits_for_addressing_pages_table()

    def bits_for_addressing_pages_table(self) -> int:
        return (self._virtual_address - self._number_of_bits_in_page)

    def bits_for_identify_page_frames(self) -> int:
        return ceil(log2(self._physical_memory / self._page_size))

    def bits_for_physical_address(self) -> int:
        return (self._number_of_bits_in_page + self.bits_for_identify_page_frames())

    def shift_bits_within_page(self) -> int:
        return self._number_of_bits_in_page

    def find_physical_address(self, virtual_address: int, number_of_page_frame: int) -> int:
        shift_bits = bin(virtual_address)[-self.shift_bits_within_page()::]
        physical_address = bin(number_of_page_frame) + shift_bits
        return int(physical_address, 2)

    def find_page_of_virtual_address(self, virtual_address: int) -> int:
        return (virtual_address // self._page_size)

    def show_results(self) -> None:
        print(f"Entradas na tabela de página: {self.number_of_entry_in_pages_table()} \n"
              f"Número de bits para endereçar a tabela de páginas: {self.bits_for_addressing_pages_table()} \n"
              f"Número de bits para molduras de página: {self.bits_for_identify_page_frames()} \n "
              f"Número de bits para endereço físico: {self.bits_for_physical_address()} \n "
              f"Número de bits para deslocamento dentro da página: {self.shift_bits_within_page()}")
        return None
