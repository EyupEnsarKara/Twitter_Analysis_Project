import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords




# Linked List
class LinkedList:
    class LNode:
        def __init__(self,data):
            self.data=data
            self.next=None

    def __init__(self):
        self.start=None
        self.count=0

    def add(self,data):
        newNode=self.LNode(data)

        if self.start is None:
            self.start = newNode
            return
        else:
            newNode.next=self.start
            self.start=newNode
    
    def get(self,data):
        temp=self.start
        while temp is not None:
            if data is temp.data:
                return data
            temp=temp.next
        return None
    def pop(self):
        if self.start is None:
            return None
        else:
            temp=self.start
            self.start=self.start.next
            return temp.data

    def contains(self,data):
        temp=self.start
        while temp is not None:
            if data is temp.data:
                return True
            temp=temp.next
        return False
    def print(self):
        current = self.start
        while current:
            print(current.data)
            current=current.next
        print("None")
    
    def dictConverter(self):
        tempnode=self.start
        tempdict=[]
        while tempnode is not None:
            tempdict.append(tempnode.data)
            tempnode=tempnode.next
        return tempdict
    def get_data_at_index(linked_list, index):
        current = linked_list.start
        count = 0

        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1

        return None
    def getHashList(self,data):
        tempnode=self.start
        while tempnode is not None:
            if tempnode.data.key == data:
                return tempnode

            tempnode=tempnode.next
        return None
    
    def lenght(self):
        count=0
        tempnode=self.start
        while tempnode is not None:
            count+=1
            tempnode=tempnode.next
        return count
        













#Graph Class'ı
class Graph:

    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.edges = LinkedList()
    def __init__(self):
        self.nodes = LinkedList()

    def add_node(self, value):
        node = self.GraphNode(value)
        self.nodes.add(node)

    def add_edge(self, source_value, destination_value):
        source = None
        destination = None

        node=self.nodes.start
        for node in self.nodes.dictConverter():
            if node.value == source_value:
                source = node
            elif node.value == destination_value:
                destination = node

        if source is not None and destination is not None:
            source.edges.add(destination)
    def clear(self):
        self.nodes=LinkedList()

    def convert_to_networkx(graph):
        G = nx.Graph()

        for node in graph.nodes.dictConverter():
            G.add_node(node.value)
            for edge in node.edges.dictConverter():
                G.add_edge(node.value, edge.value)

        return G
    
    def convert_to_networkxUser(graph):
        G = nx.Graph()

        for node in graph.nodes.dictConverter():
            G.add_node(node.value.username)
            for edge in node.edges.dictConverter():
                G.add_edge(node.value.username, edge.value.username)

        return G
    def isHere(self,value):
        tempnode=self.nodes.start
        while tempnode is not None:
            if tempnode.data.value.username == value:
                return True
            tempnode=tempnode.next
        return False
    
    def get_user(self,key):
        node=self.nodes.start
        while node is not None:
            if node.data.value.username == key:
               return node.data     
            node=node.next
        return None
    




class HashMap:
    class hashedLinkedList:
        class hNode:
            def __init__(self, key, value):
                self.key = key
                self.value = value
                self.next = None

        def __init__(self,key):
            self.start=None
            self.count=0
            self.key=key
        def add(self,key,value):
            newNode=self.hNode(key,value)

            if self.start is None:
                self.start = newNode
                return
            else:
                newNode.next=self.start
                self.start=newNode
        def get(self,key):
            temp=self.start
            while temp is not None:
                if key is temp.key:
                    return temp.value
                temp=temp.next
            return temp
        def dictConverter(self):
            tempnode=self.start
            tempdict=[]
            while tempnode is not None:
                tempdict.append(tempnode.value)
                tempnode=tempnode.next
            return tempdict


    def __init__(self):
        self.size = 100
        self.buckets = LinkedList()

    def _hash(self, key):
        
        return hash(key) % self.size
     
    def set(self, key, value):
        index = self._hash(key)
        node = self.buckets.getHashList(index)
        if node is None:
            self.buckets.add(self.hashedLinkedList(index))
            node = self.buckets.getHashList(index)
        
        node.data.add(key,value)
        


    def get(self, key):
        index = self._hash(key)
        if self.buckets.getHashList(index) is None:
            return None
        node = self.buckets.getHashList(index).data.start 

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

        
    

    def dictConverter(self):
        result = []
        tempnode = self.buckets.start
        while tempnode is not None:
            node = tempnode.data.start
            while node is not None:
                result.append(node.key)
                node = node.next
            tempnode = tempnode.next    
         
        return result
    def dictConverterHashed(self):
        result = {}
        tempnode = self.buckets.start
        while tempnode is not None:
            node = tempnode.data.start
            while node is not None:
                result[node.key] = node.value
                node = node.next
            tempnode = tempnode.next    
         
        return result
    
    def print(self):
        tempnode=self.buckets.start
        count =0
        while tempnode is not None:
            node=tempnode.data.start
            while node is not None:
                print(str(tempnode.data.key)+"|||||"+node.key)
                count+=1
                node=node.next
            tempnode=tempnode.next



#for user
class User:
    def __init__(self,name,username,followers_count,following_count,lang,area,tweets,followers,following):
        self.name=name
        self.username=username
        self.followers_count=followers_count
        self.following_count=following_count
        self.lang=lang
        self.area=area
        self.tweets=LinkedList()
        for tweet in tweets:
            self.tweets.add(tweet)
        self.followers=LinkedList()
        for follower in followers:
            self.followers.add(follower)
        self.following=LinkedList()
        for follow in following:
            self.following.add(follow)
        self.interests=LinkedList()
    #conver one string
    def convertTweetsOneString(self):
        tempnode=self.tweets.start
        sumstr=""
        while tempnode is not None:
            sumstr=(sumstr+" "+tempnode.data)
            tempnode=tempnode.next
        return sumstr
    def add_interests(self,interests):
        self.interests=interests




class analyze:
    def temizle(text):
    
        text = re.sub(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ\s]', '', text)
    
        return text
    
    def tokenize(text):
        return word_tokenize(text, language='english')
    
    def remove_stopwords(words):
        stop_words = set(stopwords.words('english'))
        return [word for word in words if word not in stop_words]

    def interest_analyze(self,text):
        text=text.lower()
        cleaned_text = self.temizle(text)
        words = self.tokenize(cleaned_text)
        meaningful_words = self.remove_stopwords(words)
    
        word_freq=LinkedList()
        for word in meaningful_words:
            word_freq.add(word)
        return word_freq

    
    


#bütün kullanıcıları bir grafa aktarma
def add_users_to_graph(users):
    graph=Graph()
    with tqdm(desc="Adding Users To Graph") as pbar:
        hashedLinkedListNode=users.buckets.start
        while hashedLinkedListNode is not None:
            LinkedListNode=hashedLinkedListNode.data.start
            while LinkedListNode is not None:
                user=LinkedListNode.value
                graph.add_node(user)
                LinkedListNode=LinkedListNode.next
                pbar.update(1)
            hashedLinkedListNode=hashedLinkedListNode.next
    graph=add_users_edges_to_graph(graph,users)
    return graph

#bağlı olanlara kenar ekleme
def add_users_edges_to_graph(graph, users):
    with tqdm(desc="Adding Edges To Graph") as pbar:
        hashedLinkedListNode = users.buckets.start
        while hashedLinkedListNode is not None:
            LinkedListNode = hashedLinkedListNode.data.start
            while LinkedListNode is not None:
                user = LinkedListNode.value
                followerNode = LinkedListNode.value.followers.start
                while followerNode is not None:
                    followerUserData = users.get(followerNode.data)
                    if graph.isHere(followerNode.data):
                        graph.add_edge(user, followerUserData)
                    else:
                        graph.add_node(followerUserData)
                        graph.add_edge(user, followerUserData)
                    followerNode = followerNode.next
                pbar.update(1)
                LinkedListNode = LinkedListNode.next
            hashedLinkedListNode = hashedLinkedListNode.next
    return graph



#graph için bir stack yapısı
class graphStack:
    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.edges = LinkedList()
            self.next=None
    def __init__(self):
        self.start=None
    
    def add(self,value):
        newNode=self.GraphNode(value)

        if self.start is None:
            self.start = newNode
            return
        else:
            newNode.next=self.start
            self.start=newNode
    def pop(self):
        if self.start is None:
            return None
        else:
            temp=self.start
            self.start=self.start.next
            return temp.value
    def contains(self,data):
        temp=self.start
        while temp is not None:
            if data is temp.value.value.username:
                return True
            temp=temp.next
        return False
    def length(self):
        temp=self.start
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count

#graph için bir kuyruk yapısı
class graphQueue:
    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.edges = LinkedList()
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        newNode = self.GraphNode(value)

        if self.rear is None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

        return temp.value

    def isEmpty(self):
        return self.front is None

    def contains(self, data):
        temp = self.front
        while temp is not None:
            if data is temp.value.value.username:
                return True
            temp = temp.next
        return False

    def length(self):
        temp = self.front
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count



def dfsTextAnalyze(startnode):
    interests=HashMap()
    visited = LinkedList()
    stack = graphStack()
    stack.add(startnode)
    count=0
    
    with tqdm(desc="Processing interests")as pbar:
        while stack.start is not None:
            
            node = stack.pop()
            if not visited.contains(node):
                visited.add(node.value.username)
                #uygulanacak işlemler

                user_interest=LinkedList()

                analiz_result = analyze.interest_analyze(analyze,node.value.convertTweetsOneString().lower())
                wordNode = analiz_result.start
                while wordNode is not None:
                    word=wordNode.data

                    if interests.get(word) is not None:
                        temp=interests.get(word)
                        temp.add(node.value.username)
                        temp.count+=1
                        
                    else:
                        tempLinkedList=LinkedList()
                        tempLinkedList.add(node.value.username)
                        tempLinkedList.count+=1
                        interests.set(word, tempLinkedList)
                    
                    user_interest.add(word)
                    wordNode=wordNode.next
                node.value.add_interests(user_interest)
                pbar.update(1)
                


                for edge in node.edges.dictConverter():
                    if not visited.contains(edge.value.username) and not stack.contains(edge.value.username):

                        stack.add(edge)
                    

    return interests
        


def bfs_interest_connections(start_user, interests_similarity_threshold):
    visited = LinkedList()
    queue = LinkedList()
    queue.add(start_user)

    connections = []

    while queue.start:
        current_user = queue.start.data
        queue.start = queue.start.next
        visited.add(current_user)

        for neighbor in current_user.edges.dictConverter():
            if not visited.contains(neighbor) and not queue.contains(neighbor):
                similarity = calculate_interests_similarity(current_user, neighbor)
                if similarity >= interests_similarity_threshold:
                    connections.append((current_user, neighbor))
                    queue.add(neighbor)

    return connections


def create_minimum_spanning_tree(connections):
    visited = set()
    stack = graphStack()
    for connection in connections:
        stack.add(connection[0])
        stack.add(connection[1])

    tree_edges = []

    while stack.start is not None:
        current_user = stack.pop()

        if current_user not in visited:
            visited.add(current_user)

            for neighbor in current_user.edges.dictConverter():
                if neighbor not in visited and connection_exists(connections, current_user, neighbor):
                    tree_edges.append((current_user, neighbor))
                    stack.add(neighbor)

    return tree_edges

def connection_exists(connections, user1, user2):
    return (user1, user2) in connections or (user2, user1) in connections


def visualize_connections_and_tree(connections, tree_edges):
    G = nx.Graph()

    # Bağlantıları ekle
    for connection in connections:
        G.add_edge(connection[0].value.username, connection[1].value.username, color='blue')

    # Minimum Spanning Tree'i ekle
    for edge in tree_edges:
        G.add_edge(edge[0].value.username, edge[1].value.username, color='green')

    # Çizim
    pos = nx.spring_layout(G)

    # Kenarları bir liste olarak al
    edges = list(G.edges())
    edge_colors = [G[u][v]['color'] for u, v in edges]

    nx.draw(G, pos, edgelist=edges, edge_color=edge_colors, with_labels=True)

    # Grafik gösterme
    plt.show()




def calculate_interests_similarity(user1, user2):
    interests1 = set(user1.value.interests.dictConverter())
    interests2 = set(user2.value.interests.dictConverter())

    common_interests = interests1.intersection(interests2)
    similarity = len(common_interests) / (len(interests1) + len(interests2) - len(common_interests))
    return similarity


   
def write_hashedLinkedList(sorted_list):
    temp=HashMap.hashedLinkedList("0")

    current = sorted_list.buckets.start
    while current is not None:
        hashnode=current.data.start
        while hashnode is not None:
            #file.write(f"{hashnode.key}: {hashnode.value.count}\n")
            temp.add(hashnode.key,hashnode.value.count)
            hashnode=hashnode.next
        current = current.next
    
    return temp
    
def drawGraphic(interests_hashlist):    

    categories = []
    values = []
    
    tempnode=interests_hashlist.start
    while tempnode is not None:
        categories.append(tempnode.key)
        values.append(tempnode.value)
        tempnode=tempnode.next


    plt.bar(categories, values, color='blue')

    # Grafiği düzenleme
    plt.xlabel('İlgi alanları')
    plt.ylabel('Değerler')
    plt.title('İlgi Alanlarına Göre Kullanıcı Sayısı')

    plt.show()



def convert_Hashmap_to_list(hashmap):
    hashlist_start_node = hashmap.buckets.start
    list=[]
    while hashlist_start_node is not None:
        node = hashlist_start_node.data.start
        while node is not None:
            list.append(node.key)
            node = node.next
        hashlist_start_node = hashlist_start_node.next
    return list