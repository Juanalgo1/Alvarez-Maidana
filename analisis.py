import pandas as pd
import matplotlib.pyplot as plt

path_file = "D:\\Juan\\UNSAM\\Matematica3\\Animales-Mate-III\\dataAnimales.csv"
dataframe = pd.read_csv(path_file) 

dict_species = {
    "Mountain Lion": 0,
    "Black Bear": 1,
    "Brown Bear": 2,
    "Polar Bear": 3,
    "Muskox": 4,    # Buey
    "Gray Wolf": 5,
    "Thinhorn Sheep": 6,
    "Mountain Goat": 7,
    "Bighorn Sheep": 8,
    "Caribou": 9,   # Reno
    "Pronghorn": 10, # Berrendo
    "White-tailed Deer": 11,
    "Moose": 12, # Alce
    "Mule Deer": 13,
    "Elk": 14  # Ciervo canadiense
}

dict_province_state = {
  'Alabama': 0, 'Alaska': 1, 'Alberta': 2, 'Arizona': 3, 'British Columbia': 4, 
  'California': 5, 'Colorado': 6, 'Florida': 7, 'Georgia': 8, 'Idaho': 9, 
  'Illinois': 10, 'Indiana': 11, 'Iowa': 12, 'Kansas': 13, 'Kentucky': 14, 
  'Maine': 15, 'Manitoba': 16, 'Minnesota': 17, 'Mississippi': 18, 'Missouri': 19, 
  'Montana': 20, 'Nebraska': 21, 'Nevada': 22, 'New Brunswick': 23, 'New Hampshire': 24, 
  'New Mexico': 25, 'New York': 26, 'Newfoundland': 27, 'North Carolina': 28, 'North Dakota': 29, 
  'Northwest Territories': 30, 'Nunavut': 31, 'Oklahoma': 32, 'Ontario': 33, 'Oregon': 34, 
  'Pennsylvania': 35, 'Quebec': 36, 'Saskatchewan': 37, 'South Dakota': 38, 'Texas': 39, 
  'Utah': 40, 'Vermont': 41, 'Virginia': 42, 'Washington': 43, 'Wyoming': 44, 'Yukon': 45
}

dict_srank = {
  'S1': 0, 'S2': 1, 'S2S3': 2, 'S3': 3, 'S3S4': 4, 'S4': 5, 'S5': 6, 'S5 ': 7
}

dict_classification = {
  'Carnivore': 0, 'Ungulate': 1
}

dict_sci = {
  'N': 0, 'Y': 1
}

dataframe["Species"] = dataframe["Species"].replace(
    dict_species.keys(),
    dict_species.values()
)

dataframe["Province/State"] = dataframe["Province/State"].replace(
    dict_province_state.keys(),
    dict_province_state.values()
)

dataframe["S Rank"] = dataframe["S Rank"].replace(
    dict_srank.keys(),
    dict_srank.values()
)

dataframe["Classification"] = dataframe["Classification"].replace(
    dict_classification.keys(),
    dict_classification.values()
)

dataframe["SCI"] = dataframe["SCI"].replace(
    dict_sci.keys(),
    dict_sci.values()
)

print(dataframe)