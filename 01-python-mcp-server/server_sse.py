# server_sse.py
"""
Run the MCP server using SSE (Server-Sent Events) transport.
Useful for streaming real-time updates from tools/resources to clients.
"""

from server import mcp

if __name__ == "__main__":
    # Run MCP server with SSE transport
    # Clients can subscribe to the SSE endpoint to receive live updates
    mcp.run(transport="sse")
