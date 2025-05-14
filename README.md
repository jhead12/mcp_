# MCP - Model Context Protocol SDK

<div align="center">

<strong>Python implementation of the Model Context Protocol (MCP)</strong>

[![PyPI](https://img.shields.io/pypi/v/mcp.svg)](https://pypi.org/project/mcp/)
[![MIT licensed](https://img.shields.io/pypi/l/mcp.svg)](https://github.com/modelcontextprotocol/python-sdk/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/mcp.svg)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-modelcontextprotocol.io-blue.svg)](https://modelcontextprotocol.io)
[![Specification](https://img.shields.io/badge/spec-spec.modelcontextprotocol.io-blue.svg)](https://spec.modelcontextprotocol.io)
[![GitHub Discussions](https://img.shields.io/github/discussions/modelcontextprotocol/python-sdk)](https://github.com/modelcontextprotocol/python-sdk/discussions)

</div>

## Overview

The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to:

- Build MCP clients that can connect to any MCP server
- Create MCP servers that expose resources, prompts and tools
- Use standard transports like stdio and SSE
- Handle all MCP protocol messages and lifecycle events

## Installation

### Adding MCP to your python project

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects. In a uv managed python project, add mcp to dependencies by:

```bash
uv add "mcp[cli]"
```

Alternatively, for projects using pip for dependencies:
```bash
pip install mcp
```

### Running the standalone MCP development tools

To run the mcp command with uv:

```bash
uv run mcp
```

## Quickstart

Let's create a simple MCP server that exposes a calculator tool and some data:

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

You can install this server in [Claude Desktop](https://claude.ai/download) and interact with it right away by running:
```bash
mcp install server.py
```

Alternatively, you can test it with the MCP Inspector:
```bash
mcp dev server.py
```

## Documentation

For complete documentation, visit [modelcontextprotocol.io](https://modelcontextprotocol.io).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.