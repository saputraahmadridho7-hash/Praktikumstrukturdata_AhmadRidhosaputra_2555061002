class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None

            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nNama Pasien:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()
    hashmap.insert(111, "Data Pasien Abam Ditemukan")
    hashmap.insert(222, "Data Pasien Luthfi Ditemukan")
    hashmap.insert(333, "Data Pasien Rizki Ditemukan")
    hashmap.insert(444, "Data Pasien Ridho Ditemukan")
    hashmap.display()

    pilih = 0
    while pilih != 2:
        print("\n=== Menu Pasien ===")
        print("1. Cek status Pasien")
        print("2. Keluar")
        try:
            pilih = int(input("Masukkan pilihan Anda: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
           print("Masukkan Kode pasien : ")
           try:
               pasien_key = int(input("Key: "))
               result_entry = hashmap.search(pasien_key)
               if result_entry:
                   print(f"Data ditemukan: Key {result_entry.key}, Value {result_entry.value}")
               else:
                   print("Data pasien tidak ditemukan!")
           except ValueError:
               print("Input kode tidak valid! Mohon masukkan angka.")
        elif pilih == 2:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()