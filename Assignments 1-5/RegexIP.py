import re
from collections import Counter
with open('/home/justincase/Desktop/IT-102-Winter-2025/Assignments 1-5/access.log', "r") as file:
    logs = file.readlines()
ip_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'    

ip_addresses = [re.search(ip_pattern, line).group(1) for line in logs if re.search(ip_pattern, line)]
ip_counts = Counter(ip_addresses)

if ip_counts:
    total_requests = sum(ip_counts.values())
    top_ips = ip_counts.most_common(5)
    for ip, count in top_ips:
        percentage = (count / total_requests) * 100
        print(f" {ip} made {count} requests ({percentage:.2f}% of total traffic)")

else:
    print("\ No IP addresses found in log file.")