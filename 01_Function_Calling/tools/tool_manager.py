from tools.get_todo_list_tool import GetTodoListTool

class ToolManager:
  def __init__(self):
    pass

  def get_tools_definition(self):
    tools = [
      {
        "type": "function",
        "function": GetTodoListTool.get_tool_definition()
      }
    ]

    return tools
  
  def execute_tool(self, tool_name):
    if tool_name == "GetTodoListTool":
      tool = GetTodoListTool()
      return tool()
    else:
      raise Exception("Tool not found")
  
