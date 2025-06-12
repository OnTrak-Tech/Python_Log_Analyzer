# IP Request Window Analysis

This script analyzes web server logs to identify how many requests each IP address made within a 10-second window after their first request.

## How It Works

1. The script reads the log file line by line
2. For each line, it extracts the timestamp and IP address using regex
3. For each IP address:
   - Records the timestamp of its first request
   - Counts subsequent requests that occur within 10 seconds of the first request
4. Results are sorted by the number of requests in descending order

## Usage

```bash
# Run with default log file (../NodeJsApp.log)
python3 ip_requests_window.py

# Or specify a custom log file path
python3 ip_requests_window.py /path/to/your/logfile.log
```

## Example Output

```
Analyzing log file: ../NodeJsApp.log

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

## Customization

You can modify the script to:
- Change the time window (currently set to 10 seconds) by editing the `time_diff <= 10.0` condition
- Add additional metrics or filtering criteria
- Change the output format

## Technical Details

- Uses Python's `re` module for regex pattern matching
- Uses `datetime` for timestamp parsing and time difference calculations
- Uses `defaultdict` for efficient counting
- No external dependencies required