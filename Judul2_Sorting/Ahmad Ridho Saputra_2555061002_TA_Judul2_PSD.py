def insertion_sort(students):
    n = len(students)
    for i in range(1, n):
        temp_student = students[i]
        j = i - 1
        while j >= 0 and students[j]['npm'] > temp_student['npm']:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = temp_student


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    students = []
    print("\nMasukkan data mahasiswa (Nama dan NPM):")
    for i in range(n):
        print(f"\nMahasiswa ke-{i+1}:")
        name = input("Nama: ")
        while True:
            try:
                npm = int(input("NPM: "))
                students.append({'nama': name, 'npm': npm})
                break
            except ValueError:
                print("Input NPM tidak valid, silakan masukkan angka!")

    print(f"\nData Mahasiswa yang diinput: {students}")

    insertion_sort(students)

    print("\nUrutan Mahasiswa berdasarkan NPM (Insertion Sort):")
    for student in students:
        print(f"Nama: {student['nama']}, NPM: {student['npm']}")


if __name__ == "__main__":
    main()