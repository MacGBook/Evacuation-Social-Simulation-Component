# Evacuation-Social-Simulation-Component

# INSTRUCTIONS & TUTORIAL 

(1) Begin by downloading and installing the desktop version of Ollama for your computer: https://ollama.com/download

(2) Once downloaded, open Ollama. There should be a dropdown menue with a number of LLM models you can use. Click on one to download that model. I reccomend starting with gemma3:1b as that is currently what the program is confirgured to. 

(3) Once that model version is downloaded, feild Ollama a general question like "what color is the sky" to get it running and make sure it is working. Keep the desktop app open while you run the following code for best and fastest results. 

(4) Open your terminal and CD into the file that the code is stored in (i.e. Evacuation-Social-Simulation-Component-mark_1 wherever it is located on your device or tied to Github).

(5) Run the command: python main.py . This should run the initial default version of the program. Don't be alarmed if this takes 1-3 minutes to load as there are multiple LLM calls involved. 

(6) There will not be a print out in the terminal once this run is complete (as of now). All results and data will be directly written to the ind_ag_output.csv file and the total_output.csv file. You can check it there. Note: each run will overwrite prior run data, so make sure to save a copy if needed. 

# CHANGING THE EVACUATION MESSAGE

You can edit the evacuation message to say whatever you want by directly editing the string in evac_mess.py. 

# CHANGING THE CURRENT LLM MODEL

You can change to using a different LLM model by directly changing the string title of the model in curr_mod.py. 

# SEEING THE AGENT RESPONSES

To see the agent responses being generated, do the following:
(1) At the bottom of the code in agents.py, add the following print statement: print(agent_response_dict) .
(2) run the following command in the terminal: python agents.py 
(3) This should print out agent responses (that are being evaluated by the system) in the terminal for you to view.

# CHANGING THE AGENT PROMPTS

Each of the 30 default agents has a core personality prompt (ex: agent_11_description). Feel free to alter these prompts and see how results change. 

# IMPROVEMENTS TO COME WITH MARK 2
(1) Refining individual agent prompts 
(2) Allowing user to specify what type of warning agents are receiving (WEA, flood warning, tornado warning)\
(3) Allow user to set the total number of runs they want to complete and save multiple runs to CSV
(4) Improving efficiency of multiple runs 
