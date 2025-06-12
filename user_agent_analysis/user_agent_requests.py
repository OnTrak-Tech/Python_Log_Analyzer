#!/usr/bin/env python3
"""
User Agent Analysis Script

WHAT THIS CODE DOES:
This script analyzes a log file to count the number of requests coming from each
user agent type. It categorizes user agents by browser and platform, helping you
understand which browsers and devices are accessing your web application.

Usage:
    python3 user_agent_requests.py [log_file_path]

If no log file path is provided, it defaults to "../NodeJsApp.log"
"""

import re
from collections import defaultdict
import sys
import os

def analyze_user_agents(log_file):
    """
    Analyze log file to count requests by user agent type
    
    Args:
        log_file (str): Path to the log file
        
    Returns:
        None: Results are printed to stdout
    """
    # Regular expression to extract user agent (the last quoted string in the log line)
    pattern = r'"([^"]*)"$'
    
    # Count requests by user agent type
    user_agent_counts = defaultdict(int)
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Extract user agent from log line
                match = re.search(pattern, line)
                if match:
                    user_agent = match.group(1)
                    
                    # Categorize user agent based on browser and platform
                    if "Chrome" in user_agent and "Safari" in user_agent:
                        if "Macintosh" in user_agent:
                            agent_type = "Chrome (Mac)"
                        elif "Windows" in user_agent:
                            agent_type = "Chrome (Windows)"
                        elif "Linux" in user_agent:
                            agent_type = "Chrome (Linux)"
                        else:
                            agent_type = "Chrome (Other)"
                    elif "Safari" in user_agent and "Chrome" not in user_agent:
                        agent_type = "Safari"
                    elif "Firefox" in user_agent:
                        agent_type = "Firefox"
                    elif "Edge" in user_agent:
                        agent_type = "Edge"
                    else:
                        agent_type = "Other"
                    
                    # Increment count for this user agent type
                    user_agent_counts[agent_type] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Print results in a formatted table
    print("\nUser Agent Type | Request Count")
    print("-" * 30)
    
    # Sort user agents by request count (descending)
    for agent_type, count in sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{agent_type} | {count}")
    
    # Print summary statistics
    total_requests = sum(user_agent_counts.values())
    print("\nSummary:")
    print(f"Total requests: {total_requests}")
    print(f"Unique user agent types: {len(user_agent_counts)}")
    if user_agent_counts:
        most_common = max(user_agent_counts.items(), key=lambda x: x[1])
        percentage = (most_common[1] / total_requests) * 100 if total_requests else 0
        print(f"Most common user agent: {most_common[0]} ({most_common[1]} requests, {percentage:.1f}%)")

def main():
    """Main function to handle command line arguments and run the analysis"""
    # Default log file path (relative to script location)
    default_log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "NodeJsApp.log")
    
    # Use command line argument if provided, otherwise use default
    log_file = sys.argv[1] if len(sys.argv) > 1 else default_log_file
    
    print(f"Analyzing log file: {log_file}")
    analyze_user_agents(log_file)

if __name__ == "__main__":
    main()