import pickle
import matplotlib.pyplot as plt

# Specify the file path to your pickle file
file_path_accuracy = 'poisoned_accuracy_per_client_per_round.pkl'
file_path_loss = 'poisoned_loss_per_client_per_round.pkl'

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
# For accuracy
clients = []
for keys in loaded_dict_accuracy:
    clients.append(keys)

for i in range(len(clients)):
    list_of_values = loaded_dict_accuracy[clients[i]]
    round_on_x_axis = []
    accuracy_on_y_axis = []

    for j in range(len(list_of_values)):
        round_number, accuracy = list_of_values[j]

        if clients[i] == "7" and round_number > 30:
            break

        round_on_x_axis.append(round_number)
        accuracy_on_y_axis.append(accuracy)

    plt.plot(round_on_x_axis, accuracy_on_y_axis)
    plt.xlabel('Rounds')
    plt.ylabel('Accuracy')

    if clients[i] == "7":
        plt.title(f'Poisoned Client {clients[i]} Accuracy')
    else:
        plt.title(f'Client {clients[i]} Accuracy')

    plt.grid(True)

    if clients[i] == "7":
        plt.savefig(f'Poisoned_Client_{clients[i]}_Accuracy.png')
    else:
        plt.savefig(f'Client_{clients[i]}_Accuracy.png')

    plt.show()
    round_on_x_axis.clear()
    accuracy_on_y_axis.clear()


##################################
# For loss
clients.clear()
clients = []
for keys in loaded_dict_loss:
    clients.append(keys)

for i in range(len(clients)):
    list_of_values = loaded_dict_loss[clients[i]]
    round_on_x_axis = []
    loss_on_y_axis = []

    # for j in range(len(list_of_values)):
    #     round_number, loss = list_of_values[j]
    #     round_on_x_axis.append(round_number)
    #     loss_on_y_axis.append(loss)

    for j in range(len(list_of_values)):
        round_number, accuracy = list_of_values[j]

        if clients[i] == "7" and round_number > 30:
            break

        round_on_x_axis.append(round_number)
        loss_on_y_axis.append(accuracy)

    plt.plot(round_on_x_axis, loss_on_y_axis)
    plt.xlabel('Rounds')
    plt.ylabel('Loss')

    if clients[i] == "7":
        plt.title(f'Poisoned_ Client {clients[i]} Loss')
    else:
        plt.title(f'Client {clients[i]} Loss')

    plt.grid(True)

    if clients[i] == "7":
        plt.savefig(f'Poisoned_Client_{clients[i]}_Loss.png')
    else:
        plt.savefig(f'Client_{clients[i]}_Loss.png')

    plt.show()
    round_on_x_axis.clear()
    loss_on_y_axis.clear()

