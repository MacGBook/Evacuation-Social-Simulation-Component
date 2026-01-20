
# Imports
import json
import ollama

# Current model being used
current_model = 'gemma3:1b'

# Ollama: Basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

agent_response_list = []

# AGENT 1

agent1_prompt = "What color is the sky? Answer in one word."
agent1_response = generate_text(current_model, agent1_prompt)

agent_response_list.append(agent1_response)

# AGENT 2

agent2_prompt = "What color is the sky? Answer in one word."
agent2_response = generate_text(current_model, agent2_prompt)

agent_response_list.append(agent2_response)

# AGENT 3

agent3_prompt = "What color is the sky? Answer in one word."
agent3_response = generate_text(current_model, agent3_prompt)

agent_response_list.append(agent3_response)

# AGENT 4

agent4_prompt = "What color is the sky? Answer in one word."
agent4_response = generate_text(current_model, agent4_prompt)

agent_response_list.append(agent4_response)

# AGENT 5

agent5_prompt = "What color is the sky? Answer in one word."
agent5_response = generate_text(current_model, agent5_prompt)

agent_response_list.append(agent5_response)

# AGENT 6

agent6_prompt = "What color is the sky? Answer in one word."
agent6_response = generate_text(current_model, agent6_prompt)

agent_response_list.append(agent6_response)

# AGENT 7

agent7_prompt = "What color is the sky? Answer in one word."
agent7_response = generate_text(current_model, agent7_prompt)

agent_response_list.append(agent7_response)

# AGENT 8

agent8_prompt = "What color is the sky? Answer in one word."
agent8_response = generate_text(current_model, agent8_prompt)

agent_response_list.append(agent8_response)

# AGENT 9

agent9_prompt = "What color is the sky? Answer in one word."
agent9_response = generate_text(current_model, agent9_prompt)

agent_response_list.append(agent9_response)

# AGENT 10

agent10_prompt = "What color is the sky? Answer in one word."
agent10_response = generate_text(current_model, agent10_prompt)

agent_response_list.append(agent10_response)

# AGENT 11

agent11_prompt = "What color is the sky? Answer in one word."
agent11_response = generate_text(current_model, agent11_prompt)

agent_response_list.append(agent1_response)

# AGENT 12

agent12_prompt = "What color is the sky? Answer in one word."
agent12_response = generate_text(current_model, agent12_prompt)

agent_response_list.append(agent12_response)

# AGENT 13

agent13_prompt = "What color is the sky? Answer in one word."
agent13_response = generate_text(current_model, agent13_prompt)

agent_response_list.append(agent13_response)

# AGENT 14

agent14_prompt = "What color is the sky? Answer in one word."
agent14_response = generate_text(current_model, agent14_prompt)

agent_response_list.append(agent14_response)

# AGENT 15

agent15_prompt = "What color is the sky? Answer in one word."
agent15_response = generate_text(current_model, agent15_prompt)

agent_response_list.append(agent15_response)

# AGENT 16

agent16_prompt = "What color is the sky? Answer in one word."
agent16_response = generate_text(current_model, agent16_prompt)

agent_response_list.append(agent16_response)

# AGENT 17

agent17_prompt = "What color is the sky? Answer in one word."
agent17_response = generate_text(current_model, agent17_prompt)

agent_response_list.append(agent17_response)

# AGENT 18

agent18_prompt = "What color is the sky? Answer in one word."
agent18_response = generate_text(current_model, agent18_prompt)

agent_response_list.append(agent18_response)

# AGENT 19

agent19_prompt = "What color is the sky? Answer in one word."
agent19_response = generate_text(current_model, agent19_prompt)

agent_response_list.append(agent19_response)

# AGENT 20

agent20_prompt = "What color is the sky? Answer in one word."
agent20_response = generate_text(current_model, agent20_prompt)

agent_response_list.append(agent20_response)

# AGENT 21

agent21_prompt = "What color is the sky? Answer in one word."
agent21_response = generate_text(current_model, agent21_prompt)

agent_response_list.append(agent21_response)

# AGENT 22

agent22_prompt = "What color is the sky? Answer in one word."
agent22_response = generate_text(current_model, agent22_prompt)

agent_response_list.append(agent22_response)

# AGENT 23

agent23_prompt = "What color is the sky? Answer in one word."
agent23_response = generate_text(current_model, agent23_prompt)

agent_response_list.append(agent23_response)

# AGENT 24

agent24_prompt = "What color is the sky? Answer in one word."
agent24_response = generate_text(current_model, agent24_prompt)

agent_response_list.append(agent24_response)

# AGENT 25

agent25_prompt = "What color is the sky? Answer in one word."
agent25_response = generate_text(current_model, agent25_prompt)

agent_response_list.append(agent25_response)

# AGENT 26

agent26_prompt = "What color is the sky? Answer in one word."
agent26_response = generate_text(current_model, agent26_prompt)

agent_response_list.append(agent26_response)

# AGENT 27

agent27_prompt = "What color is the sky? Answer in one word."
agent27_response = generate_text(current_model, agent27_prompt)

agent_response_list.append(agent27_response)

# AGENT 28

agent28_prompt = "What color is the sky? Answer in one word."
agent28_response = generate_text(current_model, agent28_prompt)

agent_response_list.append(agent28_response)

# AGENT 29

agent29_prompt = "What color is the sky? Answer in one word."
agent29_response = generate_text(current_model, agent29_prompt)

agent_response_list.append(agent29_response)

# AGENT 30

agent30_prompt = "What color is the sky? Answer in one word."
agent30_response = generate_text(current_model, agent30_prompt)

agent_response_list.append(agent30_response)


cleaned_agent_response_list = []
for string in agent_response_list:
    new_string = string.replace('Generated text (gemma3:1b):', '')
    no_line_new_string = new_string.strip('\n')
    cleaned_agent_response_list.append(no_line_new_string)

agent_name_list = ['agent1', 'agent2', 'agent3', 'agent4', 'agent5', 'agent6', 'agent7', 'agent8', 'agent9', 'agent10', 'agent11', 'agent12', 'agent13', 'agent14', 'agent15', 'agent16', 'agent17', 'agent18', 'agent19', 'agent20', 'agent21', 'agent22', 'agent23', 'agent24', 'agent25', 'agent26', 'agent27', 'agent28', 'agent29', 'agent30']

agent_response_dict = dict(zip(agent_name_list, cleaned_agent_response_list))

print(agent_response_dict)

#cleaned_agent_response_list = string list of all agent responses
#agent_name_list = the list of the agent
#agent_response_dict = dictionary with agent name as key and their generated response as the value