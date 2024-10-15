import pickle

# Specify the file path to your pickle file
file_path = 'accuracy_per_client_per_round.pkl'

# Open the file in binary read mode and load the dictionary
with open(file_path, 'rb') as file:
    loaded_dict = pickle.load(file)

# Now, `loaded_dict` contains the dictionary from the pickle file
print(loaded_dict)