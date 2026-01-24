# SOCIAL SIMULATION EVALUATION AGENT
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

#General
import json
import ollama
import re 

#SET CURRENT MODEL
from curr_mod import current_model

#SET EVAC MESSAGE
from evac_mess import evacuation_message

#From agents.py
from agents import agent_response_dict

##############################################################################################################################################################################################################################################################################################################################################################
#LLM SET UP
# Ollama: function for basic text generation
def generate_text(model_name, prompt):
    response = ollama.generate(model=model_name, prompt=prompt)
    return(f"Generated text ({model_name}):\n{response['response']}\n")

#List to append rankings to 
eval_rankings_list = []
##############################################################################################################################################################################################################################################################################################################################################################
#EVALUATION AGENT PROMPTING



for message in agent_response_dict.keys():

    #Obtain an LLM ranking of the message
    eval_agent_description = "You are an evaluation agent, tasked with grading how well someone understands a particular message. "
    eval_agent_prompt =  eval_agent_description + "The person you are grading receives the following message: " + evacuation_message + " The person you're grading responds with the following message: " + message + " Based on this message, if the person understands who will be effected by the storm in the original message, award them one point. If the person understands what the threat of the original message is, award them one point. If the person understands where this storm will hit, award them one point. If this person understands when this storm will impact them, award one point. If the person understands why it is important for them to take action or why the storm is dangerous, award them one point. If the person understands how to take proper action from this threat, award them one point. Sum all points that you have given this response into an overall total for the person's message. It is essential that you provide this ranking as an integer from 1 to 6, surrounded by square brackets. For example, your answer must include one of the following: [1], [2], [3], [4], [5] or [6]. Your ranking must be in square brackets!"
    eval_agent_response = generate_text(current_model, eval_agent_prompt)

    # Isolate that LLM ranking as an integer and add it to a list
    obtain_ranking = re.search(r'\[(.*?)\]', eval_agent_response)
    if obtain_ranking: 
        content = obtain_ranking.group(1)
        #this_is_a_number = int(content)
    else:
        content = str(404) #If 404 appears as the ranking, it's a sign that the LLM as provided an invalid response
        #this_is_a_number = int(404)

    does_content_have_non_numbers = any(char.isalpha() for char in content)

    # Now, we clear out any generated values that still have letters
    if does_content_have_non_numbers == True:
        final_add = int(404) #if the answer has letters, we assign it a 404 error code
    if does_content_have_non_numbers == False:
        final_add = int(content) # else, we convert it directly into an integer 

    eval_rankings_list.append(final_add)




# We initialize a counter to sum up the overall score of all agent responses
total_message_sum = 0

for value in eval_rankings_list:
    if value == int(404):
        pass # We don't count 404 errors to the overall score. Notably, 404 codes could be used to count model or prompting efficiency going forward
    else:
        total_message_sum += value


# This provides us with a final dictionary llinking rankings as values to keys as agent names
eval_response_dict = dict(zip(agent_response_dict.keys(), eval_rankings_list))

#printing for testing
#print(eval_response_dict)
#print('Total Message Score: ')
#print(total_message_sum)