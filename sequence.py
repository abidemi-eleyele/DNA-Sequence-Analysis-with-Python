# This file contains a class declaration Sequence and methods are been added as the need comes.
class Sequence:
    # This method is the initializer, it is called when creating (instantiating) an object (instance) of this class.
    def __init__(self, bases, dna1, dna2, namefile):
        # store the bases, input dna 1 and 2 and supplied gene file name as an attribute.
        self.bases = bases
        self.dna1 = dna1
        self.dna2 = dna2
        self.namefile = namefile

    # Task 1 it returns the first base.
    def first_base(self):
        result = self.bases [0]
        return result

    #task 2 - it returns the number of bases supplied
    def all_base(self):
        result_1 = self.bases [0:]
        return len (result_1)

    #task 3 - returns if all the input bases are valid Dna bases
    def is_dna(self):
        for i in self.bases:
            if i == 'A' or i == 'C' or i == 'G' or i == 'T':
                pass
            else:
                return False
        return True

    #task 4 - returns the complement of a base
    def complement(self):
        for i in self.bases:
            comp = self.bases.replace ('A', 't').replace ('T', 'a').replace ('C', 'g').replace ('G', 'c')
        return comp.upper ()

    #task 5 - returns the comparison between two bases and prints out the first dna mismatch between the pairs
    def comparison(self):
        if self.dna1 == self.dna2 or self.dna1 == '' and self.dna2 == '':
            return -1
        else:
            for i in range (len (self.dna1)):
                if self.dna1 [i] != self.dna2 [i]:
                    return i, self.dna1 [i], i, self.dna2 [i]

    # task 7 - split the genome file into gene using the with open function and prints out the gene which is part[0]
    def split_gene(self, filename):
        gene = []
        return_gene=[]
        current_index = 0
        with open (filename, 'r') as gene_a:  # load the pulses dna file
            lines_1 = gene_a.readlines ()
            for line in lines_1:
                parts = line.split (',')
            gene.append (parts [0])
            separator = "AAAAAAAAAATTTTTTTTTT"
            while ( parts[0].find (separator ,current_index , len(parts[0]) ) != -1):
                #using find function to find the seperator, store the index in current index increase it by the length of the seperator in other to jump to the next dna sequence and so on
                new_current_index =   parts [0].find (separator, current_index, len(parts[0]))
                gene_sequence = parts [0] [current_index:new_current_index + len(separator)]
                return_gene.append(gene_sequence)
                current_index = new_current_index + len(separator)
            return return_gene

#task 8 -
    def genome_01(self, filename):
        gene = []
        return_gene = []
        current_index = 0
        with open (filename, 'r') as gene_a:  # load the pulses dna file
            lines_1 = gene_a.readlines ()
            for line in lines_1:
                parts = line.split (',')
            gene.append (parts [0])
            separator = "AAAAAAAAAATTTTTTTTTT"
            while (parts [0].find (separator, current_index, len (parts [0])) != -1):
                new_current_index = parts [0].find (separator, current_index, len (parts [0]))
                gene_sequence = parts [0] [current_index:new_current_index + len (separator)]
                return_gene.append (len(gene_sequence))
                current_index = new_current_index + len (separator)
            return return_gene

#task 9 method DNA_comparison comparing two DNA file with different sequence together, print the different and total number
    def DNA_comparison(self, filename1, filename2):
        gene = []
        gene1 = []
        return_count = []
        count = 0
        with open (filename1, 'r') as gene_a:  # load the genome_01 file
            lines_1 = gene_a.readlines ()
            for line in lines_1:
                parts = line.split (',')
            gene.append (parts [0])

        with open (filename2, 'r') as gene_b:  # load the genome_02 file
            lines_2 = gene_b.readlines ()
            for line in lines_2:
                parts = line.split (',')
            gene1.append (parts [0])
# compare between the two gene file, print out the index and bases where they are diffrent and print the total count
            first_genome_file = gene[0]
            second_genome_file = gene1[0]
            for i in range (len (gene[0])):
                  if first_genome_file [i] != second_genome_file [i]:
                      print(i, first_genome_file [i], i, second_genome_file [i])
                      return_count.append(i)
                      count += 1
        return return_count