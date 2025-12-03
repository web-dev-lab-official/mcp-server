# server_stdio.py

"""
MCP Server using STDIO (Standard Input/Output) Transport

This file runs the MCP server using the "stdio" transport, which allows
clients to interact with the server directly through the terminal or
command-line interface (CLI). The server reads input from standard input
(stdin) and outputs results to standard output (stdout).

STDIO transport is ideal for local development, testing tools/resources,
or automation scripts where network access is not required.

--------------------------------------------------------------
How to Connect to the STDIO MCP Server
--------------------------------------------------------------

1. Start the server:
   Run this file in your terminal:
       $ python server_stdio.py

2. Interact via Terminal:
   - The server will prompt for input in the terminal.
   - You can call tools, resources, or prompts interactively.
   - Example input to call a tool "add":
       {"tool": "add", "input": {"a": 5, "b": 7}}
   - The server will output the response directly in the terminal.

3. Example Tool Call:
   Input:
       {"tool": "add", "input": {"a": 2, "b": 3}}
   Output:
       {"result": 5}

4. Example Resource Call:
   Input:
       {"resource": "calendar://events/month"}
   Output:
       List of events in JSON format for the current month.

5. Example Prompt Call:
   Input:
       {"prompt": "greet_user", "input": {"name": "Alice", "style": "friendly"}}
   Output:
       AI-generated greeting or instruction based on the prompt.

--------------------------------------------------------------
Options / Use Cases
--------------------------------------------------------------

- Tools:
    - Example: "add", "create_calendar_event"
    - Perform actions or modify data.

- Resources:
    - Example: "calendar://events/month", "calendar://events/{date}"
    - Fetch data dynamically and display results.

- Prompts:
    - Example: Generate greetings or AI instructions interactively.
    - Can be used for testing or development of AI-assisted tasks.

- Advantages of STDIO Transport:
    - Extremely simple to use—no network setup required.
    - Ideal for debugging, testing, or local automation scripts.
    - Direct terminal interaction gives immediate feedback.

- Limitations:
    - Local only; cannot be accessed remotely.
    - Not suitable for web or mobile app integration.
    - Not real-time for multiple clients simultaneously.

--------------------------------------------------------------
Notes
--------------------------------------------------------------
- All requests must be in JSON format.
- STDIO is synchronous: input → process → output.
- Best used during development or for small-scale local automation.
- For networked or streaming use cases, consider "streamable-http" or "sse" transport.
"""

from server import mcp

if __name__ == "__main__":
    # Run the MCP server with STDIO transport
    # Input and output happen directly in the terminal/command-line
    mcp.run(transport="stdio")
