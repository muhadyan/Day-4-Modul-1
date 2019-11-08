x = [1, 2, 3]   # ini list
y = (1, 2, 3)   # ini tuple
z = {1, 2, 3}   # ini set / himpunan


x = [
    (1, 2, 3),
    (4, 5, 6)
]

print(x[1][1])
x[0] = 'Andi'       # bisa diubah
print(x)
[0][0] = 'Andi'    # gabisa diubah
print(x)

x = [
    (1, ['a', 'b', 'c'], 3),
    (4, 5, 6)
]

# list yg didalem tuple tetep bisa diubah elemennya
x[0][1][2] = 'Andi'
print(x)



z = {1, 2, 3, 1, 2, 3}
print(z[0])             # no indexing (akan error)
print(z)                # duplicate elements not allowed
print(set(x))           # cara ubah list atau tuple menjadi set
print(list(set(x)))     # list yg tadi diubah jadi set, sekarang diubah jadi list lagi(berguna buat ngebuang elemen list yg duplikat)


# cara menambahkan elemen set
z.add('a')
print(z)
z.add(('c', 'd', 'e'))
print(z)
z.add([9, 8, 7])
print(z)                # set itu mutable, tp elemen2nya immutable, jadi gabisa nambahin sebuah list buat jadi elemennya set


z = {1, 2, 3, 1, 2, 3}
# cara lain nambahin elemen set
z.update('Andi')
z.update([6, 7, 8])
z.update({'z', 'budi'})

print('budi' in z)      # buat ngecek suatu elemen ada di sebuah set apa engga
# cara ngehapus elemen atau set
z.remove('budi')
z.discard('deni')       # Bedanya kalo '.discard' itu kalo yg mau dihapus elemennya ga ada, dia ga akan terbaca error
z.pop()                 # elemen yg kehapus itu random
z.clear()               # semua elemen keapus, tapi set nya masih ada
del z                   # ngehapus bukan cuma elemennya, tapi juga set nya



# HIMPUNAN
a = list('abcde')
b = list('bcfgh')

# ubah dulu list menjadi set
a = set(a)
b = set(b)

# MENCARI IRISAN
print(a.intersection(b))
# atau
print(b.intersection(a))
# bisa juga begini
print(a & b)
# atau
print(b & a)


# MENCARI GABUNGAN
print(a.union(b))
# atau
print(b.union(a))
# bisa juga begini
print(a | b)
# atau
print(b | a)


# MENCARI SELISIH
print(a.difference(b))      # elemen a yg ga ada di b
# dan
print(b.difference(a))      # elemen b yg ga ada di a
# bisa juga begini
print(a - b)
# dan
print(b - a)


# MENCARI SELAIN IRISAN
print(a.symmetric_difference(b))
# atau
print(b.symmetric_difference(a))
# bisa juga begini
print(a ^ b)
# atau
print(b ^ a)




# FROZENSET = SET IMMUTEABLE
x = set({1, 2, 3})
y = frozenset([1, 2, 3])