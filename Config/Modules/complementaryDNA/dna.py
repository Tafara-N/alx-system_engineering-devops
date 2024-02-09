#!/usr/bin/python3

"""
A function that receives one side of the DNA and returns the complementary side.
"""


def dna_strand(dna):
    dna_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    strand = [dna_dict[nucleotide] for nucleotide in dna]

    return ''.join(strand)
