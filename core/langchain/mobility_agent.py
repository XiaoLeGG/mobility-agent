from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from core.langchain.tool_manager import collect_tools

class MobilityAgent():

    def __init__(self):

        self._llm = ChatOpenAI(temperature=0)
        self._tools = collect_tools()
        self._agent = initialize_agent(
            self._tools, self._llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True,
            return_intermediate_steps=True
        )

        self._json_template = """
        {
            "step": 1,
            "tool": "tool1",
            "parameters": {
                "args1": "value1",
                "args2": "value2"
            },
            "thought": "reason",
        },
        {
            "step": 2,
            "tool": "tool2",
            "parameters": {
                "args1": "value1",
                "args2": "value2"
            },
            "thought": "reason",
        },
        """

        self._prompt = """
        [Role]
        1. You are a spatio-temporal data analyst.
        2. You should choose the most appropriate tools to process the data based on the request. You will be punished because of using wrong or unnecessary tools.
        3. If the provided tools are not enough to solve the problem, you can ask for more tools, instead of using wrong tools.
        4. Notice that there maybe useless information in the request, you should ignore them.
        [Input Data File] {input_file}
        [Request] {request}
        [Output Data File] The output file of each step should be csv file. All output files should be store in directory "./output".
        [Last Step]
        1. You should invoke json tool at last to store all the details. The output file should be "output.json".
        2. The sample json template to store details is as following:
        ```
        {json_template}
        ```
        Description:
        - step: The step number of the tool.
        - tool: The name of the tool.
        - parameters: The invoked parameters of the tool.
        - thought: The reason why you choose this tool.
        3. You should store all steps in one json file as same as the json template above.
        """

    def ask(self, input_file, request):
        """Ask the agent to solve the problem.

        Parameters
        ----------
        input_file : str
            The data file path to be processed.
        request : str
            The request of the user.

        Returns
        -------
        str
            The output file path.
        """
        prompt = self._prompt.format(input_file=input_file, request=request, json_template=self._json_template)
        response = self._agent({
            "input": prompt,
        })
        return response["output"]