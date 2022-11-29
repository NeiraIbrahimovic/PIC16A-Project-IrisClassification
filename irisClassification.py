import pandas as pd
import numpy as np

class IrisClassifier(object):
    
    def __init__(self, data):
        # exception handling: make sure entered data is a string that ends in .csv (or a link)
        self.data = data
    
    def read_csv(self):
        self.irises = pd.read_csv(self.data)
        return self.irises
    
    def decision_tree(self, energy, instrumentalness, danceability, speechiness, loudness, liveness, popularity, acousticness, valence):
        # exception handling: make sure correct value types entered
        # predict classical if low energy
        if energy < 0.42:
            return "Classical"
        # predict hiphop or rock
        elif danceability > 0.58 and popularity > 50:
            return "Hip-hop"
        
        pass
    
    def summary_table(self, group_cols, value_cols):
        # exception handling: make sure elements in group_cols and value_cols are
        # present in self.genres
        return self.irises.groupby(group_cols)[value_cols].aggregate([np.mean, np.std])
    
    def visualize_hist(self):
        pass
    
    def visualize_scatter(self):
        pass
    
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
