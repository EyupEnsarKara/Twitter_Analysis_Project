import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from variables import Graph, bfs_interest_connections, create_minimum_spanning_tree, drawGraphic, visualize_connections_and_tree

def create_canvas(parent, width, height, color):
    canvas = tk.Canvas(parent, width=width, height=height, bg=color)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    return canvas

def Usersearch():
    plt.clf()

    try:
      
        tempuser = users.get(entry.get())
        if tempuser is None:
            print("User not found")
            return
        graph.add_node(tempuser.username)
        if tempuser.following.start is None:
            print("Takip etmiyor")
        else:
            node = tempuser.following.start
            while node is not None:
                graph.add_node(node.data)
                graph.add_edge(tempuser.username,node.data)
                node = node.next
        nx.draw(graph.convert_to_networkx(), with_labels=True, font_size=10,node_size=100,node_color="gray",font_color="teal")
        plt.show()
        
    except Exception as e:
        print("An error occurred:", str(e))

    

def Interestsearch():
    plt.clf()
    try:
        key=combo.get()
        tempword = interests.get(key)   
        if tempword is None:
            print("word not found")
            return

        graph.add_node(key)
        
        
        node = tempword.start
        while node is not None:
            graph.add_node(node.data)
            graph.add_edge(key,node.data)
            node = node.next
        nx.draw(graph.convert_to_networkx(), with_labels=True, font_size=10,node_size=100,node_color="gray",font_color="teal")
        plt.show()
        
    except Exception as e:
        print("An error occurred:", str(e))

def allUserGraphShow():
    plt.clf()
    try:
        nx.draw(users_graph.convert_to_networkxUser(), with_labels=True, font_size=10,node_size=100,node_color="gray",font_color="teal")
        plt.show()
        
    except Exception as e:
        print("An error occurred:", str(e))

def clearGraphButton_action():
    plt.clf()
    try:
        plt.show()
        graph.clear()
        
    except Exception as e:
        print("An error occurred:", str(e))


def SearchButton3_action():
    # benzerlik eşiği
    interests_similarity_threshold = 0.0001

    source_user = users_graph.get_user(sourceUserEntry.get())
    
    connections = bfs_interest_connections(source_user, interests_similarity_threshold)
  
    tree_edges = create_minimum_spanning_tree(connections)


    visualize_connections_and_tree(connections, tree_edges)

def SearchButton4_action():
    plt.clf()
    try:
        
        drawGraphic(interests_hashlist) 
        
    except Exception as e:
        print("An error occurred:", str(e))

  


    
    

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Arayüz")

# Canvas'ları oluştur
canvas1 = create_canvas(root, 400, 100, "lightblue")
canvas2 = create_canvas(root, 400, 200, "lightblue")
canvas3 = create_canvas(root, 400, 100, "lightblue")
canvas4 = create_canvas(root, 400, 100, "lightblue")
canvas5 = create_canvas(root, 400, 100, "lightblue")
root.configure(bg="black")


# İlk canvas'a arama kutusu ve birinci "Ara" butonu ekle
entry = tk.Entry(canvas1, font=("Helvetica", 14))
entry.pack(pady=10, padx=10)

Usersearch_button1 = tk.Button(canvas1, text="Ara", command=Usersearch, font=("Helvetica", 12))
Usersearch_button1.pack(pady=10)

# Dropdown menüyü ve ikinci "Ara" butonunu yeşil alana taşı
options = []
selected_option = tk.StringVar()
combo = ttk.Combobox(canvas2, values=options, textvariable=selected_option)
combo.set("İlgi alanı seçin")
combo.pack(pady=10, padx=10)

Interestsearch_button = tk.Button(canvas2, text="Ara", command=Interestsearch, font=("Helvetica", 12))
Interestsearch_button.pack(pady=10, padx=10)

#3. canvas ayarları
allUserGraphShowButton = tk.Button(canvas3, text="Tüm kullanıcıların graph'ı", command=allUserGraphShow, font=("Helvetica", 12))
allUserGraphShowButton.pack(pady=10, padx=10)
clearGraphButton = tk.Button(canvas3, text="Grafiği temizle", command=clearGraphButton_action, font=("Helvetica", 12))
clearGraphButton.pack(pady=5, padx=5)
#4. canvas ayarları
sourceUserEntry=tk.Entry(canvas4,font=("Helvetica", 14))
sourceUserEntry.pack(pady=10,padx=10)
bfsSearchButton=tk.Button(canvas4,text="Kullanıcıların ilgi alanları ara",command=SearchButton3_action, font=("Helvetica", 14))
bfsSearchButton.pack(padx=10,pady=10)
#5. canvas ayarları
interests_showButton=tk.Button(canvas5,text="İlgi alanlarını göster",command=SearchButton4_action, font=("Helvetica", 14))
interests_showButton.pack(padx=10,pady=10)
# Değişkenleri aktar


users=0
interests=0
users_graph=0
interests_hashlist=0





graph=Graph()