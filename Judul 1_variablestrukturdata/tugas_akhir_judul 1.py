class Node:
    def __init__(self, tiket):
        self.tiket = tiket
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_tiket(self, tiket):
        new_node = Node(tiket)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print(f"Tiket '{tiket}' ditambahkan.")

    def tampilkan_tiket(self):
        if self.head is None:
            print("Belum ada tiket.")
            return

        print("\nDaftar Tiket:")
        temp = self.head
        no = 1
        while temp:
            print(f"{no}. {temp.tiket}")
            temp = temp.next
            no += 1

    def proses_tiket(self):
        if self.head is None:
            print("Tidak ada tiket.")
        else:
            print(f"Tiket '{self.head.tiket}' sedang diproses.")
            self.head = self.head.next


def menu():
    print("\n=== Sistem Pemesanan Tiket Kapal ===")
    print("1. Tambah tiket")
    print("2. Tampilkan tiket")
    print("3. Proses tiket pertama")
    print("4. Keluar")


def main():
    daftar = LinkedList()

    while True:
        menu()
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilihan == 1:
            tiket = input("Masukkan detail tiket (misal: Tujuan, Tanggal): ")
            daftar.tambah_tiket(tiket)

        elif pilihan == 2:
            daftar.tampilkan_tiket()

        elif pilihan == 3:
            daftar.proses_tiket()

        elif pilihan == 4:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()