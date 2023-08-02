from netpyne import specs
from netpyne.batch import Batch
import os 

# Specify the folder path
A1_data_path = ('A1dev/A1_data')

os.makedirs('A1_data', exist_ok = True)

def batchA1():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['startTime'] = [1500]
        params['cfg.weightE'] = [0.6]
        params['cfg.weightI'] = [0.4]
        params['cfg.probE'] = [0.38]
        params['cfg.probI'] = [0.68]


        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py')

        
        # Set output folder, grid method (all param combinations), and run configuration
        
        b.batchLabel = 'batchA1'
        b.saveFolder = 'A1_data'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                                'script': 'init.py',
                                'skip': True}
        '''
        #for SGE cluster:
        b.batchLabel = 'tauWeight'
        b.saveFolder = 'tut8_data'
        b.method = 'grid'
        b.runCfg = {'type': 'hpc_sge',
                    'cores': 4,
                    'script': 'init.py',
                    'pre': 'tree',
                    'skip': True}
        '''

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        batchA1()