# Soal NIM ganjil nomor 2
# Konversi suhu dari fahrenheit menjadi celcius
# rumus fahrenheit menjadi celcius adalah 5/9*(f-32)

print("Conversi suhu fahrenheit ke celcius")
fahrenheit = int(input("Masukkan Suhu fahrenheit :"))
r1 = 5/9
r2 = 32

rumus2 = fahrenheit-r2 #hasil dari suhu fahrenheit-32 atau r2
rumusfahrenheitcelcius = r1*rumus2 #hasil dari 5/9*rumus2

print("Maka suhu celciusnya adalah", rumusfahrenheitcelcius,"*c")