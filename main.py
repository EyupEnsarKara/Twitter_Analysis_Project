import tkinter as tk
from tkinter import ttk
import initTkinter as root
from variables import *
import json
from tqdm import tqdm

import networkx as nx
import matplotlib.pyplot as plt



#global değişkenler
users =HashMap()


with open("users1k.json", 'r') as file:
    try:
        # Json dosyasından veri okuma
        jsonlist = json.load(file)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        jsonlist = []

#loading users
for user in tqdm(jsonlist, desc="Loading Users From Json File"):
    users.set(user["username"], User(user["name"], user["username"], user["followers_count"], user["following_count"],user["language"],user["region"], user["tweets"], user["followers"], user["following"]))

users_graph=add_users_to_graph(users)

interests=dfsTextAnalyze(users_graph.nodes.start.data)
root.combo["values"]=convert_Hashmap_to_list(interests)


interests_hashlist=write_hashedLinkedList(interests)



root.users=users
root.interests=interests
root.users_graph=users_graph
root.interests_hashlist=interests_hashlist




root.root.mainloop()