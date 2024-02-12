# Menginput nilai tugas, uts, dan uas
tugas = float(input("Masukan Nilai Tugas: "))
uts = float(input("Masukan Nilai Uts: "))
uas = float(input("Masukan Nilai Uas: "))

# Menginput Nilai akhir seusai dengan bobot
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

# Menentukan Grade berdasarkan nilai akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'


# Menentukan status kelulusan berdasarkan nilai akhir
if nilai > 60:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

# Membuat bingkai untuk tampilan yang lebih menarik
print("=" * 40)
print("           Program Penentuan Nilai")
print("=" * 40)

#Menampilkan nilai akhir, grade, dan status kelulusan
print(f'Nilai Akhir: {nilai:.2f}')
print(f'Grade: {grade}')
print(f'Status: {status}')

#garis pemisah untuk tampilan yang lebih rapih
print("=" * 40)