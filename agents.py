
# SOCIAL SIMULATION AGENTS
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

#General
import json
import ollama

#SET CURRENT MODEL
from curr_mod import current_model

#SET EVAC MESSAGE
from evac_mess import evacuation_message

##############################################################################################################################################################################################################################################################################################################################################################
#LLM SET UP
# Ollama: function for basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

# Initialized list we will add generated agent responses to
agent_response_list = []

##############################################################################################################################################################################################################################################################################################################################################################
#AGENT FRAMEWORK AND INDIVIDUAL LLM FRAMEWORK

# AGENT 1
agent_1_description = "You are just a little guy. "
agent1_prompt = agent_1_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent1_response = generate_text(current_model, agent1_prompt)
agent_response_list.append(agent1_response)

# AGENT 2
agent_2_description = "You are just a little guy. "
agent2_prompt =  agent_2_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent2_response = generate_text(current_model, agent2_prompt)
agent_response_list.append(agent2_response)

# AGENT 3
agent_3_description = "You are just a little guy. "
agent3_prompt =  agent_3_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent3_response = generate_text(current_model, agent3_prompt)
agent_response_list.append(agent3_response)

# AGENT 4
agent_4_description = "You are just a little guy. "
agent4_prompt =  agent_4_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent4_response = generate_text(current_model, agent4_prompt)
agent_response_list.append(agent4_response)

# AGENT 5
agent_5_description = "You are just a little guy. "
agent5_prompt =  agent_5_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent5_response = generate_text(current_model, agent5_prompt)
agent_response_list.append(agent5_response)

# AGENT 6
agent_6_description = "You are just a little guy. "
agent6_prompt =  agent_6_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent6_response = generate_text(current_model, agent6_prompt)
agent_response_list.append(agent6_response)

# AGENT 7
agent_7_description = "You are just a little guy. "
agent7_prompt =  agent_7_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent7_response = generate_text(current_model, agent7_prompt)
agent_response_list.append(agent7_response)

# AGENT 8
agent_8_description = "You are just a little guy. "
agent8_prompt =  agent_8_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent8_response = generate_text(current_model, agent8_prompt)
agent_response_list.append(agent8_response)

# AGENT 9
agent_9_description = "You are just a little guy. "
agent9_prompt =  agent_9_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent9_response = generate_text(current_model, agent9_prompt)
agent_response_list.append(agent9_response)

# AGENT 10
agent_10_description = "You are just a little guy. "
agent10_prompt =  agent_10_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent10_response = generate_text(current_model, agent10_prompt)
agent_response_list.append(agent10_response)

# AGENT 11
agent_11_description = "You are just a little guy. "
agent11_prompt =  agent_11_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent11_response = generate_text(current_model, agent11_prompt)
agent_response_list.append(agent1_response)

# AGENT 12
agent_12_description = "You are just a little guy. "
agent12_prompt =  agent_12_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent12_response = generate_text(current_model, agent12_prompt)
agent_response_list.append(agent12_response)

# AGENT 13
agent_13_description = "You are just a little guy. "
agent13_prompt =  agent_13_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent13_response = generate_text(current_model, agent13_prompt)
agent_response_list.append(agent13_response)

# AGENT 14
agent_14_description = "You are just a little guy. "
agent14_prompt =  agent_14_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent14_response = generate_text(current_model, agent14_prompt)
agent_response_list.append(agent14_response)

# AGENT 15
agent_15_description = "You are just a little guy. "
agent15_prompt =  agent_15_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent15_response = generate_text(current_model, agent15_prompt)
agent_response_list.append(agent15_response)

# AGENT 16
agent_16_description = "You are just a little guy. "
agent16_prompt = agent_16_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent16_response = generate_text(current_model, agent16_prompt)
agent_response_list.append(agent16_response)

# AGENT 17
agent_17_description = "You are just a little guy. "
agent17_prompt =  agent_17_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent17_response = generate_text(current_model, agent17_prompt)
agent_response_list.append(agent17_response)

# AGENT 18
agent_18_description = "You are just a little guy. "
agent18_prompt =  agent_18_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent18_response = generate_text(current_model, agent18_prompt)
agent_response_list.append(agent18_response)

# AGENT 19
agent_19_description = "You are just a little guy. "
agent19_prompt =  agent_19_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent19_response = generate_text(current_model, agent19_prompt)
agent_response_list.append(agent19_response)

# AGENT 20
agent_20_description = "You are just a little guy. "
agent20_prompt =  agent_20_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent20_response = generate_text(current_model, agent20_prompt)
agent_response_list.append(agent20_response)

# AGENT 21
agent_21_description = "You are just a little guy. "
agent21_prompt =  agent_21_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent21_response = generate_text(current_model, agent21_prompt)
agent_response_list.append(agent21_response)

# AGENT 22
agent_22_description = "You are just a little guy. "
agent22_prompt =  agent_22_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent22_response = generate_text(current_model, agent22_prompt)
agent_response_list.append(agent22_response)

# AGENT 23
agent_23_description = "You are just a little guy. "
agent23_prompt =  agent_23_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent23_response = generate_text(current_model, agent23_prompt)
agent_response_list.append(agent23_response)

# AGENT 24
agent_24_description = "You are just a little guy. "
agent24_prompt =  agent_24_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent24_response = generate_text(current_model, agent24_prompt)
agent_response_list.append(agent24_response)

# AGENT 25
agent_25_description = "You are just a little guy. "
agent25_prompt =  agent_25_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent25_response = generate_text(current_model, agent25_prompt)
agent_response_list.append(agent25_response)

# AGENT 26
agent_26_description = "You are just a little guy. "
agent26_prompt =  agent_26_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent26_response = generate_text(current_model, agent26_prompt)
agent_response_list.append(agent26_response)

# AGENT 27
agent_27_description = "You are just a little guy. "
agent27_prompt =  agent_27_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent27_response = generate_text(current_model, agent27_prompt)
agent_response_list.append(agent27_response)

# AGENT 28
agent_28_description = "You are just a little guy. "
agent28_prompt =  agent_28_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent28_response = generate_text(current_model, agent28_prompt)
agent_response_list.append(agent28_response)

# AGENT 29
agent_29_description = "You are just a little guy. "
agent29_prompt =  agent_29_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent29_response = generate_text(current_model, agent29_prompt)
agent_response_list.append(agent29_response)

# AGENT 30
agent_30_description = "You are just a little guy. "
agent30_prompt =  agent_30_description + "You receive the following evacuation message on your phone as a wireless emergency alert: " + evacuation_message + "Describe your understanding of the situation in less than 500 characters. Also mention if you're going to evacuate or not."
agent30_response = generate_text(current_model, agent30_prompt)
agent_response_list.append(agent30_response)

##############################################################################################################################################################################################################################################################################################################################################################
# PREP AGENT RESPONSES 

cleaned_agent_response_list = []
for string in agent_response_list:
    new_string = string.replace('Generated text (gemma3:1b):', '')
    no_line_new_string = new_string.strip('\n')
    cleaned_agent_response_list.append(no_line_new_string)

agent_name_list = ['agent1', 'agent2', 'agent3', 'agent4', 'agent5', 'agent6', 'agent7', 'agent8', 'agent9', 'agent10', 'agent11', 'agent12', 'agent13', 'agent14', 'agent15', 'agent16', 'agent17', 'agent18', 'agent19', 'agent20', 'agent21', 'agent22', 'agent23', 'agent24', 'agent25', 'agent26', 'agent27', 'agent28', 'agent29', 'agent30']

agent_response_dict = dict(zip(agent_name_list, cleaned_agent_response_list))

#cleaned_agent_response_list = string list of all agent responses
#agent_name_list = the list of the agent
#agent_response_dict = dictionary with agent name as key and their generated response as the value