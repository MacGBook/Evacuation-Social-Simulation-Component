# SOCIAL SIMULATION MAIN
# author: Mac Gagne

##############################################################################################################################################################################################################################################################################################################################################################
# IMPORTS

import csv

# From evaluation_agent:
from evaluation_agent import eval_response_dict
from evaluation_agent import total_message_sum

##############################################################################################################################################################################################################################################################################################################################################################
# COMPLETING THE RUN AND SAVING IT TO A CSV

#Save individual rankings to their csv
with open("ind_ag_output.csv", mode='a', newline="") as f:
    writer = csv.DictWriter(f, eval_response_dict.keys())
    writer.writeheader()
    writer.writerow(eval_response_dict)

try:
    with open("total_output.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the integer as a single row
        writer.writerow([total_message_sum])
except IOError as e:
    print(f"Error writing to file: {e}")


 