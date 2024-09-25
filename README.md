# 325Project1
First phase of a semester long project for CS325 Software Engineering.

This first phase includes a basic python script that reads an input file (input.txt) for prompts, processes said prompts to the phi3.5 model, then outputs the responses in an outputfile(output.txt).

Before attempting any further steps, install ollama on your local machine along with the phi3.5 model [here](https://ollama.com/ "Ollama Homepage")

In order to properly run this script, see the requirements.yaml file and create a conda environment using the following command: **conda env create -f requirements.yaml**

Alternatively, if you want to change the name of your environment use this command: **conda env create -f requirements.yaml -n <env_name>**

Once this is completed, activate the environment using: **conda activae <env_name>**

From here, insert your prompts into the input.txt file (there are some example prompts to show the format) then run the script and after the it finishes, check your output file for a saved record of the phi3.5 responses.

