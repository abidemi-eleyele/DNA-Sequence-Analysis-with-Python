# Author - Abidemi Eleyele
# DNA-Sequence-Analysis-with-Python
The project analyse a DNA file given without the use of Biopython. The two DNA file has a seperator of 10A's and 10T's.

The code makes use of class called Sequence which contains all the method or instance in the sequence.py file 
The method is been called in the project.py file. 

The code starts by returning the first base of any inputed gene, returns the number of DNA bases, validates if all the characters or bases are valid DNA bases, returns the complement of a Gene Sequence, non matching gene pairs between two DNA file, returns a DNA sequence that do not contain a DNA seperator.

It also plots the histogram of gene length and returns swap gene mutation per gene between two DNA file and also plot the scatter diagram of the number of swap mutations per gene against gene length.

A linear regression model from sklearn was use to predict and fit any future swap gene mutation. The data was splitted intp testing and train and then fit on the scatter plot diagram.
