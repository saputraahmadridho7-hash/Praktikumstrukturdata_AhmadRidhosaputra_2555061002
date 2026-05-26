class Book:
    def __init__(self, isbn, title, author, book_type):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.book_type = book_type # berupa buku fisik atau digital

    def __str__(self):
        return f"ISBN: {self.isbn}, Judul: {self.title}, Penulis: {self.author}, Tipe: {self.book_type}"


class Node:
    def __init__(self, book):
        self.book = book 
        self.left = None
        self.right = None


class LibraryBST:
    def __init__(self):
        self.root = None

    def _insert_book_node(self, root, book):
        if root is None:
            return Node(book)
        
        if book.isbn < root.book.isbn:
            root.left = self._insert_book_node(root.left, book)
        elif book.isbn > root.book.isbn:
            root.right = self._insert_book_node(root.right, book)
        return root

    def add_book(self, book):
        self.root = self._insert_book_node(self.root, book)

    def _find_min_node(self, node):
        current = node
        while current is not None and current.left is not None:
            current = current.left
        return current

    def _delete_book_node(self, root, isbn):
        if root is None:
            return None

        if isbn < root.book.isbn:
            root.left = self._delete_book_node(root.left, isbn)
        elif isbn > root.book.isbn:
            root.right = self._delete_book_node(root.right, isbn)
        else: 
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self._find_min_node(root.right)
                root.book = successor.book 
                root.right = self._delete_book_node(root.right, successor.book.isbn)
        return root

    def remove_book(self, isbn):
        self.root = self._delete_book_node(self.root, isbn)

    def search_book(self, isbn):
        current = self.root
        while current is not None:
            if isbn == current.book.isbn:
                return current.book 
            elif isbn < current.book.isbn:
                current = current.left
            else:
                current = current.right
        return None 

    def get_height(self, root):
        if root is None:
            return -1
        height_left = self.get_height(root.left)
        height_right = self.get_height(root.right)
        return 1 + max(height_left, height_right)

    def list_all_books_level_order(self):
        if self.root is None:
            print("(Perpustakaan kosong)")
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.book) 
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def _find_successor_isbn(self, root, isbn):
        current = root
        successor_book = None
        while current is not None:
            if isbn < current.book.isbn:
                successor_book = current.book
                current = current.left
            else:
                current = current.right
        return successor_book

    def find_successor_book(self, target_isbn):
        book_found = self.search_book(target_isbn)
        if book_found is None: 
            return self._find_successor_isbn(self.root, target_isbn)
        
      
        current = self.root
        successor_node = None
        while current is not None:
            if target_isbn < current.book.isbn:
                successor_node = current
                current = current.left
            elif target_isbn > current.book.isbn:
                current = current.right
            else:
                if current.right is not None:
                    return self._find_min_node(current.right).book
                break 
        
        return successor_node.book if successor_node else None


    def _find_predecessor_isbn(self, root, isbn):
        current = root
        predecessor_book = None
        while current is not None:
            if isbn > current.book.isbn:
                predecessor_book = current.book
                current = current.right
            else:
                current = current.left
        return predecessor_book

    def find_predecessor_book(self, target_isbn):
        book_found = self.search_book(target_isbn)
        if book_found is None: 
            return self._find_predecessor_isbn(self.root, target_isbn)

        current = self.root
        predecessor_node = None
        while current is not None:
            if target_isbn > current.book.isbn:
                predecessor_node = current
                current = current.right
            elif target_isbn < current.book.isbn:
                current = current.left
            else: 
                if current.left is not None:
                    temp = current.left
                    while temp.right is not None:
                        temp = temp.right
                    return temp.book
                break 
        
        return predecessor_node.book if predecessor_node else None



def main():
    library = LibraryBST()
    pilih = 0
    while pilih != 8:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Cari Buku (berdasarkan ISBN)")
        print("4. Daftar Semua Buku (Level-order)")
        print("5. Tinggi Pohon")
        print("6. Cari Successor (berdasarkan ISBN)")
        print("7. Cari Predecessor (berdasarkan ISBN)")
        print("8. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue

        if pilih == 1:
            try:
                isbn = input("Masukkan ISBN buku: ")
                title = input("Masukkan Judul buku: ")
                author = input("Masukkan Penulis buku: ")
                book_type = input("Masukkan Tipe buku (Fisik/Digital): ").capitalize()
                if book_type not in ['Fisik', 'Digital']:
                    print("Tipe buku tidak valid! Harus 'Fisik' atau 'Digital'.")
                    continue
                
                new_book = Book(isbn, title, author, book_type)
                library.add_book(new_book)
                print(f"Buku '{title}' (ISBN: {isbn}) berhasil ditambahkan.")
            except Exception as e:
                print(f"Terjadi kesalahan saat menambahkan buku: {e}")
        elif pilih == 2:
            try:
                isbn_to_delete = input("Masukkan ISBN buku yang akan dihapus: ")
                found_book = library.search_book(isbn_to_delete)
                if found_book:
                    library.remove_book(isbn_to_delete)
                    print(f"Buku dengan ISBN '{isbn_to_delete}' berhasil dihapus.")
                else:
                    print(f"Buku dengan ISBN '{isbn_to_delete}' tidak ditemukan.")
            except Exception as e:
                print(f"Terjadi kesalahan saat menghapus buku: {e}")
        elif pilih == 3:
            isbn_to_search = input("Masukkan ISBN buku yang dicari: ")
            found_book = library.search_book(isbn_to_search)
            if found_book:
                print("Buku ditemukan:")
                print(f"  {found_book}")
            else:
                print(f"Buku dengan ISBN '{isbn_to_search}' tidak ditemukan.")
        elif pilih == 4:
            print("\nDaftar semua buku (Level-order):")
            library.list_all_books_level_order()
        elif pilih == 5:
            print(f"Tinggi pohon BST: {library.get_height(library.root)}")
        elif pilih == 6:
            isbn_target = input("Cari successor dari ISBN: ")
            successor = library.find_successor_book(isbn_target)
            if successor:
                print(f"Successor dari ISBN {isbn_target}:\n  {successor}")
            else:
                print(f"Tidak ada successor untuk ISBN {isbn_target} (mungkin ISBN tidak ada atau yang terbesar).")
        elif pilih == 7:
            isbn_target = input("Cari predecessor dari ISBN: ")
            predecessor = library.find_predecessor_book(isbn_target)
            if predecessor:
                print(f"Predecessor dari ISBN {isbn_target}:\n  {predecessor}")
            else:
                print(f"Tidak ada predecessor untuk ISBN {isbn_target} (mungkin ISBN tidak ada atau yang terkecil).")
        elif pilih == 8:
            print("Program Sistem Manajemen Perpustakaan selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()