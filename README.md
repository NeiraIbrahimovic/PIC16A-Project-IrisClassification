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
    
    The first step was exploring the data using histogram and scatterplot. -Neira
    
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
    -small dataset
    -old
    
### References and Acknowledgement: -Andrew
  -Professor Lectures
  -Discussion Sheets
