from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="SimpleEchoServer", stateless_http=True)

@mcp.tool(description="A simple Echoing tool which echos an input message in string.")
def echo_string(msg: str) -> str:
    print(f"Echoing {msg}")
    return f"Echo: {msg}"