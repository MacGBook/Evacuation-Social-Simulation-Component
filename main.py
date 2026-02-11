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


# total_output.csv; ind_ag_output.csv; prompt number
#  1 - 100; 1 - 200 : Prompt 1
# 101 - 177; 201 - 354 : Prompt 2
# 178 - 277; 355 - 554 : Prompt 3
# 278 - 377; 555 - 754 : Prompt 4
# 378 - 477; 755 - 954 : Prompt 5
# 478 - 577; 955 - 1154 : Prompt 6
# 578 - 677; 1155 - 1354 : Prompt 7