**Correct order of commands to run before running a batch file**

- 1. remove any cache from previous batch runs with `rm -rf __pycache__`

- 2. remove x86_64 from previous batch runs with `rm -rf x86_64`

- 3. `cd` to mod folder

- 4. from inside mod folder, run `nrnivmodl`

- 5. `cd` outside of mod folder back to general folder

- 6. move `x86_64` outside of mod folder: `mv mod/x86_64 x86_64`

- 7. troubleshoot: run `python3 netParams.py`, `from netParams import netParams` . Use [pretty print](https://docs.python.org/3/library/pprint.html) for better visualization

- 8. run `python3 batch.py` (or with `mpiexec`)


Not running these in right order can create issues like `Intel MKL FATAL ERROR: Cannot load libmkl_intel_thread.1.dylib` in the .run files of a batch data folder / mod compilation issues in the output of `python3 batch.py`. 
