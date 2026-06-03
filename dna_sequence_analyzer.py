from Bio import SeqIO

#Reads and analyzes sequences from FASTA file
for record in SeqIO.parse("sample.fasta", "fasta"):
    print("ID :",record.id)
    print( "SEQUENCE: ",record.seq)
    print("LENGTH: ",len(record.seq))

#Calculates the nucleotide composition
    print("A: ", record.seq.count("A"))
    print("T: ", record.seq.count("T"))
    print("G: ", record.seq.count("G"))
    print("C: ", record.seq.count("C"))

#Generates complementary DNA sequence 
    print("Complement sequence: ", record.seq.complement())

#calculates DNA content
    print("GC content:", ((record.seq.count("G")+record.seq.count("C"))/len(record.seq)*100))

#Translates DNA sequence to protein
    print("Proteins: ", record.seq.translate())

#Checks whether the given sequence contains the start codon ATG
    if "ATG" in record.seq:
        print("The sequence contains a start codon")
    else:
        print("The sequnece doesn't contain a start codon")
