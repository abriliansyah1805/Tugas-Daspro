def bin_to_dec(bin_num):
    return int(bin_num, 2)

def dec_to_bin(dec_num):
    return bin(dec_num)[2:]

def oct_to_dec(oct_num):
    return int(oct_num, 8)

def dec_to_oct(dec_num):
    return oct(dec_num)[2:]

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def dec_to_hex(dec_num):
    return hex(dec_num)[2:]

def main():
    while True:
        print("\n1. Biner ke Desimal")
        print("2. Desimal ke Biner")
        print("3. Oktal ke Desimal")
        print("4. Desimal ke Oktal")
        print("5. Heksadesimal ke Desimal")
        print("6. Desimal ke Heksadesimal")
        print("7. Keluar")
        
        pil = int(input("Masukkan pilihan Anda: "))

        if pil == 1:
            bin_num = input("Masukkan bilangan biner: ")
            print("Hasil desimal:", bin_to_dec(bin_num))
        elif pil == 2:
            dec_num = int(input("Masukkan bilangan desimal: "))
            print("Hasil biner:", dec_to_bin(dec_num))
        elif pil == 3:
            oct_num = input("Masukkan bilangan oktal: ")
            print("Hasil desimal:", oct_to_dec(oct_num))
        elif pil == 4:
            dec_num = int(input("Masukkan bilangan desimal: "))
            print("Hasil oktal:", dec_to_oct(dec_num))
        elif pil == 5:
            hex_num = input("Masukkan bilangan heksadesimal: ")
            print("Hasil desimal:", hex_to_dec(hex_num))
        elif pil == 6:
            dec_num = int(input("Masukkan bilangan desimal: "))
            print("Hasil heksadesimal:", dec_to_hex(dec_num))
        elif pil == 7:
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan anda tidak valid")

if __name__ == "__main__":
    main()