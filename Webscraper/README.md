# 325Project1
## STEP 1, PHI-3.5 Setup:
First phase of a semester long project for CS325 Software Engineering.

This first phase includes a basic python script that reads an input file (input.txt) for prompts, processes said prompts to the phi3.5 model, then outputs the responses in an outputfile(output.txt).

Before attempting any further steps, install ollama on your local machine along with the phi3.5 model [here](https://ollama.com/ "Ollama Homepage")

In order to properly run this script, see the requirements.yaml file and create a conda environment using the following command: **conda env create -f requirements.yaml**

Alternatively, if you want to change the name of your environment use this command: **conda env create -f requirements.yaml -n <env_name>**

Once this is completed, activate the environment using: **conda activae <env_name>**

From here, insert your prompts into the input.txt file (there are some example prompts to show the format) then run the script and after the it finishes, check your output file for a saved record of the phi3.5 responses.

## STEP 2, Steam game webscraping setup:
The second phase of this project is the implementation of a webscraper that parses the Steam store via the Steamworks api. 

If not done yet, please reference back to step 1 for cloning the python environment for this script to function correctly.

This webscraper is handled by grabbing inputs from an input file (scraperInputs.txt) where a user can input AppIDs. These AppIDs are in-house identification numbers that Steam uses to identify every individual application that is downloadable through the Steam store.

Note: There are 6 example pieces of software inside the scraperInputs.txt file. If you wish to change this or add your own games/software to this file, simply click **[This](https://steamdb.info/ "SteamDB Homepage")** link to access the SteamDB website. Here, you can simply type in the software you would like to parse and grab its associated AppID from the far left column.

Once you have inserted the software you would like to parse, run the webscraper.py file, this will create output files with the software's name inside of the **Reviews** directory.
