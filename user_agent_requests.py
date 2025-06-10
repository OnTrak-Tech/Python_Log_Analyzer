#!/usr/bin/env python3
import re
from collections import defaultdict

def analyze_user_agents(log_file):
    # Regular expression to extract user agent
    pattern = r'"([^"]*)"$'
    
    # Count requests by user agent type
    user_agent_counts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                user_agent = match.group(1)
                
                # Categorize user agent
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
                
                user_agent_counts[agent_type] += 1
    
    # Print results
    print("User Agent Type | Request Count")
    print("-" * 30)
    for agent_type, count in sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{agent_type} | {count}")

if __name__ == "__main__":
    analyze_user_agents("/home/rocka/Python_Log_Analyzer/NodeJsApp.log")