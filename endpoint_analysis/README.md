# Endpoint Analysis

This script analyzes web server logs to count the number of times each endpoint was accessed.

## How It Works

1. The script reads the log file line by line
2. For each line, it extracts the HTTP method and endpoint using regex
3. It counts:
   - The number of requests for each unique endpoint
   - The number of requests for each HTTP method (GET, POST, etc.)
4. Results are sorted by the number of requests in descending order

## Usage

```bash
# Run with default log file (../NodeJsApp.log)
python3 endpoint_requests.py

# Or specify a custom log file path
python3 endpoint_requests.py /path/to/your/logfile.log
```

## Example Output

```
Analyzing log file: ../NodeJsApp.log

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

## Customization

You can modify the script to:
- Group similar endpoints (e.g., those with the same path prefix)
- Filter by specific HTTP methods
- Analyze response status codes
- Track endpoint access patterns over time
- Change the output format

## Technical Details

- Uses Python's `re` module for regex pattern matching
- Uses `defaultdict` for efficient counting
- No external dependencies required