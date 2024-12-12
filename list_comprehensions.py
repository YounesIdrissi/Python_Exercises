# given x, y, z, n, print everything for i, j, k, who inclusively lie 
# between x, y, z and 0, (ex: 0 <= i <= x) and whose sum does not equal n 
# (i+j+k != n)

x = 1
y = 1
z = 2
n = 3

print([[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) 
       for k in range(0, z + 1) if i + j + k != n])
