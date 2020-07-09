import torch 
from torch import nn

# Model Definition
class Net(nn.Module):
    
    def __init__(self, hyper_params):
        super(Net, self).__init__()

        
        # Attr.
        self.inputSize = hyper_params['input_size']
        self.numHidden = len(hyper_params['hidden_size'])
        self.hiddenSize = hyper_params['hidden_size']
        self.outputSize = hyper_params['output_size']
        self.dropOut = hyper_params['drop_out']
        
        
        # Define input + hidden layers
        self.layers = nn.ModuleList()
        
        for i in range(self.numHidden):
            if i == 0:
                self.layers.append(nn.Linear(self.inputSize, self.hiddenSize[i]))
            else:
                self.layers.append(nn.Linear(self.hiddenSize[i-1], self.hiddenSize[i]))
        
        # Define output layer
        self.outputLayer = nn.Linear(self.hiddenSize[-1], self.outputSize)
        
        # Activations & Regulation
        self.reLU = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
        
        # Regulation
        self.dropOut = nn.Dropout(p=self.dropOut)
        
        # init weights and biases
        nn.init.xavier_uniform_(self.outputLayer.weight)       
        nn.init.zeros_(self.outputLayer.bias)
        for layer in self.layers:
            nn.init.xavier_uniform_(layer.weight)
            nn.init.zeros_(layer.bias)

            
    def forward(self, x):
        
        
        # Hidden layers
        for layer in self.layers:
            x = self.dropOut( self.reLU( layer(x) ))
    
        # Output
        x = self.softmax(self.outputLayer(x))
        
        return x  

    