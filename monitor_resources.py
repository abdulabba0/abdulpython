""" 
Question 2: System Resource Monitor
Create a script monitor_resources.py that:
1.	Uses the subprocess module to run system commands like top (Linux/macOS) or tasklist (Windows) to list running processes.
2.	Parses the output to:
o	Display the top 5 processes consuming the most memory.
o	Display the top 5 processes consuming the most CPU.
3.	Write this information into a log file resource_log.txt.
Bonus: Schedule the script to run every minute using the os module to manipulate file timestamps as markers.
"""

import subprocess
import os
def convert_to_number(result):
    out = ""
    for s in result :
        if s != "," :
            out += s
    return float(out)

def get_top_process(command, num_top_process):
    try :
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        sorted_result = sorted(result.stdout.splitlines()[3:], key = lambda x: convert_to_number(x.split()[-2]), reverse=True)
    except Exception as e :
        print(f"An error occurred: {e}")
    finally :
        with open("resource_log.txt", "w") as log_file:
            log_file.write(f"Top {num_top_process} processes consuming the most memory:\n")
            for i in range(num_top_process):
                extract = sorted_result[i].split()[:-5]
                size = convert_to_number(sorted_result[i].split()[-2]) / 1024
                text = " ".join(extract)
                log_file.write(f"{i+1} {text} | {int(size)}MB \n")
        print("log file has been created")
    
                
get_top_process("TASKLIST", 10)

# result = subprocess.run("TASKLIST", capture_output=True, text=True, shell=True)
# sorted_result = sorted(result.stdout.splitlines()[3:], key = lambda x: convert_to_number(x.split()[-2]), reverse=True)
# for line in sorted_result:
#     print(f"len(line).split())")