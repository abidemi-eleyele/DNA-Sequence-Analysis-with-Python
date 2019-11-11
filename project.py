import sequence
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

Dna_sequence = sequence.Sequence ('AGCT', 'ABGX', 'ACGT', "genome_01.dat")
# Call the first_base method on our instance.
Dna_first_base = Dna_sequence.first_base ()
print (f'The first base is: {Dna_first_base}')

#print the total number of any bases inputed
Dna_all_bases = Dna_sequence.all_base ()
print (f'The number of base is: {Dna_all_bases}')

#Return the first different base by calling the method is_dna()
Dna_is_dna = Dna_sequence.is_dna ()
print (f'The base is: {Dna_is_dna}')

#print the complement of a base by calling method complement()
Dna_complement = Dna_sequence.complement ()
print (f'The complement base is : {Dna_complement}')

#print the first mismatch base with the index by calling method comparison()
Dna_comparison = Dna_sequence.comparison ()
print (f'The comparison is :{Dna_comparison}')

#task 6 dna_read_file function reads genome_01.dat file and print the total number of bases by calling method all_bases use before
def dna_read_file(filename):
    gene = []
    with open (filename, 'r') as gene_a:  # load the pulses dna file
        lines_1 = gene_a.readlines ()
        for line in lines_1:
            parts = line.split (',')
        gene.append (parts [0])
    genome_sequence = sequence.Sequence (parts [0], 'ACGT', 'ACTT', "genome_01.dat")
    all_bases = genome_sequence.all_base ()
    print (f'The total number of base is: {all_bases}')
# calling the function on the genome_01 file
dna_read_file ("genome_01.dat")

# split genome_01.dat into gene and return the first gene sequence
gene_sequence = Dna_sequence.split_gene ("genome_01.dat")
gene_new_sequence = sequence.Sequence (gene_sequence [0], 'ACGT', 'ACTT', "genome_01.dat")
print (f'First gene sequence is: {gene_sequence[0]}')

all_bases = gene_new_sequence.all_base ()
print (f'The total number of first gene sequence is: {all_bases}')

# histogram plot gene number against gene length
gene_histogram = Dna_sequence.genome_01 ("genome_01.dat")
plt.hist (gene_histogram)  # histogram plot of corrected list
plt.title ('Histogram of Gene sequence')
plt.ylabel ('Gene Number')
plt.xlabel ('Length of gene')
plt.savefig ('Gene Historgram plot.jpg')
plt.show ()

genome_01_and_genome_02_compare = Dna_sequence.DNA_comparison ("genome_01.dat", "genome_02.dat")

print (f'The DNA Compare difference is :{len (genome_01_and_genome_02_compare)}')
while (len (gene_histogram) < len (genome_01_and_genome_02_compare)):
    gene_histogram.append (0)# appended 0 so that it is possible to train in sklearn
print (len (genome_01_and_genome_02_compare))
print (len (gene_histogram))

#scatter plot of swap mutation per gene against gene length
plt.scatter(x=gene_histogram, y =genome_01_and_genome_02_compare)
plt.title('Scatter diagram')
plt.xlabel('Gene Length')
plt.ylabel('swap Gene mutation')
plt.savefig ('scatter plot1.jpg')
plt.show()

#Task 10
gene_X = np.array([gene_histogram])
Gene_X_transpose = gene_X.reshape(-1, 1)
Gene_y = np.array([genome_01_and_genome_02_compare])
Gene_y_transpose = Gene_y.reshape(-1, 1)
#splitting the data into testing and training data, where the test size was 20% of the whole data
X_train, X_test, y_train, y_test = train_test_split(Gene_X_transpose, Gene_y_transpose, test_size = 0.3)
regr = LinearRegression () # calling the linear regression model
regr.fit (X_train, y_train) # fit the train and test data of the data
print (regr.score (X_test, y_test))
print(regr.coef_)   # print the coefficient according to equation y = mx + c
print(regr.intercept_) # print the intercept

Gene_pred = regr.predict (X_test) # predicted swap gene mutation
# scatter plot of the predicted after fiting the line
plt.scatter (X_test, y_test, color='b')
plt.title('Scatter diagram with best fit line')
plt.xlabel('Gene Length')
plt.ylabel('swap Gene mutation')
plt.plot (X_test, Gene_pred, color='k')
plt.savefig ('scatter plot2.jpg')
plt.show ()




