"""
#init.py when no batch is involved 
from netpyne import sim

cfg, netParams = sim.loadFromIndexFile('index.npjson')
sim.createSimulateAnalyze(netParams, cfg)

"""


"""
init.py

Starting script to run NetPyNE-based CA3 model.
"""

from netpyne import sim

#cfg, netParams = sim.loadFromIndexFile('index.npjson')
#sim.createSimulateAnalyze(netParams = netParams, cfg = cfg)

# read cfg and netParams from command line arguments if available; otherwise use default
#simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='/Users/irenebernardi/Desktop/GSoC_files/ca3model_3pops/cfg.py', #netParamsDefault='/Users/irenebernardi/Desktop/GSoC_files/ca3model_3pops/netParams.py')


#trying without path
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')



# Create network and run simulation
sim.createSimulateAnalyze(netParams, simConfig)


