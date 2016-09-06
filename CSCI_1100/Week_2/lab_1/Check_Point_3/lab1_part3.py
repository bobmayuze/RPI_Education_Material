base10size = 128
base2size = int(base10size * 10 ** 9 / 2 ** 30)
lost_size = base10size - base2size

print (base10size, "GB in base 10 is actually", base2size, "GB in base 2,", lost_size, "GB less than advertised.")

