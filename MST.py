#Heap class declaration begins

class heap:

    def __init__(self):
        self.s = 0
        self.A = {}
        self.p = {}
        self.key = {}
        
    def heapify_up(self,i):
        s = self.s;A = self.A;p = self.p;key = self.key;
        while(i>1):
            j = i//2
            if(key[A[i]] < key[A[j]]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                p[A[i]] = i
                p[A[j]] = j
                i = j

            else:
                break
        self.s = s;self.A = A;self.p = p;self.key = key;

    def heapify_down(self,i):
        s = self.s;A = self.A;p = self.p;key = self.key;
        while(2*i<=s):
            if((2*i == s) | (key[A[2*i]] <= key[A[2*i+1]])):
               j = 2*i
            else:
               j = 2*i + 1
            if(key[A[j]] < key[A[i]]):
               temp = A[i]
               A[i] = A[j]
               A[j] = temp
               p[A[i]] = i
               p[A[j]] = j
               i = j
            else:
               break
        self.s = s;self.A = A;self.p = p;self.key = key;

    def insert(self,v, key_value):
        s = self.s;A = self.A;p = self.p;key = self.key;
        s = s + 1
        A.update({s : v})
        p.update({v : s})
        key.update({v : key_value})
        self.s = s;self.A = A;self.p = p;self.key = key;
        self.heapify_up(s)


    def extract_min(self):
        s = self.s;A = self.A;p = self.p;key = self.key;
        ret = A[1]
        A[1] = A[s]
        p[A[1]] = 1
        s = s-1
        self.s = s;self.A = A;self.p = p;self.key = key;
        if(s>=1):
            self.heapify_down(1)
        return ret

    def decrease_key(self,v,key_value):
        s = self.s;A = self.A;p = self.p;key = self.key
        key[v] = key_value
        self.s = s;self.A = A;self.p = p;self.key = key;
        self.heapify_up(p[v])

#Heap class declaration ends

b = []
u = []
weights = {}
swe = {}
vertices = {}
vms = {}
pif = {}
S = {}
sumofweights = 0
file = open("input.txt")
i = 0
j = 0
counter = 1

for line in file:
    b.append(line)
    if(i == 0):
        size = b[i].split(" ")
        numvert = int(size[0])
        size[1] = size[1].replace("\n","")
        i += 1
        continue
    temp = b[i].split(" ")
    temp[2] = temp[2].replace("\n","")
    temint = int(temp[2])
    weights.update({temp[0]+ " and " +temp[1] : temint})
    weights.update({temp[1]+ " and " +temp[0] : temint})
    i += 1


while(counter <= numvert):
    vertices.update({str(counter) : 1000001})
    counter += 1

counter = 1
while(counter <= numvert):
    vms.update({str(counter) : 1000001})
    counter += 1

vertices["1"] = 0

file.close()

Q = heap()
for v in vertices:
    Q.insert(v,vertices[v])

counter = 1
while(counter <= numvert):
    u = Q.extract_min()
    counter += 1
    del vms[u]
    for v in vms:
        if(weights.get(u + " and " + v) != None):
            if(weights.get(u + " and " + v) < vertices[v]):
                vertices[v] = weights.get(u  + " and " + v)
                Q.decrease_key(v,vertices[v])
                pif.update({v : u})
                

for w in vertices:
    sumofweights += vertices[w]



file = open("output.txt","w")
file.write(str(sumofweights) + "\n")

for v in vertices:
    if(v != "1"):
        file.write(v + " " + str(pif.get(v)) + "\n")
        

file.close()                


