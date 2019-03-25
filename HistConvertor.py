# This script was written to convert the ComplexHistogram.dat file (an output of fpr) in to a human-readable and plotable format. 
# it currently lacks the efficient sync needed between the columns, meaning at every block of info reports (between two iterations)
# it does not account for the species that were not reported, hence there happens to be a shift in the data.


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


for line in L:
  list.append(line.strip())

#print(list)
# So far we have every line of the file saved as an item in one big list.
    


for n in list:
    l=n.split()  # I now split each item of the list. we now have a list of all the words in a line.
    if l[0]=="iter:":
        it.append(l[1])
        #m.append(0)
        #p.append(0)
        #pm.append(0)
        #pp.append(0)
        #ppm.append(0)
        #mppm.append(0)
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

print("{:>4s}{:>5s}{:>7s}{:>6s}{:>6s}{:>7s}{:>7s}".format("it","M","P","PM","PP","PPM","MPPM"))

for a,b,c,d,e,f,g in zip(it,m,p,pm,pp,ppm,mppm):
    print("%5s %5s %5s %5s %5s %5s %5s"%(a,b,c,d,e,f,g))
    #myoutput.write("%5s %5s %5s %5s %2s %2s %2s"%(a,b,c,d,e,f,g))


myoutput.close()
#now we have the lists but there is no garantee that they match temporally

#where I left off: I made individual lists of all the copy numbers of all six species plus the iteration, but I still cannot get them to merge in a clean table format.I can show them in a table, but that doesnt mean they are reported at the same time step as each other.
