# User Agent Analysis

This script analyzes web server logs to determine the number of requests coming from each user agent type.

## How It Works

1. The script reads the log file line by line
2. For each line, it extracts the user agent string using regex (the last quoted string in each log line)
3. It categorizes each user agent into types based on browser and platform:
   - Chrome (Windows, Mac, Linux, Other)
   - Safari
   - Firefox
   - Edge
   - Other
4. Results are sorted by the number of requests in descending order

## Usage

```bash
# Run with default log file (../NodeJsApp.log)
python3 user_agent_requests.py

# Or specify a custom log file path
python3 user_agent_requests.py /path/to/your/logfile.log
```

## Example Output

```
Analyzing log file: ../NodeJsApp.log

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

## Customization

You can modify the script to:
- Add more detailed user agent categorization
- Extract browser versions
- Group by operating systems
- Add additional metrics or filtering criteria
- Change the output format

## Technical Details

- Uses Python's `re` module for regex pattern matching
- Uses `defaultdict` for efficient counting
- No external dependencies required