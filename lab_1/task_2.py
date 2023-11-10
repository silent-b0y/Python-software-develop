# TODO Найдите количество книг, которое можно разместить на дискете
ONE_CHAR_BYTES = 4

count_of_pages = 100
count_of_strings = 50
count_of_chars = 25

count_of_symbols = count_of_chars * count_of_strings * count_of_pages
one_book_size_bytes = count_of_symbols * ONE_CHAR_BYTES
one_book_size_mbytes = one_book_size_bytes / 1024 / 1024
print("Количество книг, помещающихся на дискету:", int(1.44 // one_book_size_mbytes))
