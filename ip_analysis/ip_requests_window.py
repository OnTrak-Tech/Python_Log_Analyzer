#!/usr/bin/env python3
"""
IP Request Window Analysis Script

WHAT THIS CODE DOES:
This script analyzes a log file to count how many requests each IP address made
within a 10-second window after their first request. It helps identify potential
automated traffic or IP addresses making rapid requests to the server.

Usage:
    python3 ip_requests_window.py [log_file_path]

If no log file path is provided, it defaults to "../NodeJsApp.log"
"""

import re
from datetime import datetime
from collections import defaultdict
import sys
import os

def parse_timestamp(timestamp_str):
    """
    Parse timestamp string to datetime object
    
    Args:
        timestamp_str (str): Timestamp in format 'YYYY-MM-DDThh:mm:ss.sssZ'
        
    Returns:
        datetime: Parsed datetime object or None if parsing fails
    """
    try:
        return datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        return None

def analyze_ip_requests(log_file):
    """
    Analyze log file to find how many requests each IP made within 
    10 seconds after their first request
    
    Args:
        log_file (str): Path to the log file
        
    Returns:
        None: Results are printed to stdout
    """
    # Regular expression to extract timestamp and IP address
    pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (\d+\.\d+\.\d+\.\d+)'
    
    # Store first request time for each IP
    first_requests = {}
    # Count requests within 10-second window for each IP
    window_counts = defaultdict(int)
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Extract timestamp and IP from log line
                match = re.search(pattern, line)
                if match:
                    timestamp_str, ip = match.groups()
                    timestamp = parse_timestamp(timestamp_str)
                    
                    if not timestamp:
                        continue
                    
                    if ip not in first_requests:
                        # First request from this IP
                        first_requests[ip] = timestamp
                    else:
                        # Calculate time difference in seconds
                        time_diff = (timestamp - first_requests[ip]).total_seconds()
                        if time_diff <= 10.0:
                            # Count this request if it's within the 10-second window
                            window_counts[ip] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Print results in a formatted table
    print("\nIP Address | Requests within 10-second window after first request")
    print("-" * 60)
    
    # Sort IPs by request count (descending)
    for ip, count in sorted(window_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} | {count}")
    
    # Print summary statistics
    print("\nSummary:")
    print(f"Total unique IPs: {len(first_requests)}")
    print(f"IPs with multiple requests in window: {len(window_counts)}")
    if window_counts:
        max_ip = max(window_counts.items(), key=lambda x: x[1])
        print(f"Most active IP: {max_ip[0]} with {max_ip[1]} requests in window")

def main():
    """Main function to handle command line arguments and run the analysis"""
    # Default log file path (relative to script location)
    default_log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "NodeJsApp.log")
    
    # Use command line argument if provided, otherwise use default
    log_file = sys.argv[1] if len(sys.argv) > 1 else default_log_file
    
    print(f"Analyzing log file: {log_file}")
    analyze_ip_requests(log_file)

if __name__ == "__main__":
    main()