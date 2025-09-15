import json
import os
from func import get_usernames

class BaseJsonFile:
    def __init__(self,file_name):
        self.file_name = file_name
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)

        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=1)

    def read_json(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []


class Followers(BaseJsonFile):
    def __init__(self):
        super().__init__("Takipçiler ve Takip Edilenler(JSON)/followers_1.json")

    def show_followers(self):
        followers = self.read_json()

        if not followers:
            print("Sizi Takip Eden Kimse Yok")
        else:
            print("Takipçiler:\n")
            for item in get_usernames(followers):
                print(item)

class Followings(BaseJsonFile):
    def __init__(self):
        super().__init__("Takipçiler ve Takip Edilenler(JSON)/following.json")

    def show_followings(self):
        following = self.read_json()

        if not following:
            print("Takip Ettiğiniz Kimse Yok")
        else:
            print("Takip Ettiklerin:\n")
            for item in get_usernames(following):
                print(item)



