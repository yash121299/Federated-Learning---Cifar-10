import os
import random
from PIL import Image

NUM_CLASSES = 10

def flip_label_per_image(original_label):
    available_labels = list(range(NUM_CLASSES))
    available_labels.remove(original_label)  
    new_label = random.choice(available_labels)  # Randomly select a new label from remaining labels
    return new_label

def poison_client_data_per_image(original_dir, poisoned_dir, num_clients_to_poison):

    os.makedirs(poisoned_dir, exist_ok=True)
    

    client_dirs = [d for d in os.listdir(original_dir) if d.startswith('client_')]
    
    # Selecting client to poison
    random.shuffle(client_dirs)
    clients_to_poison = client_dirs[:num_clients_to_poison]

    print(f"Poisoning the following clients: {clients_to_poison}")

    for client in clients_to_poison:

        client_path = os.path.join(original_dir, client)
        

        poisoned_client_path = os.path.join(poisoned_dir, f'poisoned_{client}')
        os.makedirs(poisoned_client_path, exist_ok=True)

        for label_folder in os.listdir(client_path):
            original_label_path = os.path.join(client_path, label_folder)

            if os.path.isdir(original_label_path):
                original_label = int(label_folder.split("_")[1])

                for img_file in os.listdir(original_label_path):
                    img_path = os.path.join(original_label_path, img_file)
                    
                    # Determine the new flipped label for this image
                    new_label = flip_label_per_image(original_label)

                    poisoned_label_path = os.path.join(poisoned_client_path, f'label_{new_label}')
                    os.makedirs(poisoned_label_path, exist_ok=True)

                    img = Image.open(img_path)
                    img.save(os.path.join(poisoned_label_path, img_file))

    print(f"Poisoning complete. Poisoned data saved in: {poisoned_dir}")


original_data_dir = './federated_clients_data' 
poisoned_data_dir = './poisoned_clients_data'   # new directory to save poisoned data
num_clients_to_poison = 1  # No of cleints to poison


poison_client_data_per_image(original_data_dir, poisoned_data_dir, num_clients_to_poison)