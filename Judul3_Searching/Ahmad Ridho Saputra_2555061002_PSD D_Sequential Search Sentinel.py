def sequential_search_sentinel(data, n, target):
    data.append(target)
    i = 0
    while data[i] != target:
        i += 1
    data.pop()
    if i < n:
        return True, i  
    else:
        return False, -1 


def main():
    data = ["Ridho", "Danish", "Ghani", "Atha", "Raja", "Abdul", "Luthfi", "Zahra", "Cindy", "Okta", "Fahra", "Izzul", "Azkal", "Rima", "Rahma", "Marvel", "Abam", "Arsel", "Inshan", "Berkat", "Davy", "Dewa", "Gyoga", "Nabil", "Ramey", "Ledies", "Tifani", "safira"]
    n = len(data)
    print(f"Data array: {data}")
    while True:
        try:
            target = str(input("Masukkan Nama Mahasiswa PSTI D yang ingin dicari : "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan ulang")
    
    found, index = sequential_search_sentinel(data, n, target) # Unpack the tuple
    
    if found:
        print(f"Nama '{target}' ditemukan pada indeks ke-{index} (elemen ke-{index + 1}).")
    else:
        print(f"Nama '{target}' tidak ditemukan.")


if __name__ == "__main__":
    main()