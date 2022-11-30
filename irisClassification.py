import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

class IrisClassifier(object):
    
    def __init__(self, data):
        '''
        Initialize IrisClassifier object with a Pandas dataframe that includes data on Irises
        Args: 
            data: a Pandas dataframe
        Returns:
            None
        '''
        # exception handling: make sure entered data is a Pandas dataframe
        # if it is, then save data into a new dataframe self.data
        if isinstance(data, pd.DataFrame):
            self.irises = data
        # otherwise, raise a TypeError
        else:
            raise TypeError("Data is not and must be a Pandas dataframe.")
    
    
    def decision_tree(PetalWidthCm,PetalLengthCm):
    '''
    Predicts type of Iris using petal width and length in cm.
    Args: 
        PetalWidthCm: a float
        PetalLengthCm: a float
    Returns: 
        A string that is the predicted Iris species.
    '''
    if (type(PetalWidthCm) not in [float, int] or type(PetalLengthCm) not in [float, int]):
        raise TypeError("This function is designed to work only with floats or ints")
    if PetalWidthCm < 0.8:
        return "setosa"
    else:
        if PetalWidthCm > 1.75:
            return "virginica"
        elif PetalLengthCm <= 4.95:
            return "versicolor"
        else:
            return "virginica"
    
    
    def summary_table(self, group_cols, value_cols):
        # exception handling: make sure elements in group_cols and value_cols are
        # present in self.irises
        return self.irises.groupby(group_cols)[value_cols].aggregate([np.mean, np.std])
    
    
    def visualize_hist(df_species, x_axis):
    '''
    Function that plots a histogram showing all the species and user-inputted parameter for x-axis
        Args: User inputs string which is one of the four column values given in the dataframe
        Outputs: histogram with all species shown and user-inputted parameter for x-axis
    '''
        #check to make sure user inputted one of the columns in the dataframe
        if x_axis in ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]:
            #graph the histogram grouped by species and with x-axis values given by user input
            #pivot creates reshaped dataframe, setting "Species" equal to columns makes three columns with species names
            #the new dataframe will have values in each cell that correspond with the columns of the original dataframe  
            #plot.hist is used to plot this reshaped dataframe
            df_species.pivot(columns = "Species", values = x_axis).plot.hist(bins = 25, alpha = 0.5)
            #show the histogram
            plt.show()
            #if user inputted string that is not a column name, output error message
        else:
            print("The column you inputted does not exist. Please input one of the following columns:\n'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' for the x axis.")
            #exit the program 
            sys.exit(0)
    
    
    def visualize_scatter(self, x, y, color=["blue", "green", "red"]):
        '''
        Create and plot a scatterplot of different features of Irises that color codes points 
        based on the species of the Iris. Plot y vs x. 
        Args:
            x: a column of the Iris dataframe
            y: another column of the Iris dataframe
            color: a list containing 3 string elements that are color names
        Returns:
            None, just outputs the scatterplot created
        '''
        # create an empty plot with a single axis
        fig, ax = plt.subplots()
        fig.set_size_inches(13, 7) # adjust the length and width of plot
        
        # define a dict colors, which assigns element 0 in the color list to the "setosa" iris
        # assigns element 1 in the color list to the "versicolor" iris
        # and assigns element 2 in the color list to the "virginica" iris
        # this will be used to color code the points of the scatterplot by species
        colors = {"setosa":color[0], "versicolor":color[1], "virginica":color[2]}
        
        # for every species in the irises dataframe, and for every smaller dataframe containing
        # data on just that species
        # plot column x of that dataframe against column y
        # pass in the species name as the label for that plot, and set the color of the 
        # points corresponding to the species name
        for species, df_species in self.irises.groupby(["Species"]):
            ax.scatter(df_species[x], df_species[y], label=species, facecolor=colors[species])
        
        # show the legend indicating which color corresponds to which species on the plot
        ax.legend()
    
    
    def max_min(self, species, feature):
        accepted_inputs = {"setosa", "versicolor", "virginica"}
        if species in accepted_inputs:
            bool_idx = iris["Species"] == species # creates boolean array for which rows match user's inputted genre
            species_info = iris[bool_idx] # rows containing info only from selected genre
            species_feature_info = species_info[feature] # gets information on selected genre for a specific feature of data
            min_feature = min(species_feature_info) # minimum value of the feature for selected genre
            max_feature = max(species_feature_info) # max value of the feature for selected genre
            print(f"\nThe min {feature} for {species} is {min_feature}.\n \nThe max {feature} for {species} is {max_feature}.\n")
        else:
            raise Exception("Species user input must be in the species column of the iris dataframe." )
    

    
def computerDecisionTree():
    pass
