from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="SimpleMathServer", stateless_http=True)

@mcp.tool(description="A smiple add tool which adds number 2 to an integer input value and returns the result in integer.")
def add_two(n: int) -> int:
    return n + 2

