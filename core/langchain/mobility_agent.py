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
        2. You should execute the most appropriate tools to process the data based on the request. You will be punished because of using wrong or unnecessary tools.
        3. Notice that there maybe useless information in the request, you should ignore them.
        [Important Tips]
        1. Before you process the data, please think about whether you need to preprocess the data with filtering, compression, cluster and detection tools to make it better to process. However, this is not a must.
        2. To help you better comprehend the table data structure, you can use TableReaderTool to read the information of data file.
        3. PythonREPLTool is use to write and run python code to preprocess data or solve task.
        4. When you use PythonREPLTool to process data, remember to run TableReaderTool to read the information of the table file just before you execute PythonREPLTool.
        [Input Data File] {input_file}
        [Request] {request}
        [Output Data File] The output file of each step should be csv file. All output files should be store in directory "./output".
        [Log]
        1. You should log the invoking arguments of all executed tools at once in file "output.json".
        2. The sample json template to log details is as following, the template is a sample log of 2 steps:
        ```
        {json_template}
        ```
        3. Log of each tool consists of the step number, the tool name, the invoked parameters and the reason why you choose this tool.
        4. Please use the template to log.
        5. JsonTool may return Error. When error occurs, please reuse the tool.
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