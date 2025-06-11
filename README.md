# Python Log Analyzer

A collection of Python scripts for analyzing web server logs to extract useful metrics and insights.

## Overview

This project contains three specialized scripts for analyzing NodeJS application logs:

1. **IP Request Window Analysis**: Identifies how many requests each IP address made within a 10-second window after their first request
2. **User Agent Analysis**: Categorizes and counts requests by user agent type
3. **Endpoint Analysis**: Counts the number of times each endpoint was accessed

## Scripts

### 1. ip_requests_window.py

Analyzes how many requests came from each IP address within a 10-second window after their first request.

```bash
python3 ip_requests_window.py
```

**Features:**
- Tracks the first request timestamp for each unique IP
- Counts subsequent requests within a 10-second window
- Provides detailed output with IP addresses and request counts
- Sorts results by highest request count

### 2. user_agent_requests.py

Determines the number of requests coming from each user agent type.

```bash
python3 user_agent_requests.py
```

**Features:**
- Extracts and categorizes user agent strings
- Groups similar browsers by platform (Chrome on Windows/Mac/Linux)
- Counts requests for each user agent category
- Sorts results by highest request count

### 3. endpoint_requests.py

Counts the number of times each endpoint was accessed.

```bash
python3 endpoint_requests.py
```

**Features:**
- Extracts HTTP method and endpoint information
- Counts requests for each unique endpoint
- Sorts results by most frequently accessed endpoints

## Requirements

- Python 3.6 or higher
- Standard library modules only (no external dependencies)

## Log File Format

The scripts are designed to work with standard NodeJS application logs in the following format:

```
YYYY-MM-DDThh:mm:ss.sssZ IP_ADDRESS - - [DD/Mon/YYYY:hh:mm:ss +0000] "METHOD /endpoint HTTP/1.1" STATUS_CODE - "REFERRER" "USER_AGENT"
```

Example:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
```

## Usage

1. Place your log file at `/home/rocka/Python_Log_Analyzer/NodeJsApp.log` or modify the file path in each script
2. Make the scripts executable: `chmod +x *.py`
3. Run any script: `./script_name.py`

## Customization

You can modify the scripts to:
- Change the time window (currently set to 10 seconds)
- Adjust user agent categorization
- Add additional metrics
- Change the output format

## Example Output

### IP Request Window Analysis
```
IP Address | Requests within 10-second window after first request
------------------------------------------------------------
197.159.135.110 | 42
154.161.35.247 | 28
185.195.59.88 | 15
```

### User Agent Analysis
```
User Agent Type | Request Count
------------------------------
Chrome (Linux) | 352
Chrome (Windows) | 24
Safari | 48
```

### Endpoint Analysis
```
Endpoint | Request Count
------------------------------
/favicon.ico | 214
/ | 210
```