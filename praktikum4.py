#Program Menentukan Nilai Terbesar

#Input Bilangan 1,2,3

num1 = int(input('Masukan Bilangan ke-1='))
num2 = int(input('Masukan Bilangan ke-2='))
num3 = int(input('Masukan Bilangan ke-3='))

#Proses dan Output

if num1 > num2 and num1 > num3:
    print("bilangan terbesar adalah =", num1)
elif num2 > num1 and num2 > num3:
    print("bilangan terbesar adalah =", num2)
else :
    print("bilangan terbesar adalah =", num3)
