class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.size = 0
        self.processing_time_per_ticket = 2 

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, nama, tujuan):
        ticket = {'nama': nama, 'tujuan': tujuan}
        new_node = Node(ticket)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        self.size += 1
        print(f"Tiket untuk {nama} tujuan {tujuan} berhasil ditambahkan ke antrean.")
        if self.size >= 5:
            print("PERINGATAN: Antrean tiket sangat padat, mohon percepat pelayanan!")

    def dequeue(self):
        if self.is_empty():
            print("Antrean tiket kosong")
            return
        temp = self.front_ptr
        ticket_data = temp.data
        print(f"Tiket untuk {ticket_data['nama']} tujuan {ticket_data['tujuan']} berhasil dikeluarkan dari antrean.")
        self.front_ptr = self.front_ptr.next
        self.size -= 1
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean tiket kosong")
            return
        ticket_data = self.front_ptr.data
        print(f"Tiket terdepan: {ticket_data['nama']} dengan tujuan {ticket_data['tujuan']}")

    def display(self):
        if self.is_empty():
            print("Antrean tiket kosong")
            print("Status antrean: Lancar")
            return
        print("Isi antrean tiket (depan ke belakang):")
        current = self.front_ptr
        idx = 1
        while current is not None:
            ticket_data = current.data
            print(f"  {idx}. Nama: {ticket_data['nama']}, Tujuan: {ticket_data['tujuan']}")
            current = current.next
            idx += 1
        
        if self.size >= 5:
            print("Status antrean: Padat")
        else:
            print("Status antrean: Lancar")

    def calculate_wait_time(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada waktu tunggu.")
            return
        estimated_time = self.size * self.processing_time_per_ticket
        print(f"Estimasi waktu tunggu saat ini: {estimated_time} menit untuk {self.size} tiket.")


def main():
    queue = QueueLinkedList()
    pilih = 0
    while pilih != 6: 
        print("\n=== ANTRIAN TIKET KERETA API (Linked List) ===")
        print("1. Tambah Tiket (Enqueue)")
        print("2. Keluarkan Tiket (Dequeue)")
        print("3. Lihat Tiket Terdepan (Peek)")
        print("4. Tampilkan Antrean")
        print("5. Hitung Estimasi Waktu Tunggu") 
        print("6. Keluar") 
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka antara 1-6.")
            continue
        if pilih == 1:
            try:
                nama = input("Masukkan nama penumpang: ")
                tujuan = input("Masukkan tujuan kereta: ")
                if not nama or not tujuan:
                    print("Nama penumpang dan tujuan tidak boleh kosong!")
                else:
                    queue.enqueue(nama, tujuan)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            queue.calculate_wait_time() 
        elif pilih == 6:
            while not queue.is_empty():
                queue.dequeue() 
            print("Program antrean tiket selesai. Sampai jumpa!")
        else:
            print("Pilihan tidak valid! Masukkan angka antara 1-6.")


if __name__ == "__main__":
    main()