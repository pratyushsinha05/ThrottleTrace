# ThrottleTrace

## Overview

**ThrottleTrace** is a powerful tool designed for developers and testers to analyze and understand the rate-limiting behavior of APIs. By simulating requests and monitoring responses, ThrottleTrace provides insights into how APIs handle traffic, allowing you to optimize your applications accordingly.

## Features

- **Rate-Limit Detection**: Identify when rate limits are hit and how the API responds.
- **Pattern Analysis**: Analyze the intervals and frequency of rate-limited responses to understand throttling behavior.
- **Dynamic Retry Logic**: Automatically retry requests after encountering rate limits, with configurable wait times.
- **Concurrent Requests**: Simulate multiple clients to test how APIs handle bursts of traffic.

## Installation

To install ThrottleTrace, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/pratyushsinha05/throttletrace.git
    cd throttletrace
    ```

2. **Install Dependencies**:
    Make sure you have Python installed. Then, install the required packages using pip:
    ```bash
    pip install requests
    ```

## Usage

### Command-Line Interface

You can use ThrottleTrace through the command line. Here’s how to run it:

```bash
python throttle_trace.py --endpoint <API_ENDPOINT> --method <HTTP_METHOD> --max-requests <NUMBER_OF_REQUESTS> --retry-after <SECONDS>
