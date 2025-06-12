# Python Log Analyzer

A collection of Python scripts for analyzing web server logs to extract useful metrics and insights.

## Overview

This project contains three specialized scripts for analyzing NodeJS application logs:

1. **[IP Request Window Analysis](ip_analysis/README.md)**: Identifies how many requests each IP address made within a 10-second window after their first request
2. **[User Agent Analysis](user_agent_analysis/README.md)**: Categorizes and counts requests by user agent type
3. **[Endpoint Analysis](endpoint_analysis/README.md)**: Counts the number of times each endpoint was accessed

## Project Structure

```
Python_Log_Analyzer/
├── NodeJsApp.log           # The log file to analyze
├── README.md               # This documentation file
├── ip_analysis/            # IP request analysis
│   ├── README.md           # IP analysis documentation
│   └── ip_requests_window.py
├── user_agent_analysis/    # User agent analysis
│   ├── README.md           # User agent analysis documentation
│   └── user_agent_requests.py
└── endpoint_analysis/      # Endpoint access analysis
    ├── README.md           # Endpoint analysis documentation
    └── endpoint_requests.py
```

## Scripts

### 1. [ip_analysis/ip_requests_window.py](ip_analysis/README.md)

Analyzes how many requests came from each IP address within a 10-second window after their first request.

```bash
cd ip_analysis
python3 ip_requests_window.py
```

**Features:**
- Tracks the first request timestamp for each unique IP
- Counts subsequent requests within a 10-second window
- Provides detailed output with IP addresses and request counts
- Sorts results by highest request count
- Includes summary statistics

### 2. [user_agent_analysis/user_agent_requests.py](user_agent_analysis/README.md)

Determines the number of requests coming from each user agent type.

```bash
cd user_agent_analysis
python3 user_agent_requests.py
```

**Features:**
- Extracts and categorizes user agent strings
- Groups similar browsers by platform (Chrome on Windows/Mac/Linux)
- Counts requests for each user agent category
- Sorts results by highest request count
- Includes summary statistics with percentages

### 3. [endpoint_analysis/endpoint_requests.py](endpoint_analysis/README.md)

Counts the number of times each endpoint was accessed.

```bash
cd endpoint_analysis
python3 endpoint_requests.py
```

**Features:**
- Extracts HTTP method and endpoint information
- Counts requests for each unique endpoint
- Provides breakdown by HTTP method (GET, POST, etc.)
- Sorts results by most frequently accessed endpoints
- Includes summary statistics with percentages

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

Each script can be run independently and accepts an optional log file path as a command-line argument:

```bash
python3 script_name.py [path/to/logfile]
```

If no log file path is provided, the scripts will look for `NodeJsApp.log` in the project root directory.

## Detailed Documentation

For more detailed information about each script, please refer to the README files in their respective directories:

- [IP Analysis Documentation](ip_analysis/README.md)
- [User Agent Analysis Documentation](user_agent_analysis/README.md)
- [Endpoint Analysis Documentation](endpoint_analysis/README.md)

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

Summary:
Total unique IPs: 8
IPs with multiple requests in window: 5
Most active IP: 197.159.135.110 with 42 requests in window
```

### User Agent Analysis
```
User Agent Type | Request Count
------------------------------
Chrome (Linux) | 352
Chrome (Windows) | 24
Safari | 48

Summary:
Total requests: 424
Unique user agent types: 3
Most common user agent: Chrome (Linux) (352 requests, 83.0%)
```

### Endpoint Analysis
```
Endpoint | Request Count
------------------------------
/favicon.ico | 214
/ | 210

HTTP Method | Request Count
------------------------------
GET | 424

Summary:
Total requests: 424
Unique endpoints: 2
Most accessed endpoint: /favicon.ico (214 requests, 50.5%)
```