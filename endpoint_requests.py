#!/usr/bin/env python3
import re
from collections import defaultdict

def analyze_endpoints(log_file):
    # Regular expression to extract endpoint from request
    pattern = r'"(GET|POST|PUT|DELETE) ([^ ]*) HTTP'
    
    # Count requests by endpoint
    endpoint_counts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                method, endpoint = match.groups()
                endpoint_counts[endpoint] += 1
    
    # Print results
    print("Endpoint | Request Count")
    print("-" * 30)
    for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{endpoint} | {count}")

if __name__ == "__main__":
    analyze_endpoints("/home/rocka/Python_Log_Analyzer/NodeJsApp.log")