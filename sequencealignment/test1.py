from Bio.Seq import Seq
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
matrix = matlist.blosum62
i=input("Enter first sequence: ");
seq_1=Seq(i);
i=input("Enter first sequence: ");
seq_2=Seq(i);
g=-1;
alpha=2
beta=-2
score=0;
length=len(seq_1)
for  i in range(length):
    if(seq_1[i]==seq_2[i]):
        score+=alpha
    elif((seq_1[i]=="-")or(seq_2[i]=="-")):
        score+=g
    elif(seq_1[i]!=seq_2[i]):
        score+=beta;
print "Mismatch Match gap value"
print "Alpha=2"
print "Beta=-2"
print "gap penalty=-1"
print "Score"
print score




