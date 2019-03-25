# This script was written to convert the ComplexHistogram.dat file (an output of fpr) in to a human-readable and plotable format. 

import sys

file=open(sys.argv[1],"r")

L=file.readlines()
file.close()

list=[]
it=[]    #number of the lines that report the iteration
m=[]
p=[]
pm=[]
ppm=[]
mppm=[]
pp=[]
cluster = 0;
oldcluster = 0;


for line in L:
    list.append(line.strip())
    #print(list)

    
#print(it)
#print(''.join(map(str,it)))

#Now we have the list of all iterations, and we have a list of all lines.

for n in list:
    l=n.split()
    if l[0]=="iter:":
        if len(m)<len(it):
            m.append(0)
        if len(p)<len(it):
            p.append(0)
        if len(pm)<len(it):
            pm.append(0)
        if len(pp)<len(it):
            pp.append(0)
        if len(ppm)<len(it):
            ppm.append(0)
        if len(mppm)<len(it):
            mppm.append(0)
        it.append(l[1])

    elif l[1]=="PIP:" and len(l)==3:
        m.append(l[0])
    elif l[1]=="end:"and l[2]=="1." and len(l)==3:
        p.append(l[0])
    elif l[1]=="PIP:" and l[2]=="1."and l[3]=="end:" and l[4]=="1.":
        pm.append(l[0])
    elif l[1]=="end:"and l[2]=="2." and len(l)==3:
        pp.append(l[0])
    elif l[1]=="PIP:" and l[2]=="1."and l[3]=="end:" and l[4]=="2.":
        ppm.append(l[0])
    elif l[1]=="PIP:" and l[2]=="2."and l[3]=="end:" and l[4]=="2.":
        mppm.append(l[0])


#print(it)
#print(m)
#print(p)
#print(pm)
#print(pp)
#print(ppm)
#print(mppm)


myoutput=open("outhist.txt","w")
sys.stdout=myoutput

print("{:>7s}{:>8s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}".format("it","M","P","PM","PP","PPM","MPPM"))

for a,b,c,d,e,f,g in zip(it,m,p,pm,pp,ppm,mppm):
    print("%8s %8s %8s %8s %8s %8s %8s"%(a,b,c,d,e,f,g))
    #myoutput.write("%5s %5s %5s %5s %2s %2s %2s"%(a,b,c,d,e,f,g))


myoutput.close()
