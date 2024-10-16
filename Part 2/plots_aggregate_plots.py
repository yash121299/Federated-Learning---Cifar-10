import pickle
import matplotlib.pyplot as plt

# Specify the file path to your pickle file
aggregate_file_path = 'aggregate_metric_list.pkl'


# Open the file in binary read mode and load the dictionary
with open(aggregate_file_path, 'rb') as file:
    loaded_aggregate_file = pickle.load(file)


accuracy_list = []
loss_list = []
rounds = []
for i in range(len(loaded_aggregate_file)):
    if 'accuracy' in loaded_aggregate_file[i]:
        val_accuracy = loaded_aggregate_file[i].get('accuracy')
        accuracy_list.append(val_accuracy)
    if 'loss' in loaded_aggregate_file[i]:
        val_loss = loaded_aggregate_file[i].get('loss')
        loss_list.append(val_loss)
    rounds.append(i+1)


plt.plot(rounds, accuracy_list)
plt.xlabel('Rounds')
plt.ylabel('Accuracy')
plt.title('Average_Evaluation_Accuracy_Among_Clients')
plt.grid(True)
plt.savefig('Average_Evaluation_Accuracy_Among_Clients.png')
plt.show()

plt.plot(rounds, loss_list)
plt.xlabel('Rounds')
plt.ylabel('Loss')
plt.title('Average_Evaluation_Loss_Among_Clients')
plt.grid(True)
plt.savefig('Average_Evaluation_Loss_Among_Clients.png')
plt.show()
