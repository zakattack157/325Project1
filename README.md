# 325Project1
## STEP 1, PHI-3.5 Setup:
First phase of a semester long project for CS325 Software Engineering.

This first phase includes a basic python script that reads an input file (input.txt) for prompts, processes said prompts to the phi3.5 model, then outputs the responses in an outputfile(output.txt).

Before attempting any further steps, install ollama on your local machine along with the phi3.5 model [here](https://ollama.com/ "Ollama Homepage")

In order to properly run this script, see the requirements.yaml file and create a conda environment using the following command: **conda env create -f requirements.yaml**

Alternatively, if you want to change the name of your environment use this command: **conda env create -f requirements.yaml -n <env_name>**

Once this is completed, activate the environment using: **conda activae <env_name>**


## STEP 2, Steam game webscraping setup:
The second phase of this project is the implementation of a webscraper that parses the Steam store via the Steamworks api. 

If not done yet, please reference back to step 1 for cloning the python environment for this script to function correctly.

This webscraper is handled by grabbing inputs from an input file (scraperInputs.txt) where a user can input AppIDs. These AppIDs are in-house identification numbers that Steam uses to identify every individual application that is downloadable through the Steam store.

Note: There are 6 example pieces of software inside the scraperInputs.txt file. If you wish to change this or add your own games/software to this file, simply click **[This](https://steamdb.info/ "SteamDB Homepage")** link to access the SteamDB website. Here, you can simply type in the software you would like to parse and grab its associated AppID from the far left column.

Once you have inserted the software you would like to parse, run the webscraper.py file, this will create output files with the software's name inside of the **Reviews** directory. (Do this by running python3 webscraper.py in your terminal)

(In order to be able to send the GET request to the Steam store pages, the requests python package is being implemented. If you would like to learn more about the requests package click **[here](https://pypi.org/project/requests/ "Requests Package Documentation")**)

## STEP 3, Running The Model and Viewing Output:
Now that the Webscraper and PHI3.5 model are both properly setup, it is time to run the files and get an output!

Starting out, make sure you have followed the steps outlined in STEP 2 so you have reviews from the steam store to give to the PHI model.

Now simply run python3 PHIreader.py in your terminal under the PHI3_Prompt_Feeder directory to start the model reading process. (NOTE: this can take a while depending on how many reviews you have set up to read!)

Once this has finished, all files can be viewed in the output.txt file under the PHI3_Prompt_Feeder directory. There is also a nice graph that shows how many positive, negative, or neutral reviews the model has found throughout the reviews.

## STEP 4(OPTIONAL), Testing:
If you would like to I have included a pytest file named PHIpytest.py in the PHI3_Prompt_Feeder directory that can be ran for unit testing!
