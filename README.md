# Iris Species Classification 

## Contributors:
    Alexis Pendleton
    Andrew Dorado
    Neira Ibrahimovic
    Lillian Gabrelian
### Project Goal: -Neira

### Background and source of dataset: -Alexis
  -Kaggle
  
### Python packages used: -Lillian
  - numpy 1.21.5
  - matplotlib 3.5.1
  - pandas 1.4.2
  - sklearn 1.0.2
  - sys 3.9.12
### Demo File Description:
    We imported the iris dataframe from the provided 'iris.csv' file as a pandas dataframe.
    
    The first step was exploring the data using scatterplots and histograms. 
    We created a function for visualizing both the scatterplots and histograms. 
    We first looked at a scatterplot showing the relationship between petal length and petal width for all three flower species.
    We observed that setosa had the smallest petal length and width, virginica generally had the largest, and versicolor had 
    petal length/widths that was mostly between the other two species. 
    
    Next, we looked at a scatterplot showing the relationship between sepal length and sepal width for the three iris species. 
    We were not able to find a way to distinguish the species from one another from this scatter plot, as there was a lot of overlap
    between the species. 
    
    We then looked at graphs showing the petal length, petal width, sepal length, and sepal width, plotted by species. After that, we looked at histograms.
  
    
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
