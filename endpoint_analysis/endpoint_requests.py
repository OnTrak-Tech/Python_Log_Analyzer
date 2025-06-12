#!/usr/bin/env python3
"""
Endpoint Analysis Script

WHAT THIS CODE DOES:
This script analyzes a log file to count the number of times each endpoint was
accessed. It extracts the HTTP method and endpoint from each log entry, helping
you identify the most frequently accessed endpoints and the distribution of
HTTP methods used in your application.

Usage:
    python3 endpoint_requests.py [log_file_path]

If no log file path is provided, it defaults to "../NodeJsApp.log"
"""

import re
from collections import defaultdict
import sys
import os

def analyze_endpoints(log_file):
    """
    Analyze log file to count requests by endpoint
    
    Args:
        log_file (str): Path to the log file
        
    Returns:
        None: Results are printed to stdout
    """
    # Regular expression to extract HTTP method and endpoint from request
    pattern = r'"(GET|POST|PUT|DELETE|PATCH|OPTIONS) ([^ ]*) HTTP'
    
    # Count requests by endpoint
    endpoint_counts = defaultdict(int)
    # Count requests by HTTP method
    method_counts = defaultdict(int)
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Extract method and endpoint from log line
                match = re.search(pattern, line)
                if match:
                    method, endpoint = match.groups()
                    
                    # Increment counts
                    endpoint_counts[endpoint] += 1
                    method_counts[method] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Print endpoint results in a formatted table
    print("\nEndpoint | Request Count")
    print("-" * 30)
    
    # Sort endpoints by request count (descending)
    for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{endpoint} | {count}")
    
    # Print HTTP method breakdown
    print("\nHTTP Method | Request Count")
    print("-" * 30)
    
    # Sort methods by request count (descending)
    for method, count in sorted(method_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{method} | {count}")
    
    # Print summary statistics
    total_requests = sum(endpoint_counts.values())
    print("\nSummary:")
    print(f"Total requests: {total_requests}")
    print(f"Unique endpoints: {len(endpoint_counts)}")
    if endpoint_counts:
        most_accessed = max(endpoint_counts.items(), key=lambda x: x[1])
        percentage = (most_accessed[1] / total_requests) * 100 if total_requests else 0
        print(f"Most accessed endpoint: {most_accessed[0]} ({most_accessed[1]} requests, {percentage:.1f}%)")

def main():
    """Main function to handle command line arguments and run the analysis"""
    # Default log file path (relative to script location)
    default_log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "NodeJsApp.log")
    
    # Use command line argument if provided, otherwise use default
    log_file = sys.argv[1] if len(sys.argv) > 1 else default_log_file
    
    print(f"Analyzing log file: {log_file}")
    analyze_endpoints(log_file)

if __name__ == "__main__":
    main()