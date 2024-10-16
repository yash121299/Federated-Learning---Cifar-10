
import csv
import pickle

def main():
    # Specify the file path to your pickle file
    file_path = 'aggregate_metric_list.pkl'

    # Open the file in binary read mode and load the dictionary
    with open(file_path, 'rb') as file:
        loaded_list = pickle.load(file)

    # Now, `loaded_dict` contains the dictionary from the pickle file

    number_of_rounds = len(loaded_list)

    # Specify the file name
    filename = 'test.csv'

    # Writing to CSV
    average_accuracy_list = []
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = [''] + [f'Round {i}' for i in range(1, number_of_rounds + 1)]
        # Writing the data
        writer.writerow(header)
        for round_number in range(number_of_rounds):
            # row = [client] + loaded_dict[client]
            # writer.writerow(row)
            current_accuracy_value = loaded_list[round_number]['loss']
            average_accuracy_list.append(current_accuracy_value)
        row = ['Average Loss'] + average_accuracy_list
        writer.writerow(row)
            #current_accuracy_list.clear()

    print(f'{filename} created successfully.')


if __name__ == '__main__':
    main()


