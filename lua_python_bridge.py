# file: lua_python_bridge.py
from lupa import LuaRuntime

# Initialize Lua environment
lua = LuaRuntime(unpack_returned_tuples=True)

# Load the Lua script
lua.execute('dofile("command_processor.lua")')

# Call the Lua function from Python
process_command = lua.globals().process_command

# Test Lua function call
response = process_command("Open browser")
print(response)
