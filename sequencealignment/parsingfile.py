from Bio.Seq import Seq
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
matrix = matlist.blosum62
from Bio import SeqIO
print "Parsing"
i=input("Enter first sequence: ");
count=0;
seq_1=Seq(i);
g=-1;
#gap penalty
alpha=2
#match
beta=-2
#mismatch
score=0;
#score with gap penalty
score_wg=0;
#score withot gap penalty
#seq_record.id is sequence id of record in database
#seq_record.seq is sequence  in genbank databse
length=len(seq_1);
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
        score=0;
        for  i in range (length):
                if(seq_1[i]==seq_record.seq[i]):
                        score+=alpha
                elif((seq_1[i]=="-")or(seq_record.seq[i]=="-")):
                        score+=g
                elif(seq_1[i]!=seq_record.seq[i]):
                        score+=beta;
        print "Mismatch Match gap value"
        print "Alpha=2"
        print "Beta=-2"
        print "gap penalty=-1"
                #print "Score with gap penatly"
        
        for a in pairwise2.align.globalxx(seq_1[i], seq_record.seq[i]):
                 print pairwise2.format_alignment(*a)
