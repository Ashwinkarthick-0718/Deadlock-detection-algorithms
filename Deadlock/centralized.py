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
 


total_site = int(input("Enter the total number of sites - "))
new_list = [[]for i in range(total_site)]

process= []
s=0
while(s<total_site):

    s = int(input("Enter the site - "))
    np = int(input("Enter the number of processes - "))
    process.append(np)
    g = Graph(np)

    for i in range(np):
        p = int(input("Process - "))
        hol = int(input("Resource that is held by the process - "))
        r = int(input("Process requesting for resource - "))
        g.addEdge(p,r)
        new_list[s-1].append(str(p)+"->"+str(r))

    print(new_list)
    if g.isCyclic():
        print("Local Deadlock in site - ",s)
    else:
        print("There is no deadlock in site - ",s)
    print("\n")

l = []
l = [num for sublist in new_list for num in sublist]

res = [*set(l)]
print("After merging the given sites - ",res)

maximum = max(process)

g = Graph(maximum)

for i in res:
    new_pro = int(i[0])
    new_res = int(i[3])
    g.addEdge(new_pro,new_res)

if g.isCyclic():
    print("Deadlock in gloabal level")
else:
    print("There is no deadlock in global level3")