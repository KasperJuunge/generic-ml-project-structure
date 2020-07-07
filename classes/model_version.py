import os


class ModelVersion():
    def __init__(self, hyper_params):
        
        # Model and dataset name
        self.modelName = hyper_params['model_name']
        self.datasetName = hyper_params['dataset_name']
        
        # Hyper parameters
        self.hyperParameters = hyper_params
        
        # Performance
        self.acc = {'train': [], 'val': []}
        self.loss = {'train': [], 'val': []}
        
         # Src
        self.trainNotebook = None
        self.createDatasetNotebook = None
        self.modelClass = None
        self.datasetClass = None
        self.modelVersionClass = None
        self.functions = None
        
        self._snapshotAll()
        
        
    def _snapshot(self, path):
        

        
        if os.path.isfile(path):
            
            # Read file
            with open(path, 'r') as file:
                src = file.read()
           
            # Save file
            file_name = path.split('/')[-1]         
            f = open(f'runs/{self.modelName}/src/{file_name}', 'w')
            f.write(src)
            f.close()
            return src
        else:
            print(f'Trying to snapshot file, but can not find path: {path}')
            return 
        
        
    def _snapshotAll(self):

        cwd = os.getcwd()
        
        if not os.path.isdir(f'{cwd}/runs'):
            os.mkdir(f'{cwd}/runs')
        
        if not os.path.isdir(f'{cwd}/runs/{self.modelName}'):
            os.mkdir(f'{cwd}/runs/{self.modelName}')
        
        if not os.path.isdir(f'{cwd}/runs/{self.modelName}/src'):
            os.mkdir(f'{cwd}/runs/{self.modelName}/src')
        
        self.trainNotebook = self._snapshot(path=f'{cwd}/train.ipynb')
        self.createDatasetNotebook = self._snapshot(path=f'{cwd}/data/datasets/{self.datasetName}/create_dataset.ipynb')
        self.datasetClass = self._snapshot(path=f'{cwd}/classes/dataset.py')
        self.earlyStopperClass = self._snapshot(path=f'{cwd}/classes/earlystopper.py')
        self.modelClass = self._snapshot(path=f'{cwd}/classes/model.py')
        self.modelVersionClass = self._snapshot(path=f'{cwd}/classes/model_version.py')
        self.functions = self._snapshot(path=f'{cwd}/functions.py')

        
    def report(self):
        print('#~~~ VERSION REPORT FOR: {} ~~~#\n'.format(self.modelName))

        for key in self.hyperParameters:
            print('{}: {}'.format(key, self.hyperParameters[key]))
        
        if not self.acc['val'] == []:
            print('\nPerformance')
            print('Train accuracy: {0:.4f}'.format(max(self.acc['train'])))
            print('Train loss:     {0:.4f}'.format(min(self.loss['train'])))
            print('Val accuracy:   {0:.4f}'.format(max(self.acc['val'])))
            print('val loss:       {0:.4f}'.format(min(self.loss['val'])))
        else:
            print('\nNo accuracy and loss available.')

                  
