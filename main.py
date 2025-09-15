from func import main_menu,message,get_usernames
from classes import Followers,Followings

followers = Followers()
followings = Followings()

while True:
    choice = main_menu()

    if choice == 1:
        followers.show_followers()
        message()
    elif choice == 2:
        followings.show_followings()
        message()
    elif choice == 3:
        follower = get_usernames(followers.read_json())
        following = get_usernames(followings.read_json())

        hayranlar = set(follower) - set(following)

        print("Gizli Hayranlar Listesi:\n")
        for item in hayranlar:
            print(item)

        message()
    elif choice == 4:
        follower = get_usernames(followers.read_json())
        following = get_usernames(followings.read_json())

        hayranolduklarim= set(following) - set(follower)

        print("Hayran Olduklarım Listesi:\n")
        for item in hayranolduklarim:
            print(item)

        message()
    elif choice == 5:
        print("Çıkış Yapılıyor. Yine Bekleriz :)")



