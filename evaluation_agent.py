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

##############################################################################################################################################################################################################################################################################################################################################################
# LABELS

#note: make sure all labels lowercase- in dict too!
#note 2: make sure all dictionary values are integers
who_labels = "[the agent mentions themselves], [the agent mentions their family]." 
who_labels_list = ["the agent mentions themselves", "the agent mentions their family"]
who_labels_dict = {"the agent mentions themselves":2, "the agent mentions their family":1}

what_labels = "[the agent mentions the hurricane], [the agent mentions threats cause by a hurricane], [the agent mentions storm surge]."
what_labels_list = ["the agent mentions the hurricane", "the agent mentions threats cause by a hurricane", "the agent mentions storm surge"]
what_labels_dict = {"the agent mentions the hurricane":1, "the agent mentions threats cause by a hurricane":2, "the agent mentions storm surge":3}

when_labels = "[the agent mentions landfall of the hurricane], [the agent mentions a direct time when the hurricane hits]."
when_labels_list = ["the agent mentions landfall of the hurricane", "the agent mentions a direct time when the hurricane hits"]
when_labels_dict = {"the agent mentions landfall of the hurricane":1, "the agent mentions a direct time when the hurricane hits":3}

where_labels = "[the agent mentions manteo north carolina], [the agent mentions their home], [the agent mentions their city]."
where_labels_list = ["the agent mentions manteo north carolina", "the agent mentions their home", "the agent mentions their city"]
where_labels_dict = {"the agent mentions manteo north carolina":1, "the agent mentions their home":1, "the agent mentions their city":1}

why_labels = "[the agent acknowledges the hurricane is dangerous], [the agent acknowledges the hurricane is too dangerous to stay], [the agents knows they could die from this hurricane]."
why_labels_list = ["the agent acknowledges the hurricane is dangerous", "the agent acknowledges the hurricane is too dangerous to stay", "the agents knows they could die from this hurricane"]
why_labels_dict = {"the agent acknowledges the hurricane is dangerous":1, "the agent acknowledges the hurricane is too dangerous to stay":2, "the agents knows they could die from this hurricane":3}

how_labels = "[the agent mentions they will evacuate], [the agent mentions a descriptive plan of how they will evacuate], [the agent mentions what they will need to evacuate]."
how_labels_list = ["the agent mentions they will evacuate", "the agent mentions a descriptive plan of how they will evacuate", "the agent mentions what they will need to evacuate"]
how_labels_dict = {"the agent mentions they will evacuate":2, "the agent mentions a descriptive plan of how they will evacuate":3, "the agent mentions what they will need to evacuate":4}

##############################################################################################################################################################################################################################################################################################################################################################
# PAIR OUTPUT TEXT WITH LABELS WITH SCORES- FUNCTION
 
def add_label_score(output_text, labels_list, labels_dictionary):
    lowercase = output_text.lower()

    count = 0
    for label in labels_list:
        if label in lowercase:
            score = labels_dictionary[label]
            count += score
    
    total_score = sum(labels_dictionary.values())

    normalized_one_value = count // total_score

    return normalized_one_value

##############################################################################################################################################################################################################################################################################################################################################################
# GENERATE CONTENT

ind_agent_total_responses = []
agent_responses_list = []


for message in agent_response_dict.values():

    per_agent_rankings_list = [] # We initialize a list to hold the rankings for each agent response


    #Obtain an LLM ranking of who
    eval_agent_description_who = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_who =  eval_agent_description_who + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    who_closing = " Return only the labels you assign."
    final_eval_agent_prompt_who = eval_agent_prompt_who + who_labels + who_closing
    eval_agent_response_who = generate_text(current_model, final_eval_agent_prompt_who)
   #print(eval_agent_response_who)
    who_score = add_label_score(eval_agent_response_who, who_labels_list, who_labels_dict)
    #print(who_score)
    per_agent_rankings_list.append(who_score)

    #Obtain an LLM ranking of what
    eval_agent_description_what = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_what = eval_agent_description_what + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    what_closing = " Return only the labels you assign."
    final_eval_agent_prompt_what = eval_agent_prompt_what + what_labels + what_closing
    eval_agent_response_what = generate_text(current_model, final_eval_agent_prompt_what)
    #print(eval_agent_response_what)
    what_score = add_label_score(eval_agent_response_what, what_labels_list, what_labels_dict)
    #print(what_score)
    per_agent_rankings_list.append(what_score)

    #Obtain an LLM ranking of when
    eval_agent_description_when = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_when = eval_agent_description_when + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    when_closing = " Return only the labels you assign."
    final_eval_agent_prompt_when = eval_agent_prompt_when + when_labels + when_closing
    eval_agent_response_when = generate_text(current_model, final_eval_agent_prompt_when)
    #print(eval_agent_response_when)
    when_score = add_label_score(eval_agent_response_when, when_labels_list, when_labels_dict)
    #print(when_score)
    per_agent_rankings_list.append(when_score)

    #Obtain an LLM ranking of where
    eval_agent_description_where = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_where = eval_agent_description_where + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    where_closing = " Return only the labels you assign."
    final_eval_agent_prompt_where = eval_agent_prompt_where + where_labels + where_closing
    eval_agent_response_where = generate_text(current_model, final_eval_agent_prompt_where)
    #print(eval_agent_response_where)
    where_score = add_label_score(eval_agent_response_where, where_labels_list, where_labels_dict)
    #print(where_score)
    per_agent_rankings_list.append(where_score)

    #Obtain an LLM ranking of why
    eval_agent_description_why = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_why = eval_agent_description_why + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    why_closing = " Return only the labels you assign."
    final_eval_agent_prompt_why = eval_agent_prompt_why + why_labels + why_closing
    eval_agent_response_why = generate_text(current_model, final_eval_agent_prompt_why)
    #print(eval_agent_response_why)
    why_score = add_label_score(eval_agent_response_why, why_labels_list, why_labels_dict)
    #print(why_score)
    per_agent_rankings_list.append(why_score)

    #Obtain an LLM ranking of how
    eval_agent_description_how = "You are a classification system, tasked with assigning a relevant label to an agent's response. "
    eval_agent_prompt_how = eval_agent_description_how + "For context, the agent you are evaluating receives the following message: " + evacuation_message + " The agent you're evaluating responds with the following message: " + message + " Based on this message, please assign all applicable labels to this agent response's content from the provided list. Your provided list of labels is: "
    how_closing = " Return only the labels you assign."
    final_eval_agent_prompt_how = eval_agent_prompt_how + how_labels + how_closing
    eval_agent_response_how = generate_text(current_model, final_eval_agent_prompt_how)
    #print(eval_agent_response_how)
    how_score = add_label_score(eval_agent_response_how, how_labels_list, how_labels_dict)
    #print(how_score)
    per_agent_rankings_list.append(how_score)

    total_per_agent_score = sum(per_agent_rankings_list)

    ind_agent_total_responses.append(total_per_agent_score)
    agent_responses_list.append(per_agent_rankings_list)


##############################################################################################################################################################################################################################################################################################################################################################
# FINAL OUTPUTS

# Provides total final sum
total_message_sum = sum(ind_agent_total_responses)

# This provides us with a final dictionary llinking rankings as values to keys as agent names
eval_response_dict = dict(zip(agent_response_dict.keys(), ind_agent_total_responses))
    
#print(total_message_sum)
#print(agent_responses_list)
#print(eval_response_dict)












    