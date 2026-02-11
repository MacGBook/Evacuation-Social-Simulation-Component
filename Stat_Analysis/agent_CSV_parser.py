#Parser for CSV results for individual agent results 
#By Mac Gagne

import csv

#Assumes 100 runs per prompt

#SET THIS AT THE START OF RUNNING CODE
#Number of prompts being tested
prompt_number = 2

with open('ind_ag_output.csv', mode='r', newline='', encoding='utf-8') as csv_file:
    # Create a reader object
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Loop through each row in the file
    results_list_of_lists = []
    for row in csv_reader:
        # Each row is a list of strings
        results_list_of_lists.append(row)
        # You can access individual columns by index (e.g., row[0], row[1])


row_count = 1
finalized_row_list = []
for row_list in results_list_of_lists:
    if row_count % 2 == 0:
        finalized_row_list.append(row_list)
    row_count += 1


#finalized_row_list now gives us only our agent values as lists of strings
int_list = []
for lil_list in finalized_row_list:
    updated_list = []
    for value in lil_list:
        value_int = int(value)
        if value_int == 404:
            pass
        else:
            what_to_append = value_int
        updated_list.append(what_to_append)
    int_list.append(updated_list)

#Int list gives these lists as integers 
#It also excludes 404 as a numerical term for None type

#Give the average for each list
#Save this as a list of integers 

row_averages_list = []
for list in int_list:
    total = sum(list)
    length = len(list)
    average = total / length
    row_averages_list.append(average)

#row_averages_list is what we return to get the row averages across all agents per run

#Next, we need to sort our original list into lists based on agent
#We need to make sure these values are int
#And we need to make sure 404 values are not saved

agent1_list = []
agent2_list = []
agent3_list = []
agent4_list = []
agent5_list = []
agent6_list = []
agent7_list = []
agent8_list = []
agent9_list = []
agent10_list = []
agent11_list = []
agent12_list = []
agent13_list = []
agent14_list = []
agent15_list = []
agent16_list = []
agent17_list = []
agent18_list = []
agent19_list = []
agent20_list = []
agent21_list = []
agent22_list = []
agent23_list = []
agent24_list = []
agent25_list = []
agent26_list = []
agent27_list = []
agent28_list = []
agent29_list = []
agent30_list = []

list_of_agent_lists = []

for lil_list in finalized_row_list:
    agent1_list.append(lil_list[0])
    agent2_list.append(lil_list[1])
    agent3_list.append(lil_list[2])
    agent4_list.append(lil_list[3])
    agent5_list.append(lil_list[4])
    agent6_list.append(lil_list[5])
    agent7_list.append(lil_list[6])
    agent8_list.append(lil_list[7])
    agent9_list.append(lil_list[8])
    agent10_list.append(lil_list[9])
    agent11_list.append(lil_list[10])
    agent12_list.append(lil_list[11])
    agent13_list.append(lil_list[12])
    agent14_list.append(lil_list[13])
    agent15_list.append(lil_list[14])
    agent16_list.append(lil_list[15])
    agent17_list.append(lil_list[16])
    agent18_list.append(lil_list[17])
    agent19_list.append(lil_list[18])
    agent20_list.append(lil_list[19])
    agent21_list.append(lil_list[20])
    agent22_list.append(lil_list[21])
    agent23_list.append(lil_list[22])
    agent24_list.append(lil_list[23])
    agent25_list.append(lil_list[24])
    agent26_list.append(lil_list[25])
    agent27_list.append(lil_list[26])
    agent28_list.append(lil_list[27])
    agent29_list.append(lil_list[28])
    agent30_list.append(lil_list[29])


list_of_agent_lists.append(agent1_list)
list_of_agent_lists.append(agent2_list)
list_of_agent_lists.append(agent3_list)
list_of_agent_lists.append(agent4_list)
list_of_agent_lists.append(agent5_list)
list_of_agent_lists.append(agent6_list)
list_of_agent_lists.append(agent7_list)
list_of_agent_lists.append(agent8_list)
list_of_agent_lists.append(agent9_list)
list_of_agent_lists.append(agent10_list)
list_of_agent_lists.append(agent11_list)
list_of_agent_lists.append(agent12_list)
list_of_agent_lists.append(agent13_list)
list_of_agent_lists.append(agent14_list)
list_of_agent_lists.append(agent15_list)
list_of_agent_lists.append(agent16_list)
list_of_agent_lists.append(agent17_list)
list_of_agent_lists.append(agent18_list)
list_of_agent_lists.append(agent19_list)
list_of_agent_lists.append(agent20_list)
list_of_agent_lists.append(agent21_list)
list_of_agent_lists.append(agent22_list)
list_of_agent_lists.append(agent23_list)
list_of_agent_lists.append(agent24_list)
list_of_agent_lists.append(agent25_list)
list_of_agent_lists.append(agent26_list)
list_of_agent_lists.append(agent27_list)
list_of_agent_lists.append(agent28_list)
list_of_agent_lists.append(agent29_list)
list_of_agent_lists.append(agent30_list)


#break list structure up into mutiple prompts 
total_runs_averages_list = []
for value in range(1, prompt_number+1):
    lower_index = 0
    upper_index = 100 * value
    this_prompts_iteration_list = []
    for lil_list in list_of_agent_lists:
        this_prompts_list = lil_list[lower_index:upper_index]
        new_this_prompts_list = []
        for value_2 in this_prompts_list:
            if int(value_2) != 404:
                new_this_prompts_list.append(int(value_2))
        sum_up = sum(new_this_prompts_list)
        len_up = len(new_this_prompts_list)
        average = sum_up / len_up
        this_prompts_iteration_list.append(average)
    lower_index += upper_index + 1
    total_runs_averages_list.append(this_prompts_iteration_list)


agent_name_list = ['agent1','agent2','agent3','agent4','agent5','agent6','agent7','agent8','agent9','agent10','agent11','agent12','agent13','agent14','agent15','agent16','agent17','agent18','agent19','agent20','agent21','agent22','agent23','agent24','agent25','agent26','agent27','agent28','agent29','agent30']
list_of_agent_dictionaries_for_runs = []
for lil_list in total_runs_averages_list:
    dictionary = dict(zip(agent_name_list, lil_list))
    list_of_agent_dictionaries_for_runs.append(dictionary)

#This returns the average sans 404s per agent across all 100 runs of a prompt
#print(list_of_agent_dictionaries_for_runs)


########################################################################
# WHAT TO RETURN

#This returns the average sans 404s per agent across all 100 runs of a prompt
#print(list_of_agent_dictionaries_for_runs)

#row_averages_list is what we return to get the row averages across all agents per run
#print(len(row_averages_list))

########################################################################
# SAVING TO NEW CSV
    

#Save individual rankings to their csv
with open("final_agent_results.csv", mode='w', newline="") as f:
    for lil_dict in list_of_agent_dictionaries_for_runs:
        writer = csv.DictWriter(f, lil_dict.keys())
        writer.writeheader()
        writer.writerow(lil_dict)

try:
    with open("final_agent_results_by_row_across_agents.csv", mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the integer as a single row
        for value in row_averages_list:
            writer.writerow([value])
except IOError as e:
    print(f"Error writing to file: {e}")