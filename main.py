from pysam import FastaFile
fasta = "test.fasta"

# read the FASTA file.
dna_strings = FastaFile(fasta)

# int with the number of reference sequences in the file. This is a read-only attribute.
n = dna_strings.nreferences

# tuple with the names of reference sequences.
sequences = dna_strings.references

# tuple with the lengths of reference sequences.
dna_lengths = dna_strings.lengths


def calc_gc_perc(sequence, i):
    gc = 0
    for base in sequence:
        if(base == "G" or base == "C"):
            gc += 1
    gc_perc = (gc/dna_lengths[i])*100
    return gc_perc


max_gc_perc = calc_gc_perc(sequences[0], 0)
max_gc_seq = sequences[0]

for i in range(n):
    sequence = dna_strings.fetch(sequences[i])
    gc_perc = calc_gc_perc(sequence, i)
    if gc_perc > max_gc_perc:
        max_gc_perc = gc_perc
        max_gc_seq = sequences[i]

print(max_gc_seq)
print(max_gc_perc)
