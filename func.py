def main_menu():
    actions = [
        "Takipçileri Listele",
        "Takip Edilenleri Listele",
        "Gizli Hayranları Listele",
        "Hayranı Olduklarımı Listele",
        "Çıkış"
    ]
    print("======InstaGhost======")
    for index, item in enumerate(actions, start=1):
        print(f"{index} -> {item}")
    print()

    while (True):
        try:
            choice = int(input("Lütfen Yapmak İstdiğiniz İşlemi Seçiniz: "))
            if 1 <= choice <= len(actions):
                print(f"{actions[choice - 1]} Seçildi. Yönlendiriliyorsunuz...\n")
                return choice
            else:
                print("Hata! Geçerli sayı giriniz.\n")

        except ValueError as e:
            print(f"Hata! Sayı Giriniz: {e}\n")

def message():
    print("\nİşlem Tamamlandı Ana Menüye Yönlendiriliyorsunuz...\n")

def get_usernames(data):
    return [x["string_list_data"][0]["value"] for x in data]
