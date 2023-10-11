# TODO Найдите количество книг, которое можно разместить на дискете
count_of_symbols = 25 * 50 * 100
one_book = count_of_symbols * 4
mb = one_book / 1024 / 1024
print("Количество книг, помещающихся на дискету:", int(1.44 // mb))
