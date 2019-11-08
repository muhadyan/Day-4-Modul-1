'''
# SOAL 1
p = {1, 2, 4, 7, 9, 19}
q = {5, 6, 7, 9, 12, 16, 17, 19}
r = {3, 6, 8, 19}

# P n Q
print(p & q)

# P n Q n R
print(p & q & r)



# SOAL 2
s = {-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
p = {-4, -3, -2, -1, 0, 1, 2, 3, 4}
q = {-7, -6, -3, -2, -1, 0, 1}
r = {-1, 0, 1, 2, 3, 4, 5, 6, 7}

setP = (p|q)
setQ = (p|r)
setR = (q|r)

setP = list(setP)
setP.sort()
print(setP)

setQ = list(setQ)
setQ.sort()
print(setQ)

setR = list(setR)
setR.sort()
print(setR)



# SOAL 3
S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {2, 3, 5, 7}
B = {5, 7, 9}

# A
print(A)
# B
print(B)
# (A n B)
print(A & B)
# (A u B)
print(A | B)
# A n (A u B)
print(A & (A | B))
# B n (A u B)
print(B & (A | B))
# (A u B) n (A u B)
print((A | B) & (A | B))
# (A n B) u (A u B)
print((A & B) | (A | B))
'''