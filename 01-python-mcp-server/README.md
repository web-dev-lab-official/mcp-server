# 🧠 MCP Server Tutorial (Python + uv)

A simple and modern MCP (Model Context Protocol) server built with **Python**, **uv**, and **FastMCP**.
This project helps you understand how MCP works and how to run your own server locally.

---

## 🚀 What is MCP?

**MCP (Model Context Protocol)** is an open standard that lets AI applications (like Claude or ChatGPT) connect to:

- 🔧 Tools (calculators, search engines, file operations)
- 📂 Data sources (local files, databases, APIs)
- 🤖 Workflows & prompts

Think of MCP like **USB-C for AI** — a universal way for AI models to connect to external systems.

---

## 💡 What Can You Build With MCP?

- AI agents that access Google Calendar, Notion, or your local system
- Claude Code tools that generate applications from Figma designs
- Chatbots connected to company databases
- AI-driven creative tools (3D modeling, automation, etc.)

---

## 🏗 Architecture Overview

MCP uses a simple **client–server** model:

- **MCP Host** → AI app (Claude Desktop, Claude Code, etc.)
- **MCP Client** → Connects the host to a server
- **MCP Server** → Provides tools, resources, prompts, and data

Your job as a developer is to **build the MCP server**.

---

## Transport layer

The transport layer manages communication channels and authentication between clients and servers. It handles connection establishment, message framing, and secure communication between MCP participants.

- **MCP supports two transport mechanisms:**

  1. Stdio transport: Uses standard input/output streams for direct process communication between local processes on the same machine, providing optimal performance with no network overhead.
  2. Streamable HTTP transport: Uses HTTP POST for client-to-server messages with optional Server-Sent Events for streaming capabilities. This transport enables remote server communication and supports standard HTTP authentication methods including bearer tokens, API keys, and custom headers. MCP recommends using OAuth to obtain authentication tokens.
  3. SSE allows the server to push events to the client over a persistent HTTP connection.

  | Feature       | STDIO                       | HTTP (Streamable)           | SSE                         |
  | ------------- | --------------------------- | --------------------------- | --------------------------- |
  | Access        | Local only                  | Local & Network             | Local & Network             |
  | Communication | Request → Response          | Request → Response / Stream | Server → Client (push)      |
  | Real-time     | No                          | Partial (with streamable)   | Yes                         |
  | Complexity    | Low                         | Medium                      | Medium-High                 |
  | Ideal for     | Development, testing        | APIs, web/mobile clients    | Live updates, notifications |
  | Bidirectional | Yes (via input/output)      | Yes (request/response)      | No                          |
  | Use with MCP  | Quick tool/resource testing | Full app integration        | Streaming events/resources  |

---

## Primitives

MCP primitives are the most important concept within MCP. They define what clients and servers can offer each other. These primitives specify the types of contextual information that can be shared with AI applications and the range of actions that can be performed.

- **MCP defines three core primitives that servers can expose:**

  1. Tools: Executable functions that AI applications can invoke to perform actions (e.g., file operations, API calls, database queries)
  2. Resources: Data sources that provide contextual information to AI applications (e.g., file contents, database records, API responses)
  3. Prompts: Reusable templates that help structure interactions with language models (e.g., system prompts, few-shot examples)

- **MCP also defines primitives that clients can expose. These primitives allow MCP server authors to build richer interactions.**
  1. Sampling: Allows servers to request language model completions from the client’s AI application. This is useful when servers’ authors want access to a language model, but want to stay model independent and not include a language model SDK in their MCP server. They can use the sampling/complete method to request a language model completion from the client’s AI application.
  2. Elicitation: Allows servers to request additional information from users. This is useful when servers’ authors want to get more information from the user, or ask for confirmation of an action. They can use the elicitation/request method to request additional information from the user.
  3. Logging: Enables servers to send log messages to clients for debugging and monitoring purposes.

---

## Understanding MCP servers

MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces.
Common examples include file system servers for document access, database servers for data queries, GitHub servers for code management, Slack servers for team communication, and calendar servers for scheduling.

---

## Using with Cursor, Gemini, etc.

MCP servers are transport-agnostic; any client that speaks MCP protocol can use your tools/resources.
Example clients:
Cursor (terminal/CLI): can call tools/resources via command line.
Gemini (or any Gemini browser): you can expose the streamable-http transport and consume it.
Other use cases:
Slack or Discord bots: call MCP tools as backend actions.
Web apps: use HTTP transport to integrate calendar events dynamically.
Local automation: use stdio transport for scripts.

---

## Google Calender

Create a Python command-line application that makes requests to the Google Calendar API.
In the Google Cloud console, enable the Google Calendar API.

- [Python quickstart](https://developers.google.com/workspace/calendar/api/quickstart/python)
- [Service account](https://docs.cloud.google.com/iam/docs/service-account-overview)
- [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/)

---

# 📦 Project Setup (Using uv)

### 1️⃣ Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2️⃣ Create a new project

```bash
uv init mcp-server-demo
cd mcp-server-demo
```

### 3️⃣ Add MCP dependency

```bash
uv add "mcp[cli]"
```

### 4️⃣ Create the server file

Create `server.py` and add your FastMCP code.

### 5️⃣ Run the server

```bash
rm -rf token.json
uv run auth.py
uv run server.py
```

The MCP server will start at:

```
http://localhost:8000/mcp
```

---

# 🧪 Testing Your MCP Server

### ✔ Using MCP Inspector

Open a second terminal:

```bash
uv run mcp dev server.py
```

Connect to:

```
http://localhost:8000/mcp
```

### ✔ Using Claude Code

```bash
claude mcp add --transport http local-mcp http://localhost:8000/mcp
```

---

# 🔧 Useful uv Commands

| Task                 | Command          |
| -------------------- | ---------------- |
| Install dependencies | `uv add PACKAGE` |
| Lock dependencies    | `uv lock`        |
| Sync dependencies    | `uv sync`        |
| Run Python file      | `uv run file.py` |
| Create venv manually | `uv venv`        |

---

# 🗂 Example Commands Used in This Project

```bash
uv init .
uv add "mcp[cli]"
uv run server.py
npx -y @modelcontextprotocol/inspector
uv lock
uv sync
```

---

# 📚 Resources

- 🎥 **Video Tutorial:** [https://www.youtube.com/@web-dev-lab](https://www.youtube.com/@web-dev-lab)
- 📝 **Written Guide:** [https://blog.webdevlab.org](https://blog.webdevlab.org)
- 💻 **Source Code:** [https://github.com/web-dev-lab-official/mcp-server](https://github.com/web-dev-lab-official/mcp-server)
 - **Official Docs** [https://github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
