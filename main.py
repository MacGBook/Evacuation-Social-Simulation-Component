# SOCIAL SIMULATION MAIN
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

import csv

# From evaluation_agent:

iterations = input("How many iterations of the social sim would you like to run? ")

##############################################################################################################################################################################################################################################################################################################################################################
# COMPLETING THE RUN AND SAVING IT TO A CSV

final_responses_dictionary = {}
final_total_sum_dictionary = {}

for number in range(int(iterations)):
    iteration_name = "iteration_" + str(number)

    from evaluation_agent import eval_response_dict

    list_of_statements = eval_response_dict.values()


    final_responses_dictionary[iteration_name] = list_of_statements

    from evaluation_agent import total_message_sum
    final_total_sum_dictionary[iteration_name] = total_message_sum
    




#Save individual rankings to their csv
with open("ind_ag_output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, final_responses_dictionary.keys())
    writer.writeheader()
    writer.writerow(final_responses_dictionary)




#Save individual rankings to their csv
#with open("total_output.csv.csv", "w", newline="") as f:
 #   writer = csv.DictWriter(f, final_total_sum_dictionary.keys())
  #  writer.writeheader()
   # writer.writerow(final_total_sum_dictionary)




#try:
 #   with open("total_output.csv", mode='w', newline='') as file:
  #      writer = csv.writer(file)

        # Write the integer as a single row
   #     writer.writerow([total_message_sum])
#except IOError as e:
 #   print(f"Error writing to file: {e}")


 