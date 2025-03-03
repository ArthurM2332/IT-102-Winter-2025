import re
from collections import Counter 

log_file_path = "/home/justincase/Desktop/IT-102-Winter-2025/Assignments 1-5/access.log"

log_pattern = r'"[A-Z]+ [^"]+ HTTP/1\.[01]" (\d{3})'

with open(log_file_path, "r") as file:
    logs = file.readlines()

status_codes = [re.search(log_pattern, line).group(1) for line in logs if re.search(log_pattern, line)]  

status_counts= Counter(status_codes)

print("HTTP Status Codes Distributions: ")
for status, count in status_counts.items():
    print(f"{status}: {count}")
