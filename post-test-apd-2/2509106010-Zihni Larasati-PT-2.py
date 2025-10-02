nama = input("Masukkan nama pasien: ")
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))

beratIdeal = tinggi - 100
isKelebihan = berat > beratIdeal

statusList = ["Normal", "Kelebihan Berat Badan"]
status = statusList[int(isKelebihan)]

print("-" * 60)
print(f"| {'HASIL CEK BERAT BADAN':^56} |")
print("-" * 60)
print(f"| Nama Pasien\t: {nama:<40} |")
print(f"| Tinggi Badan\t: {tinggi:<6.1f} cm{'':<31} |")
print(f"| Berat Badan\t: {berat:<6.1f} kg{'':<31} |")
print(f"| Berat Ideal\t: {beratIdeal:<6.1f} kg{'':<31} |")
print(f"| Status\t: {status:<40} |")
print("-" * 60)
