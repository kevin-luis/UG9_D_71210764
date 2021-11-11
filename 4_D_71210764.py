# Perhitungan Deret Geometri

print("Deret Geometri : 1, 3, 9, 27, 81, ...")
print("=====")
# Variabel Input
a = 1
r = 3
n = 11

# Proses
Sn = a * (r**n - 1) / (r - 1)

# Print
print(f"Jumlah suku ke - {n} adalah {Sn}")

