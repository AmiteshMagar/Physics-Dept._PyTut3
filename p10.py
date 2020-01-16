
file1 = open("expt.dat","r")
lines = file1.readlines()
C,V,Q,E=[],[],[],[]
for line in lines:
    k = line.find(' ')
    k1 = line.find('\n')
    num1 = int(line[0:k])
    C.append(num1)
    num2 = int(line[k+1:k1])
    V.append(num2)
file1.close()

def charge(c,v):
    return c*v
def energy(c,v):
    num = 0.5* c * (v**2)
    return num

for k in range(len(C)):
    Q.append(charge(C[k],V[k]))
    E.append(energy(C[k],V[k]))

file2 = open("ce.out","w")
for k in range(len(C)):
    string = str(C[k])+" "+str(V[k])+" "+str(Q[k])+" "+str(E[k])+"\n"
    file2.write(string)

file2.close()


