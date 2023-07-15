
# Progress Journal 


**Week 1** 

- *May 29th - 31st*
  - Documented the structure of A1 [cfg.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/cfg.py) [(here)](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/A1%20'cfg.py'%20description.md), A1 [netParams.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/netParams.py) [(here)](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/A1%20'netParams.py'%20description.md) 
and A1 [batch.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/batch.py) [(here)](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/A1%20'batch.py'%20description.md).
  - First official meeting to establish next steps : running a scaled batch script, setting up virtual machine on Google Cloud and running the batch script on the VM.

- *June 1st, 2nd*
	 - ran multicore sim of [tutorial 8](http://www.netpyne.org/tutorial.html#tutorial-8-running-batch-simulations) batch.py on terminal 
   - created 3x3 batch script for CA3 model, see [here](https://github.com/irenebernardi/GSoC2023/blob/main/CA3dev/CA3batch.py)
   - ran multicore sim of 3x3 batch.py of CA3 model on terminal, issues documented [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/batch%20simulation%20errors.md) and [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/multicore%20simulation%20errors.md)
   - Set up UBUNTU Virtual Machine on Google Cloud and downloaded NEURON and NetPyNE related packages, MPI, etc. 

**Week 2**

- *June 5th - 7th*
  - issues with SSH keypair on VM   
  - meeting on useful LINUX commands, VM goals for the next week, SSH keypair issues

- *June 8th, 9th*
	- figured out SSH keypair on VM, see [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/Issues%20generating%20SSH%20keypair%20for%20Google%20Cloud%20VM.md)


**Week 3**

- *June 12th - 14th*
  - ran [init_demo.py](https://github.com/NathanKlineInstitute/Macaque_auditory_thalamocortical_model_data/blob/main/model/init_demo.py) and [CA3 batch.py](https://github.com/irenebernardi/GSoC2023/blob/main/CA3dev/CA3batch.py) on VM.

- *June 15th - 16th*
  - meeting on VSC remote extension (see [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/Issues%20generating%20SSH%20keypair%20for%20Google%20Cloud%20VM.md)) , mods compiling issues on VM and .err files in batch output.

 
**Week 3**

 - *June 19th - 21st*
   - fixed mods issues on VM (see [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/multicore%20simulation%20errors.md))
   - still had issues in batch.py output (.err files), partial solutions [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/batch%20simulation%20errors.md)
  - made a [.md file](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/SCZparameters.md) with details of the SCZ params we'll sweep

 - *June 22nd - 23rd*
   - meeting on batch `.err` files, Git file management, `createSimulateAnalyze`  function specifics

**Week 4**

 - *June 26th*
   - worked on Git file management, read relevant literature on mismatch negativity (MMN), stimulus specific adaptation (SSA) and deviant detection (DD) ([see here](https://docs.google.com/document/d/14AhPRCchy3o4aSPvPBy1iNlrdFQQm5be9c9O2lXk7a4/edit)).
 - *June 27th*
   - lab meeting on future steps to take for A1 batch, as per [this](https://docs.google.com/document/d/14AhPRCchy3o4aSPvPBy1iNlrdFQQm5be9c9O2lXk7a4/edit) document. Goals: reproducing EEG ERPs in control and in SCZ on HPC. 
 - *June 28th, 29th, 30th*
   - learned how to use NSG San Diego portal and how to run tasks on zipped data
   - tried fixing `.err` files when running CA3batch.py 


**Week 5**
 - *July 3rd, 4th, 5th*
  - tried to figure out batch  `.err` files output on NSG San Diego HPC.
  - meeting on batch `.err` files, mod compilation issues causing them and how to fix them. Exact steps described [here](https://github.com/irenebernardi/GSoC2023/blob/main/batchcommands_order.md) 

 - *July 6th, 7th*
  - made sure CA3 batch file ran correctly on Google Cloud VM
  - started [Shell Script tutorial](https://www.shellscript.sh), relevant to use Downstate HPC 
  - collaboratively worked on IP address issues for Downstate HPC access

**Week 6**
 - *July 10th, 11th*
  - finished Shell Script tutorial
  - issues due to `git` tracking unwanted files on my computer, documented [here](https://github.com/irenebernardi/GSoC2023/blob/main/documenting_issues/gitstatus_issues.md)
 - *July 12th, 13th, 14th*
  - meeting on how to setup Downstate HPC as per [instructions](https://docs.google.com/document/d/1VwjgOICa2Pj7pE_TODhQCaztmP07qi_C-pSCzCQ5o38/edit#heading=h.cabvm0d2hgwb)
  - learned more about branches/patch files and best practices for my dev files on GitHub -> TBD whether patch files is a good strategy 
  - worked on SSH issues for Downstate HPC -> TODO: make separate file once Scott gets back and things are clear


**Week 7**
- init.py issues 