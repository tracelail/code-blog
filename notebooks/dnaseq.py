class DNASeq:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def __str__(self):
        """Returns a string representation of the DNA sequence."""
        return self.sequence

    def transcribe(self):
        return self.sequence.replace("T", "U")

    def reverse_complement(self):
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return "".join(complement[base] for base in reversed(self.sequence))

    @classmethod
    def from_rna(cls, rna_sequence):
        dna_sequence = rna_sequence.replace("U", "T")
        return cls(dna_sequence)
