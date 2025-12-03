# server_http.py

"""
MCP Server using Streamable HTTP Transport

This file runs the MCP server and exposes a Streamable HTTP endpoint,
allowing clients to interact with your tools, resources, and prompts
over HTTP. Streamable HTTP supports sending partial responses as they
are generated, which is useful for long-running tasks or dynamic data.

--------------------------------------------------------------
How to Connect to the Streamable HTTP MCP Server
--------------------------------------------------------------

1. Start the server:
   Run this file in your terminal:
       $ python server_http.py
   By default, the server will be hosted at:
       http://localhost:8000/mcp

2. Call a Tool
   Tools perform actions (like 'add' or 'create_calendar_event').

   Example using Python `requests`:
       import requests
       data = {"tool": "add", "input": {"a": 5, "b": 7}}
       response = requests.post("http://localhost:8000/mcp", json=data)
       print(response.json())

   Example using curl:
       curl -X POST http://localhost:8000/mcp \
            -H "Content-Type: application/json" \
            -d '{"tool":"add","input":{"a":5,"b":7}}'

3. Call a Resource
   Resources are queryable endpoints that return data.

   Example: Fetch all events of the month
       import requests
       data = {"resource": "calendar://events/month"}
       response = requests.post("http://localhost:8000/mcp", json=data)
       print(response.json())

4. Call a Resource with Parameters
   Example: Fetch events on a specific date
       import requests
       data = {"resource": "calendar://events/2025-12-05"}
       response = requests.post("http://localhost:8000/mcp", json=data)
       print(response.json())

5. Streamable Responses
   - For long-running or large responses, Streamable HTTP sends
     data in chunks as it is generated.
   - Example in JavaScript (Browser):
       const evtSource = new EventSource("http://localhost:8000/mcp/stream");
       evtSource.onmessage = (event) => console.log("Chunk:", event.data);
       evtSource.onerror = (err) => console.error(err);

--------------------------------------------------------------
Options / Use Cases
--------------------------------------------------------------

- Tools:
    - Example: "add", "create_calendar_event"
    - Actions triggered by client requests.

- Resources:
    - Example: "calendar://events/month", "calendar://events/{date}"
    - Fetch data dynamically from your server.

- Prompts:
    - Example: Greeting prompts or AI-generated instructions
    - Can be used to generate natural-language instructions dynamically.

- Streamed Output:
    - Useful for AI or GPT-like responses.
    - Useful for long calendar queries or logs.
    - Real-time updates without waiting for full response.

- Integration:
    - Web dashboards
    - Mobile apps
    - Automation scripts
    - Chatbots (Discord, Slack, etc.)

--------------------------------------------------------------
Notes
--------------------------------------------------------------
- JSON format is required for all POST requests.
- Dynamic resources with parameters may require URL encoding.
- You can customize host/port by passing parameters to mcp.run().
- Streamable HTTP is ideal when partial, real-time responses are needed.
"""

from server import mcp

if __name__ == "__main__":
    # Run the MCP server with streamable HTTP transport
    # Clients can connect via HTTP to send tool/resource requests
    mcp.run(transport="streamable-http")
