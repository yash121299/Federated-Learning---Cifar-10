
import csv
import pickle

def main():
    # Specify the file path to your pickle file
    file_path = 'loss_per_client_per_round.pkl'

    # Open the file in binary read mode and load the dictionary
    with open(file_path, 'rb') as file:
        loaded_dict = pickle.load(file)

    # Now, `loaded_dict` contains the dictionary from the pickle file


    client_numbers = list(loaded_dict.keys())
    client_numbers.sort()
    number_of_rounds = len(loaded_dict[client_numbers[0]])

    # Specify the file name
    filename = 'test.csv'

    # Writing to CSV
    current_accuracy_list = []
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['Client'] + [f'Round {i}' for i in range(1, number_of_rounds + 1)]
        # Writing the data
        writer.writerow(header)
        for client in client_numbers:
            # row = [client] + loaded_dict[client]
            # writer.writerow(row)
            for x in loaded_dict[client]:
                current_accuracy_list.append(x[1])
            row = [client] + current_accuracy_list
            writer.writerow(row)
            current_accuracy_list.clear()

    print(f'{filename} created successfully.')


if __name__ == '__main__':
    main()


