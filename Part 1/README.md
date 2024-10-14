# Federated Learning Data Poisoning Project

1. Install the dependencies using the following command:
    pip install -r requirements.txt

2. Run the partitiondata.py file using the following command:
    python partiondata.py
    This will create a directory called federated_clients_data which will contain the original dataset split into multiple clients 
    and their corresponding labels.
    The file will also apply the data augmentations before splitting the data into clients

3. Run poisonclient.py file using the following command:
    python poisonclient.py
    Specify the number of clients to poison in the poisonclient.py file before running the file
    This will create a poisoned_clients_data directory which will have the speciefied clients with their data labels flipped