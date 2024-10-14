import numpy as np
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset
import os



def split_data(dataset, num_clients, deviation_factor=0.1):
    """
    Splits data across clients with slight deviation
    """
    client_indices = {i: [] for i in range(num_clients)}

    # Split indices based on classes
    for class_idx in range(10):  
        class_indices = np.where(np.array(dataset.targets) == class_idx)[0]
        np.random.shuffle(class_indices)
        
        # Calculate the number of samples
        total_samples = len(class_indices)
        avg_samples_per_client = total_samples // num_clients
        
        
        splits = []
        remaining_samples = total_samples
        for client in range(num_clients):
            # Apply deviation to the average samples
            deviation = np.random.randint(-int(avg_samples_per_client * deviation_factor), 
                                          int(avg_samples_per_client * deviation_factor) + 1)
            client_sample_count = avg_samples_per_client + deviation
            
            if client == num_clients - 1:
                client_sample_count = remaining_samples
            else:
                client_sample_count = min(client_sample_count, remaining_samples)
            
            remaining_samples -= client_sample_count
            splits.append(client_sample_count)
        
        split_class_indices = np.split(class_indices, np.cumsum(splits[:-1]))

        for client, indices in enumerate(split_class_indices):
            client_indices[client].extend(indices)

    return client_indices



# Function to save client data as jpg
def save_client_data_as_jpg(dataset, indices, client_dir, client_id):
    client_path = os.path.join(client_dir, f'client_{client_id}')
    os.makedirs(client_path, exist_ok=True)

    
    for idx in indices:
        img, label = dataset[idx]
        label_folder = os.path.join(client_path, f'label_{label}')
        os.makedirs(label_folder, exist_ok=True)

        # Save the image as a .jpg
        img_path = os.path.join(label_folder, f'{idx}.jpg')

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(img_path)





def main():
    transform = transforms.Compose([
                                transforms.RandomHorizontalFlip(p=0.3),
                                transforms.RandomApply([transforms.RandomRotation(10)], p=0.3),
                                transforms.RandomResizedCrop(32, scale=(0.8, 1.0)),
                                # transforms.RandomApply([transforms.GaussianBlur(kernel_size=(3, 3), sigma=(0.1, 2.0))], p=0.2),
                                transforms.ToTensor(),
                                # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)) 
                                ])

    train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

    num_clients = 10
    client_dir = './federated_clients_data/'

    # Spliting data for training and testing
    train_indices = split_data(train_dataset, num_clients, deviation_factor=0.2)
    test_indices = split_data(test_dataset, num_clients, deviation_factor=0.2)

    # Saving the  data for each client
    for client_id in range(num_clients):
        save_client_data_as_jpg(train_dataset, train_indices[client_id], client_dir, client_id)
        save_client_data_as_jpg(test_dataset, test_indices[client_id], client_dir, client_id)

    print(f"Data has been split and saved into '{client_dir}' for {num_clients} clients.")

if __name__ == '__main__':
    main()