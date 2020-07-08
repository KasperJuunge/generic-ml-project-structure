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
        
    def _snapshot(self, file_path, snapshot_path):

        if os.path.isfile(file_path):

            # Read file
            with open(file_path, 'r') as file:
                src = file.read()

            # Save file
            f = open(snapshot_path, 'w')
            f.write(src)
            f.close()
            return src
        else:
            print(f'Trying to snapshot file, but can not find path: {file_path}')
            return 

    
    def _snapshotAll(self):

        cwd = os.getcwd()
        
        if not os.path.isdir(f'{cwd}/runs'):
            os.mkdir(f'{cwd}/runs')
        
        if not os.path.isdir(f'{cwd}/runs/{self.modelName}'):
            os.mkdir(f'{cwd}/runs/{self.modelName}')
        
        if not os.path.isdir(f'{cwd}/runs/{self.modelName}/src'):
            os.mkdir(f'{cwd}/runs/{self.modelName}/src')

        
        # Snapshot code
        self.trainNotebook = self._snapshot(file_path='./train.ipynb', 
                                            snapshot_path=f'./runs/{self.modelName}/src/train.ipynb')
        
        self.createDatasetNotebook = self._snapshot(file_path='./create_dataset.ipynb', 
                                                    snapshot_path=f'./data/datasets/{self.datasetName}/create_dataset.ipynb')
        
        self.datasetClass = self._snapshot(file_path='./classes/dataset.py', 
                                           snapshot_path=f'./runs/{self.modelName}/src/dataset.py')
        
        self.earlyStopperClass = self._snapshot(file_path='./classes/earlystopper.py', 
                                                snapshot_path=f'./runs/{self.modelName}/src/earlystopper.py')
        
        self.modelClass = self._snapshot(file_path='./classes/model.py', 
                                         snapshot_path=f'./runs/{self.modelName}/src/model.py')
        
        
        self.modelVersionClass = self._snapshot(file_path='./classes/model_version.py', 
                                                snapshot_path=f'./runs/{self.modelName}/src/model_version.py')
        
        self.functions = self._snapshot(file_path='./classes/functions.py', 
                                        snapshot_path=f'./runs/{self.modelName}/src/functions.py')

        
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

                  
