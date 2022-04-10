from utils.Paging import Paging


a = Paging("4 KB", 24, "2 GB")
print(a.number_of_entry_in_pages_table())

b = Paging("16 KB", 24, "512 MB")
print(b.bits_for_addressing_pages_table())

c = Paging("4 KB", 64, "2048 KB")
print(c.bits_for_identify_page_frames())

d = Paging("4 KB", 32, "8192 KB")
print(d.bits_for_physical_address())

e = Paging("1 KB", 20, "256 KB")
print(e.shift_bits_within_page())

f = Paging("8 KB", 32, "2 GB")
print(f.find_page_of_virtual_address(39543))
print(f.find_physical_address(39543, 2))

