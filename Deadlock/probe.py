from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.u = u
        self.v = v
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):

        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        recStack[v] = False
        return False
 
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
 

size = int(input("Enter the number of processes - "))

procesess = []
resources = []

for i in range(size):
    pro = int(input("Enter the proceses -  "))
    procesess.append(pro)
    res = int(input("Enter the resources - "))
    resources.append(res)

start = int(input("Enter the intiator - "))
ind = procesess.index(start)

temp_1 = []
temp_2 = []
temp_3 = []
temp_4 = []

temp_1 = procesess[0:ind]
temp_2 = procesess[ind:]
temp_3 = resources[0:ind]
temp_4 = resources[ind:]

new_process = temp_2 + temp_1
new_resource = temp_4 + temp_3

# new_process.append(new_process[0])
# new_resource.append(new_resource[0])

print(new_process)
print(new_resource)

for i in range(size):
    p = procesess[i]
    r = resources[i]
    print(str(p) + "->" + str(r))

print("Probe message initiated by the processor - ", start)
for i in range(size-1):
    print("Initiator - ",start , "Sender - " , new_process[i] , "Reciver - ", new_process[i+1]) 



g = Graph(size)

for i in range(size):
    g.addEdge(procesess[i],resources[i])

if g.isCyclic() == 1:
    print("Initiator - ",start , "Sender - " , new_process[size-1] , "Reciver - ", start) 
    print("There is deadlock")
else:
    print("There is no deadlock")