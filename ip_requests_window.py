#!/usr/bin/env python3
import re
from datetime import datetime
from collections import defaultdict
import sys

def parse_timestamp(timestamp_str):
    """Parse timestamp string to datetime object"""
    try:
        return datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        return None

def analyze_ip_burst_requests(log_file):
    """
    Analyze log file to find how many requests each IP made within 
    10 seconds after their first request
    """
    # Regex pattern to extract timestamp and IP
    log_pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)\s+(\d+\.\d+\.\d+\.\d+)'
    
    # Data structures to track requests
    ip_requests = defaultdict(list)  # Store all requests per IP
    
    try:
        with open(log_file, 'r') as file:
            for line_num, line in enumerate(file, 1):
                match = re.search(log_pattern, line.strip())
                if match:
                    timestamp_str, ip_address = match.groups()
                    timestamp = parse_timestamp(timestamp_str)
                    
                    if timestamp:
                        ip_requests[ip_address].append(timestamp)
                    else:
                        print(f"Warning: Invalid timestamp format at line {line_num}")
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Analyze burst requests for each IP
    results = []
    
    for ip, timestamps in ip_requests.items():
        if len(timestamps) < 2:
            # Only one request, no additional requests possible
            results.append((ip, 0, timestamps[0] if timestamps else None))
            continue
            
        # Sort timestamps to ensure chronological order
        timestamps.sort()
        first_request = timestamps[0]
        
        # Count requests within 10-second window after first request
        burst_count = 0
        for timestamp in timestamps[1:]:  # Skip first request
            time_diff = (timestamp - first_request).total_seconds()
            if time_diff <= 10.0:
                burst_count += 1
            else:
                break  # Since sorted, no more requests will be within window
        
        results.append((ip, burst_count, first_request))
    
    # Display results
    print("IP Request Burst Analysis")
    print("=" * 70)
    print(f"{'IP Address':<15} {'Burst Count':<12} {'First Request Time'}")
    print("-" * 70)
    
    # Sort by burst count (descending) then by IP
    results.sort(key=lambda x: (-x[1], x[0]))
    
    for ip, count, first_time in results:
        time_str = first_time.strftime('%Y-%m-%d %H:%M:%S') if first_time else 'N/A'
        print(f"{ip:<15} {count:<12} {time_str}")
    
    # Summary statistics
    total_ips = len(results)
    burst_ips = sum(1 for _, count, _ in results if count > 0)
    max_burst = max((count for _, count, _ in results), default=0)
    
    print("\n" + "=" * 70)
    print("SUMMARY:")
    print(f"Total unique IPs: {total_ips}")
    print(f"IPs with burst activity: {burst_ips}")
    print(f"Maximum burst count: {max_burst}")
    
    if burst_ips > 0:
        print("\nTop 5 most active IPs:")
        for i, (ip, count, _) in enumerate(results[:5]):
            if count > 0:
                print(f"  {i+1}. {ip} - {count} requests")

def main():
    log_file = "/home/rocka/Python_Log_Analyzer/NodeJsApp.log"
    
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    
    print(f"Analyzing log file: {log_file}")
    print()
    
    analyze_ip_burst_requests(log_file)

if __name__ == "__main__":
    main()