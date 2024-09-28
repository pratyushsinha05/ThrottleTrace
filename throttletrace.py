import argparse
import requests
import time

def send_requests(endpoint_url, http_method, max_requests, retry_after):
    successful_requests = 0
    rate_limited_requests = 0
    retry_attempts = 0
    rate_limit_pattern = []

    for i in range(max_requests):
        try:
            start_time = time.time()
            response = requests.request(http_method, endpoint_url)
            end_time = time.time()
            elapsed_time = end_time - start_time

            if response.status_code == 429:  # Rate limit status code
                print(f"Rate limited! Waiting for {retry_after} seconds before retrying...")
                rate_limited_requests += 1
                rate_limit_pattern.append({
                    "request_number": i+1,
                    "response_time": elapsed_time,
                    "retry_wait": retry_after,
                    "timestamp": time.time()
                })
                time.sleep(retry_after)
                retry_attempts += 1
            else:
                successful_requests += 1
                print(f"Request {i+1} successful with status {response.status_code}")

        except requests.RequestException as e:
            print(f"Request {i+1} failed: {e}")

    return successful_requests, rate_limited_requests, retry_attempts, rate_limit_pattern

def analyze_rate_limit_pattern(pattern):
    print("\nRate-Limit Pattern Analysis:")
    if not pattern:
        print("No rate limiting detected during the test.")
        return

    for entry in pattern:
        print(f"Request {entry['request_number']} was rate limited after {entry['response_time']:.2f} seconds. Retrying after {entry['retry_wait']} seconds.")

    intervals = []
    for i in range(1, len(pattern)):
        interval = pattern[i]['timestamp'] - pattern[i-1]['timestamp']
        intervals.append(interval)

    if intervals:
        avg_interval = sum(intervals) / len(intervals)
        print(f"\nAverage interval between rate limits: {avg_interval:.2f} seconds")

def main():
    parser = argparse.ArgumentParser(description="API Rate Limiter Testing Tool with Rate-Limit Pattern Detection")
    parser.add_argument('--endpoint', help='API endpoint URL', required=True)
    parser.add_argument('--method', help='HTTP method (GET, POST, etc.)', required=True)
    parser.add_argument('--max-requests', help='Maximum number of requests to send', type=int, required=True)
    parser.add_argument('--retry-after', help='Time to wait between retries when rate limited (seconds)', type=int, required=True)
    args = parser.parse_args()

    successful, rate_limited, retries, rate_limit_pattern = send_requests(args.endpoint, args.method.upper(), args.max_requests, args.retry_after)
    
    print(f"\nSummary:")
    print(f"Successful Requests: {successful}")
    print(f"Rate Limited Requests: {rate_limited}")
    print(f"Retry Attempts: {retries}")

    # Analyze and print rate-limit pattern
    analyze_rate_limit_pattern(rate_limit_pattern)

if __name__ == "__main__":
    main()
