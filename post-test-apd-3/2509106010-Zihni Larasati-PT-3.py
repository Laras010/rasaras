class TokoSembako:
    def _init_(self):
        self.produk = {
            '1': {'nama': 'Gula', 'harga': 19000},
            '2': {'nama': 'Susu kental', 'harga': 9000},
            '3': {'nama': 'Tepung', 'harga': 10000},
            '4': {'nama': 'Telur', 'harga': 2500},
            '5': {'nama': 'Coklat batang', 'harga': 25000},
            '6': {'nama': 'Margarin', 'harga': 8000},
        }
          
        
        # Data member (usn & pw)
        self.members = {
            'Andi': 'Andi3105',
            'syifa': 'cipaimut24'
        }
        
        self.keranjang = []
        self.is_member = False
    
    def login(self):
        """Sistem login dengan ternary operator"""
        print("\n" + "="*40)
        print("LOGIN MEMBER")
        print("="*40)
        
        username = input("Username: ")
        password = input("Password: ")
        
        # Ternary operator untuk autentikasi
        status = "Login berhasil!" if self.members.get(username) == password else "Login gagal!"
        print(f"\n{status}")
        
        return self.members.get(username) == password
    
    def tampilkan_menu(self):
        """Menampilkan menu produk"""
        print("\n" + "="*50)
        print("TOKO SEMBAKO LARAS")
        print("="*50)
        print("DAFTAR PRODUK:")
        print("-"*50)
        
        for kode, item in self.produk.items():
            print(f"{kode}. {item['nama']:15} - Rp {item['harga']:>10,}")
        print("-"*50)
    
    def belanja(self):
        """Proses belanja"""
        self.tampilkan_menu()
        
        while True:
            try:
                pilihan = input("\nPilih produk (1-6) atau 's' untuk selesai: ")
                
                if pilihan.lower() == 's':
                    break
                
                if pilihan not in self.produk:
                    print("Pilihan tidak valid!")
                    continue
                
                jumlah = int(input(f"Jumlah {self.produk[pilihan]['nama']}: "))
                
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    continue
                
                # Tambah ke keranjang
                item = {
                    'produk': self.produk[pilihan]['nama'],
                    'harga': self.produk[pilihan]['harga'],
                    'jumlah': jumlah,
                    'subtotal': self.produk[pilihan]['harga'] * jumlah
                }
                self.keranjang.append(item)
                
                print(f"✓ {jumlah} {self.produk[pilihan]['nama']} ditambahkan ke keranjang!")
                
            except ValueError:
                print("Input tidak valid!")
    
    def hitung_total(self):
        """Menghitung total belanja"""
        total = sum(item['subtotal'] for item in self.keranjang)
        return total
    
    def tampilkan_struk(self):
        """Menampilkan struk belanja"""
        if not self.keranjang:
            print("\nKeranjang belanja kosong!")
            return
        
        print("\n" + "="*50)
        print("STRUK BELANJA")
        print("="*50)
        
        total_sebelum_diskon = self.hitung_total()
        
        # Tampilkan detail belanja
        for i, item in enumerate(self.keranjang, 1):
            print(f"{i}. {item['produk']:15}")
            print(f"{i}   {item['jumlah']:2} x Rp {item['harga']:>10,} = Rp {item['subtotal']:>10,}")
        
        print("-"*50)
        
        # Menggunakan f-string untuk formatting output
        if self.is_member:
            diskon = total_sebelum_diskon * 0.15
            total_setelah_diskon = total_sebelum_diskon - diskon
            
            print(f"{'Harga sebelum diskon:':25} Rp {total_sebelum_diskon:>10,}")
            print(f"{'Diskon 15%:':25} Rp {diskon:>10,}")
            print(f"{'Harga setelah diskon:':25} Rp {total_setelah_diskon:>10,}")
            print(f"\n💫 Terima kasih member! Anda hemat Rp {diskon:>10,}")
        else:
            print(f"{'Total harga:':25} Rp {total_sebelum_diskon:>10,}")
            print(f"\n💡 Gabung member sekarang untuk dapat diskon 15%!")
        
        print("="*50)
        print("Terima kasih telah berbelanja! 🛍")
    
    def jalankan(self):
        """Program utama"""
        print("="*50)
        print("SELAMAT DATANG DI TOKO SEMBAKO LARAS")
        print("="*50)
        
        # Tanya status member
        member_input = input("Apakah Anda member? (y/n): ").lower()
        
        if member_input == 'y':
            self.is_member = True
            # Ternary operator untuk menentukan pesan
            pesan = "Silakan login terlebih dahulu" if not self.login() else "Login berhasil! Lanjut ke menu belanja"
            print(pesan)
            
            # Jika login gagal, ubah status menjadi non-member
            if "gagal" in pesan:
                self.is_member = False
                print("Anda akan dilayani sebagai non-member")
        else:
            self.is_member = False
            print("Anda login sebagai non-member")
        
        # Proses belanja
        self.belanja()
        
        # Tampilkan struk
        self.tampilkan_struk()

# Jalankan program
if "_name_" == "_main_":
    toko = TokoSembako()
    toko.jalankan()