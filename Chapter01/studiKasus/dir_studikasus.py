gaji = int(input('Masukan Gaji Karyawan Anda: '))

if gaji > 1000000:
    print("Selamat Menikmati Uang hasil Kerja Anda")
elif gaji == 0:
    print("Kasian Kena PHK")
else:
    print("UMR BANGET")


###########
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]

sum = int(input('Masukan Angka Bebas: '))
# sum = 0
for val in numbers:
	sum = sum+val

print("The sum is", sum)

if sum > 0:
    print("Positive number")
elif sum == 0:
    print("Zero")
else:
    print("Negative number")