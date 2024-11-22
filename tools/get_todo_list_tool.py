
import json

class GetTodoListTool:
  def __init__(self):
    pass

  def __call__(self) -> str:
    todo_list = [
      {
        "id": 1,
        "title": "Test Todo 1",
        "description": "This a description for a test todo",
        "is_done": False
      },
      {
        "id": 2,
        "title": "Test Todo 2",
        "description": "This a description for a test todo",
        "is_done": False
      },
      {
        "id": 3,
        "title": "Test Todo 3",
        "description": "This a description for a test todo",
        "is_done": False
      }
    ]

    return json.dumps(todo_list, indent=2)
  
  @staticmethod
  def get_tool_definition() -> dict[str, any]:
    definition = {
      "name": "GetTodoListTool",
      "description": "Call this whenever you want to list up the To Dos."
    }

    return definition