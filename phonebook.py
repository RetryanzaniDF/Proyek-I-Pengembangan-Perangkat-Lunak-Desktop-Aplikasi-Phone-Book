import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_contacts():
    with open('data.txt', 'r') as f:
        data = f.readlines()
    phonebook = [line.strip().split('\t') for line in data]
    return phonebook

def write_contact(phonebook):
    with open('data.txt', 'w') as file:
        for contact in phonebook:
            file.write('\t'.join(contact) + '\n')
    
def add_contact(phonebook):
    name = input('Masukkan nama kontak baru: ')
    if search_data(name, phonebook) != -1:
        print('Kontak sudah ada.')
        return
    else :
        number = input('Masukkan nomor kontak baru: ')
        phonebook.append([name, number])
        write_contact(phonebook)
    
def contact_data(phonebook):
    clear_screen()
    print("Daftar kontak:")
    print('Nama\tNomor')
    for data in phonebook:
        print(f'{data[0]}\t{data[1]}')
    input("\n \n \n \n \n\t\t\t\t\t\t\tPress enter to next program")
    clear_screen()
    
def delete_contact(phonebook):
    name = input('Masukkan nama kontak yang ingin dihapus: ')
    if search_data(name, phonebook) == -1:
        print('Kontak tidak ditemukan.')
    else:
        del phonebook[search_data(name, phonebook)]
        print('Kontak berhasil dihapus.')
        write_contact(phonebook)

def search_data(name, phonebook):
    clear_screen()
    for i, contact in enumerate(phonebook):
        if contact[0] == name:
            return i
    return -1
        
def update_contact(phonebook):
    name = input('Masukkan nama kontak yang ingin diupdate: ')
    index = search_data(name, phonebook)
    if index == -1:
        print('Kontak tidak ditemukan.')
    else:
        field = input('Update (nama/nomor) : ')
        value = input(f'Masukkan {field} baru: ')
        phonebook[index][0 if field == 'name' else 1] = value
        print('Kontak berhasil diupdate.')
        write_contact(phonebook)
        
def search_contact(phonebook):
    target = input('Masukkan nama atau nomor telepon yang ingin dicari: ')
    results = []
    for contact in phonebook:
        if target in contact[0] or target in contact[1]:
            results.append(contact)
    if not results:
        print('Kontak tidak ditemukan.')
    else:
        print('Hasil pencarian:')
        print('Nama\tNomor')
        for contact in results:
            print(f'{contact[0]}\t{contact[1]}')
                
def first_page():
    print(" __      __          ___                                      ______        ____    __                              ____                    __         ")
    print("/\ \  __/\ \        /\_ \                                    /\__  _\      /\  _`\ /\ \                            /\  _`\                 /\ \        ")
    print("\ \ \/\ \ \ \     __\//\ \     ___    ___     ___ ___      __\/_/\ \/   ___\ \ \L\ \ \ \___     ___     ___      __\ \ \L\ \    ___     ___\ \ \/'\    ")
    print(" \ \ \ \ \ \ \  /'__`\\\ \ \   /'___\ / __`\ /' __` __`\  /'__`\ \ \ \  / __`\ \ ,__/\ \  _ `\  / __`\ /' _ `\  /'__`\ \  _ <'  / __`\  / __`\ \ , <    ")
    print("  \ \ \_/ \_\ \/\  __/ \_\ \_/\ \__//\ \L\ \/\ \/\ \/\ \/\  __/  \ \ \/\ \L\ \ \ \/  \ \ \ \ \/\ \L\ \/\ \/\ \/\  __/\ \ \L\ \/\ \L\ \/\ \L\ \ \ \\\`\  ")
    print("   \ `\___x___/\ \____\/\____\ \____\ \____/\ \_\ \_\ \_\ \____\  \ \_\ \____/\ \_\   \ \_\ \_\ \____/\ \_\ \_\ \____\\\ \____/\ \____/\ \____/\ \_\ \_\ ")
    print("    '\/__//__/  \/____/\/____/\/____/\/___/  \/_/\/_/\/_/\/____/   \/_/\/___/  \/_/    \/_/\/_/\/___/  \/_/\/_/\/____/ \/___/  \/___/  \/___/  \/_/\/_/")
    input("\n \n \n \n \n\t\t\t\t\t\t\tPress enter to next program")

def menu_page():
    print("\t\t\t\t\t\t\t\t\t\t /'\_/`\                          ")
    print("\t\t\t\t\t\t\t\t\t\t/\      \     __    ___   __  __  ")
    print("\t\t\t\t\t\t\t\t\t\t\ \ \__\ \  /'__`\/' _ `\/\ \/\ \ ")
    print("\t\t\t\t\t\t\t\t\t\t \ \ \_/\ \/\  __//\ \/\ \ \ \_\ \ ")
    print("\t\t\t\t\t\t\t\t\t\t  \ \_\\\ \_\ \____\ \_\ \_\ \____/")
    print("\t\t\t\t\t\t\t\t\t\t   \/_/ \/_/\/____/\/_/\/_/\/___/ ")

def main():
    phonebook = read_contacts()
    first_page()
    clear_screen()
    while True:
        clear_screen()
        menu_page()
        choice  = int(input("1. Tambah kontak \n2. Tampilkan seluruh kontak \n3. Perbarui data kontak \n4. Hapus data kontak \n5. Cari data kontak \n6. Exit \nMasukkan pilihan menu anda : "))
        if choice == 1:
            clear_screen()
            add_contact(phonebook)
        elif choice == 2 :
            print('Daftar Kontak:')
            contact_data(phonebook)
        elif choice == 3 :
            clear_screen()
            update_contact(phonebook)
            input("\n \n \n \n \n\t\t\t\t\t\t\tPress enter to next program")
            clear_screen()
        elif choice == 4 :
            delete_contact(phonebook)
            input("\n \n \n \n \n\t\t\t\t\t\t\tPress enter to next program")
            clear_screen()
        elif choice == 5 :
            search_contact(phonebook)
            input("\n \n \n \n \n\t\t\t\t\t\t\tPress enter to next program")
            clear_screen()
        elif choice == 6 :
            print('Terima kasih telah menggunakan aplikasi Phonebook.')
            break
        else:
            print('Pilihan tidak valid.') 
            
if __name__ == '__main__':
    main()