# Iris Species Classification 

## Contributors:
-Alexis Pendleton
-Andrew Dorado
-Neira Ibrahimovic
-Lillian Gabrelian
### Project Goal: 
The goal of our project is to classify the iris data set and create a model that takes in measurements as parameters and outputs the correct iris flower classification. 
We use graphs to explore the data and aid us in creating a decision tree, then compare the decision tree we create to a computer-generated decision tree.
We intend to optimize the accuracy of our model so we could predict the correct flower with >90% accuracy.

### Background and source of dataset: -Alexis
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:

  - Id: entry number of the flower
  - SepalLengthCm: Length of the sepal (in cm)
  - SepalWidthCm: Width of the sepal (in cm)
  - PetalLengthCm: Length of the petal (in cm)
  - PetalWidthCm: Width of the petal (in cm)
  - Species: Iris species name

It should be noted that our group dropped the Id column in this data set and changed the species names to "versicolor", "setosa", and "virginica".
  
### Python packages used:
  - numpy 1.21.5
  - matplotlib 3.5.1
  - pandas 1.4.2
  - sklearn 1.0.2
  - sys 3.9.12
### Demo File Description:
We suggest having Anaconda installed on your computer to be able to most easily run our project. Also, please make sure that all of the packages, in the versions that we’ve specified above, are also downloaded on your computer. To run our demo file, download all of the files in this git repository as a .zip file. Then, on your computer, unzip the files into a folder. Once you’ve done this, open Demo_IrisSpeciesClassification.ipynb with JupyterLab or JupyterNotebook and run all of the cells in the file to see how our program works!
 
We imported the iris dataframe from the provided 'iris.csv' file as a pandas dataframe.
    
The first step was exploring the data using scatterplots and histograms. 
We created a function in our class for visualizing both the scatterplots and histograms. 
We first looked at a scatterplot showing the relationship between petal length and petal width for all three flower species.
We observed that setosa had the smallest petal length and width, virginica generally had the largest, and versicolor had 
petal length/widths that was mostly between the other two species. 

Next, we looked at a scatterplot showing the relationship between sepal length and sepal width for the three iris species. 
We were not able to find a way to distinguish the species from one another from this scatter plot, as there was a lot of overlap
between the species. 

We then looked at graphs showing the petal length, petal width, sepal length, and sepal width, plotted by species, 
so we could observe trends that differ between the species. 
After that, we further explored our data with histograms. 
When looking at the histograms for sepal length and sepal width, we found there was a lot of overlap
among the species, so the species were not easily distinguishable using these measurements. 
Therefore, we decided that these measurements would not be the most useful when creating our own decision tree. 
On the other hand, when we observed the histograms for petal length and petal width, we found that the three species       
were easily distinguishable from each other, so these measurements could be used to differentiate between the species. 

In order to estimate the bounds for the decision tree, two summary plots were made: one on sepal dimensions and the other on petal dimensions. 
We found that there was significant overlap in the sepal dimensions for the three species. On the other hand, the three species had distinct
proportions for petal dimensions. Setosas had very small petals, versicolors had medium sized petals, and virginicas had very large petals.
These means were the basis of our decision tree.

The second step was creating our own decision tree. -Andrew
   
Our decision tree code is a class method of. It takes in floats or ints, and it will raise type errors if a different data type is inputted. 
Because setosas were much smaller than the other two species, the first if statement checks if the petal length is less than 0.8 cm, which
is greater than the maximum length, and returns 'setosa' if true. Then it differentiates between virginica and versicolors by petal widths.

    
 max_min function -Alexis
 Then we compared our decision tree to the computer generated tree. -Alexis
### Scope and Limitations: -Andrew
The dataset used is very small and only provides 150 samples' data. Because of this small dataset, it can not be seen as statistically significant data.
    
### References and Acknowledgement: -Andrew
  -Professor Lectures
  -Discussion Sheets
g
