#!/usr/bin/env python3
import re
from datetime import datetime
from collections import defaultdict

def analyze_ip_requests(log_file):
    # Regular expression to extract timestamp and IP address
    pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (\d+\.\d+\.\d+\.\d+)'
    
    # Store first request time for each IP
    first_requests = {}
    # Count requests within 10-second window for each IP
    window_counts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                timestamp_str, ip = match.groups()
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                if ip not in first_requests:
                    # First request from this IP
                    first_requests[ip] = timestamp
                else:
                    # Calculate time difference in seconds
                    time_diff = (timestamp - first_requests[ip]).total_seconds()
                    if time_diff <= 10.0:
                        window_counts[ip] += 1
    
    # Print results
    print("IP Address | Requests within 10-second window after first request")
    print("-" * 60)
    for ip, count in sorted(window_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} | {count}")

if __name__ == "__main__":
    analyze_ip_requests("/home/rocka/Python_Log_Analyzer/NodeJsApp.log")