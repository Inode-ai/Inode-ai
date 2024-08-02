
This package includes helper scripts for interfacing your machine learning code with the IndoeAi.com  containerization code.



## How to implement

```
from inodeai import inodeai

# transform input data against your  model (or whatever you want)
# If an error occured please thwor an error message

def modify_data(inputdataPath,outputdataPath):
    
    # take data from inputdataPath
    # Transform that data data via your required model
    # to save data write outputdataPath
    # Return None if no error come.
    # return an error msg if any error ocuured .


please intialize your model or other thing before using wait_for_request

inodeai.wait_for_requests(process_data)

```



run via command line arguments

python test.py serve input.csv output.csv

usage: test.py [-h] {run} ...

options:
  -h, --help  show this help message and exit

subcommands:
  {run}       commands to choose from
    run       run this model once from the command line




