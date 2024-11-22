from openai import AzureOpenAI
from tools.tool_manager import ToolManager
from prompts.prompt_manager import PromptManager

class ToDoAgent:
  def __init__(self, aoai_endpoint, aoai_key, aoai_api_version, aoai_deployment):
    self.aoai_client = AzureOpenAI(
      azure_endpoint=aoai_endpoint, 
      api_key=aoai_key, 
      api_version=aoai_api_version, 
    )

    self.aoai_deployment = aoai_deployment

    self.tool_manager = ToolManager()
    self.prompt_manager = PromptManager()

  def chat_compleation(self, messages, tools):
    response = self.aoai_client.chat.completions.create(
      model=self.aoai_deployment,
      messages=messages,
      tools=tools
    )

    return response.choices[0].message

  def execute_agent(self, user_input):
    self.prompt_manager.add_user_prompt(user_input)

    response_msg = self.chat_compleation(
      self.prompt_manager.messages, 
      self.tool_manager.get_tools_definition()
    )
    self.prompt_manager.add_assistant_prompt(response_msg)

    if response_msg.tool_calls is not None and len(response_msg.tool_calls) > 0:
      tool = response_msg.tool_calls[0]

      tool_result = self.tool_manager.execute_tool(tool.function.name)

      self.prompt_manager.add_tool_prompt(tool_result, tool.id)

      final_response = self.chat_compleation(
        self.prompt_manager.messages, 
        self.tool_manager.get_tools_definition()
      )

      self.prompt_manager.add_assistant_prompt(final_response)

      return final_response.content
    else:
      return response_msg.content
      



    