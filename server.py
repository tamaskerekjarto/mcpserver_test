from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server", port=80)

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")