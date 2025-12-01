# 🧠 MCP Server Tutorial (Python + uv)

A simple and modern MCP (Model Context Protocol) server built with **Python**, **uv**, and **FastMCP**.
This project helps you understand how MCP works and how to run your own server locally.

---

## 🚀 What is MCP?

**MCP (Model Context Protocol)** is an open standard that lets AI applications (like Claude or ChatGPT) connect to:

* 🔧 Tools (calculators, search engines, file operations)
* 📂 Data sources (local files, databases, APIs)
* 🤖 Workflows & prompts

Think of MCP like **USB-C for AI** — a universal way for AI models to connect to external systems.

---

## 💡 What Can You Build With MCP?

* AI agents that access Google Calendar, Notion, or your local system
* Claude Code tools that generate applications from Figma designs
* Chatbots connected to company databases
* AI-driven creative tools (3D modeling, automation, etc.)

---

## 🏗 Architecture Overview

MCP uses a simple **client–server** model:

* **MCP Host** → AI app (Claude Desktop, Claude Code, etc.)
* **MCP Client** → Connects the host to a server
* **MCP Server** → Provides tools, resources, prompts, and data

Your job as a developer is to **build the MCP server**.

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

Create `main.py` and add your FastMCP code.

### 5️⃣ Run the server

```bash
uv run main.py
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
uv run mcp dev main.py
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
uv run main.py
npx -y @modelcontextprotocol/inspector
uv lock
uv sync
```

---

# 📚 Resources

* 🎥 **Video Tutorial:** [https://www.youtube.com/@web-dev-lab](https://www.youtube.com/@web-dev-lab)
* 📝 **Written Guide:** [https://blog.webdevlab.org](https://blog.webdevlab.org)
* 💻 **Source Code:** [https://github.com/web-dev-lab-official/mcp-server](https://github.com/web-dev-lab-official/mcp-server)

