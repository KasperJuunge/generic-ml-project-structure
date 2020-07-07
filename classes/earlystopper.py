import copy
import torch
from os import getcwd

class EarlyStopper():
    def __init__(self, max_patience, model_name):
        
        self.modelName = model_name
        self.bestLoss = 1e9
        self.maxPatience = max_patience
        self.bestModel = None
        self.patience = 0
        
    def check_early_stop(self, loss, model, version):
        
        # CASE: Model better
        if loss < self.bestLoss:
            self.bestModel = copy.deepcopy(model)
            self.patience = 0
            self.bestLoss = loss

            # Save state dict and version object
            state_dict = model.state_dict()
            torch.save(state_dict, f'{getcwd()}/runs/{self.modelName}/state_dict.torch')
            torch.save(version, f'{getcwd()}/runs/{self.modelName}/version.torch')
            
            return self.patience > self.maxPatience
        
        # CASE: Model worse
        else:
            # Increment Patience
            self.patience += 1
            return self.patience > self.maxPatience

