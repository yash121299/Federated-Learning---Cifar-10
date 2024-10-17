# Federated Learning Data Poisoning Project

## Part 1 - Setting Up Dependencies and Data
1. Install the dependencies using the following command:
    pip install -r requirements.txt

2. Run the partitiondata.py file using the following command:
    python partiondata.py
    This will create a directory called federated_clients_data which will contain the original dataset split into multiple clients 
    and their corresponding labels.
    The file will also apply the data augmentations before splitting the data into clients


## Part 2.0 - Baseline Model
### The code for the baseline model can also be executed by running the notebook - "Project_Part_2_Baseline_Model.ipynb"
3.  Run the baseline_model.py file using the command - 
    python baseline_model.py
    The executed output is already present in the notebook.

## Part 2.1 - Simulating a Federated Learning Setup with 10 Clients

### The entire simulation can also be executed by running the notebook - "Project_Part_2_UnPoisoned_Federated_Learning.ipynb"
Note: Install Jupyter Notebook or use it online using the method specified at - https://jupyter.org/

3. Run the unpoisoned_simulation.py file using the command - 
    python unpoisoned_simulation.py
    Note: Make sure the federated_clients_data folder is in the same directory
    All the code is also present in "Project_Part_2_UnPoisoned_Federated_Learning.ipynb" with the outputs of the cells where you can the see the results and output of the simulation that we ran
    The code will generate 3 pickle files titled 'accuracy_per_client_per_round.pkl','loss_per_client_per_round.pkl','aggregate_metric_list.pkl'
4. The output for the metrics for the simulation would be displayed in the console and stored in the above mentioned pickle files.
    Verify that the files exist in the directory.
    In order to visualize the results, run the 'plots_accuracy_loss.py' file using the command - 
    python plots_accuracy_loss.py
    This will show the plots of each clients accuracy over rounds and loss over rounds
    Then run the 'plot_aggregate_plots.py' file using the command - 
    python plot_aggregate_plots.py
    This will show the plots for average accuracy and average loss over the rounds

## Part 2.2 - Simulating a Federated Learning Setup with 10 Clients and 1 Client poisoned with a Label Flipping Attack

### The entire simulation can also be executed by running the notebook - "Project_Part_2_Poisoned_Federated_Learning.ipynb"

5. Make sure that dataset exists in the directory 'federated_clients_data'
6. Run poisonclient.py file using the following command:
    python poisonclient.py
    Specify the number of clients to poison in the poisonclient.py file before running the file
    This will create a poisoned_clients_data directory which will have the speciefied clients with their data labels flipped
7. Move the poisoned client data to the dataset directory. Follow the following steps:
    1. Copy the folders inside 'poisoned_clients_data directory' and paste them inside the 'federated_clients_data' directory
    2. Delete the directories for the clients that we poisoned
        For Eg. If client 8 was poisoned, delete the directory 'client_8'
    3. You should have pasted the posioned data for that client in step 1. Just rename it to the directory you just deleted
        For Eg. If you just deleted 'client_8' in step 2, rename the 'poisoned_client_8' folder to 'client_8'
    4. Verify that the 'federated_clients_data' contains folders for all clients 0-9 and no other folders with different names
8. Run the poisoned_simulation.py file using the following command - 
    python poisoned_simulation.py 
    Note: Make sure the federated_clients_data folder is in the same directory
    All the code is also present in "Project_Part_2_Poisoned_Federated_Learning.ipynb" with the outputs of the cells where you can the see the results and output of the simulation that we ran
    The code will generate 3 pickle files titled 'poisoned_accuracy_per_client_per_round.pkl','poisoned_loss_per_client_per_round.pkl','poisoned_aggregate_metric_list.pkl'
9. The output for the metrics for the simulation would be displayed in the console and stored in the above mentioned pickle files.
    Verify that the files exist in the directory.
    Modify the file names in plots_accuracy_loss.py
    Set the file_path_accuracy to 'poisoned_accuracy_per_client_per_round.pkl'
    Set the file_path_loss to 'poisoned_loss_per_client_per_round.pkl' 
    In order to visualize the results, run the 'plots_accuracy_loss.py' file using the command - 
    python plots_accuracy_loss.py
    This will show the plots of each clients accuracy over rounds and loss over rounds
    In plots_aggregate_plots.py, set the aggregate_file_path to 'poisoned_aggregate_metric_list.pkl' 
    Then run the 'plots_aggregate_plots.py' file using the command - 
    python plot_aggregate_plots.py
    This will show the plots for average accuracy and average loss over the rounds
