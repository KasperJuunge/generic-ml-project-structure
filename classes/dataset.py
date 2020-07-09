import torch
import os
from torch.utils import data


class Dataset(data.Dataset):
    def __init__(self, list_IDs, labels, partition, dataset_name):
        
        self.labels = labels
        self.listIDs = list_IDs
        self.partition = partition
        self.datasetName = dataset_name

    def __len__(self):
        return len(self.listIDs)

    def __getitem__(self, index):
                
        # Select sample
        ID = self.listIDs[index]

        # Load data and get label
        x = torch.load(f'/home/ec2-user/gitrepo/ebml-iptc-model/notebooks/data/datasets/{self.datasetName}/{self.partition}/{ID}')
        y = self.labels[ID]

        return x, y