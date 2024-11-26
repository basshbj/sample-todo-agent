import json

class PromptManager:
  def __init__(self):
    self.messages = []

    self.__load_sys_prompt()

  def __load_sys_prompt(self):
    with open("prompts/sys_prompt.txt", "r") as f:
      self.messages.append({
        "role": "system",
        "content": f.read()
      })

  def add_user_prompt(self, user_prompt):
    self.messages.append({
      "role": "user",
      "content": user_prompt
    })

  def add_assistant_prompt(self, message):
    self.messages.append(message)

  def add_tool_prompt(self, tool_exec_result, tool_call_id):
    self.messages.append({
      "role": "tool",
      "content": tool_exec_result,
      "tool_call_id": tool_call_id
    })
    