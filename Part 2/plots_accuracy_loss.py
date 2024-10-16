import pickle
import matplotlib.pyplot as plt

# Specify the file path to your pickle file
file_path_accuracy = 'accuracy_per_client_per_round.pkl'
file_path_loss = 'loss_per_client_per_round.pkl'

# Open the file in binary read mode and load the dictionary
with open(file_path_accuracy, 'rb') as file:
    loaded_dict_accuracy = pickle.load(file)

with open(file_path_loss, 'rb') as file:
    loaded_dict_loss = pickle.load(file)

# Now, `loaded_dict` contains the dictionary from the pickle file
# print(loaded_dict)x

# Keys in the dictionary are the client ids.
# The values in the dictionary is a list containing the round number along with the accuracy
# The X-axis is the number of rounds.
# The Y-axis is the accuracy.
# Stores the clients in a list.
clients = []
for keys in loaded_dict_accuracy:
    clients.append(keys)

for i in range(len(clients)):
    list_of_values = loaded_dict_accuracy[clients[i]]
    round_on_x_axis = []
    accuracy_on_y_axis = []
    for j in range(len(list_of_values)):
        round_number, accuracy = list_of_values[j]
        round_on_x_axis.append(round_number)
        accuracy_on_y_axis.append(accuracy)

    plt.plot(round_on_x_axis, accuracy_on_y_axis)
    plt.xlabel('Rounds')
    plt.ylabel('Accuracy')
    plt.title(f'Client {clients[i]} Accuracy')
    plt.grid(True)
    plt.savefig(f'Client_{clients[i]}_Accuracy.png')
    plt.show()
    round_on_x_axis.clear()
    accuracy_on_y_axis.clear()


##################################

clients.clear()
clients = []
for keys in loaded_dict_loss:
    clients.append(keys)

for i in range(len(clients)):
    list_of_values = loaded_dict_loss[clients[i]]
    round_on_x_axis = []
    loss_on_y_axis = []
    for j in range(len(list_of_values)):
        round_number, loss = list_of_values[j]
        round_on_x_axis.append(round_number)
        loss_on_y_axis.append(loss)

    plt.plot(round_on_x_axis, loss_on_y_axis)
    plt.xlabel('Rounds')
    plt.ylabel('Loss')
    plt.title(f'Client {clients[i]} Loss')
    plt.grid(True)
    plt.savefig(f'Client_{clients[i]}_Loss.png')
    plt.show()
    round_on_x_axis.clear()
    loss_on_y_axis.clear()

