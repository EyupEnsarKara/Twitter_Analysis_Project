from faker import Faker
import json
import random
from tqdm import tqdm

fake = Faker()

# Toplam kullanıcı sayısı
total_users = 40000

# Her bir grup için kullanıcı sayısı
batch_size = 40000

# Oluşturulan kullanıcıları bir JSON dosyasına yaz
users = {}
other_users = []
for i in tqdm(range(0, total_users, batch_size), desc="Progress"):
    for _ in tqdm(range(batch_size), desc="Creating users part||{}".format(i // 1000 + 1)):
        temp = random.choice(["tr", "en"])
        user_data = {
            "username": fake.user_name(),
            "name": fake.name(),
            "following_count": 0,
            "followers_count": 0,
            "region": temp,
            "language": temp,
            "tweets": [fake.text() for _ in range(random.randint(15,25))],
            "following": set(),
            "followers": [],
        }
        users[user_data["username"]] = user_data
        other_users.append(user_data["username"])

# Her kullanıcıyı birbirini takip edecek şekilde düzenle
for user in tqdm(users.values(), desc="Updating followers"):
    num_followers = min(fake.random_int(min=100, max=350), len(other_users))
    user["following"] = set(random.sample(sorted(set(other_users) - {user["username"]}), num_followers))
    for followed_user in user["following"]:
        followed_user_data = users[followed_user]
        followed_user_data["followers"].append(user["username"])

# Takipçi ve takip edilen sayılarını eşitle
for user in tqdm(users.values(), desc="Balancing follower/following counts"):
    user["followers_count"] = len(user["followers"])
    user["following_count"] = len(user["following"])

# Oluşturulan kullanıcıları JSON dosyasına ekleyin
with open("users60k.json", 'w') as file:
    for user in tqdm(users.values(), desc="Dumping users to JSON"):
        user["following"] = list(user["following"])
        user["followers"] = [
            follower_username for follower_username, follower_data in users.items()
            if user["username"] in follower_data["following"]
        ]
    json.dump(list(users.values()), file, indent=2)

print("Toplam {} kullanıcı oluşturuldu ve users.json dosyasına kaydedildi.".format(total_users))
