from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, ZeroShotAgent, Tool, AgentExecutor, initialize_agent
from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate
from core.langchain.tool_manager import collect_tools
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
class MobilityAgent():

    def __init__(self):

        self._llm = ChatOpenAI(temperature=0, model="gpt-4")
        self._tools = collect_tools()

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

        # self._prompt = """
        # [Role]
        # 1. You are a spatio-temporal data analyst.
        # 2. You should execute the most appropriate tools to process the data based on the request. You will be punished because of using wrong or unnecessary tools.
        # 3. Notice that there maybe useless information in the request, you should ignore them.
        # [Important Tips]
        # 1. Before you process the data, please think about whether you need to preprocess the data with filtering, compression, cluster and detection tools to make it better to process. However, this is not a must.
        # 2. To help you better comprehend the table data structure, you can use TableReaderTool to read the information of data file.
        # 3. PythonREPLTool is use to write and run python code to preprocess data or solve task.
        # 4. When you use PythonREPLTool to process data, remember to run TableReaderTool to read the information of the table file just before you execute PythonREPLTool.
        # [Input Data File] {input_file}
        # [Request] {request}
        # [Output Data File] The output file of each step should be csv file. All output files should be store in directory "./output".
        # [Log]
        # 1. You should log the invoking arguments of all executed tools at once in file "output.json".
        # 2. The sample json template to log details is as following, the template is a sample log of 2 steps:
        # ```
        # {json_template}
        # ```
        # 3. Log of each tool consists of the step number, the tool name, the invoked parameters and the reason why you choose this tool.
        # 4. Please use the template to log.
        # 5. JsonTool may return Error. When error occurs, please reuse the tool.
        # """

        self._prompt = """Here are some information you need to know before our work:
        [ROLE] You are a spatio-temporal data analyst. You are knowledged about the mobility data analysing.
        [HANDLING STEPS]
        1. Analyse the main idea of the request and the data features mentioned in the request.
        2. Think about how to solve the request and make a plan.
        3. Carefully choosing the parameters of each tool in the plan with considering the data features.
        4. Execute the plan with the tools to solve the request.
        5. Store and log the details of execution details in json format in the file "output.json" which is in the output folder. The log format is in following [LOG FORMAT] part.
        [OUTPUT DATA FILE] Every output file should be csv file.
        [OUTPUT FOLDER] "output/"
        [INITIAL DATA FILE] {input_file}
        [LOG FORMAT]
        1. Log template for 2 steps (you can imitate this template to add more):
        ```
        {json_template}
        ```
        2. Log fields for each step in json:
        - step: The step number of the tool.
        - tool: The name of the tool.
        - parameters: The parameters of the tool.
        - thought: The reason why you choose this tool.
        3. Tips:
        - Tool "json" may return Error. When error occurs, please reuse the tool.
        [PLAN MAKING TIPS]
        1. Preprocess the data when you think it is necessary.
        2. Write your personal codes with PythonREPLTool when there is no tool able to solve the request but remember to run TableReaderTool to read the information of the table file to help you better write codes.
        3. For PythonREPLTool, you should store the processed data in a csv file for the next step to use.
        4. Remember to consider the data features memtioned in the request when choosing parameters.
        5. The seperate symbols of the data file is ",".
        """

        # self._suffix="""

        # [CHAT_HISTORY]
        # {memory}
        # [REQUEST] {request}
        # {agent_scratchpad}
        # """

        # self._zero_shot_prompt = ZeroShotAgent.create_prompt(
        #     tools=self._tools,
        #     prefix=self._prompt,
        #     suffix=self._suffix,
        #     input_variables=["input_file", "request", "memory", "agent_scratchpad"],
        # )

        self._agent_memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
        # self._llm_chain = LLMChain(llm=self._llm, prompt=self._zero_shot_prompt)
        # self._agent = ZeroShotAgent(
        #     llm_chain=self._llm_chain,
        #     tools=self._tools,
        #     verbose=True
        # )
        self._agent = initialize_agent(
            tools=self._tools,
            llm=self._llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True,
            agent_kwargs = {
                'extra_prompt_messages': [MessagesPlaceholder(variable_name="memory")]
            },
            memory=self._agent_memory,
            handle_parsing_errors=lambda e: "Error occurs, you may use table reader to exam the data: " + str(e),
        )

        self._is_started = False
    
    def start(self, input_file):
        """Start the agent.
        
        Parameters
        ----------
        input_file : str
            The initial data file path to be processed.
        
        """
        self._is_started = True
        response = self._agent.run(self._prompt.format(input_file=input_file, json_template=self._json_template))
        return response

    def ask(self, request):
        """Ask the agent to solve the problem.

        Parameters
        ----------
        request : str
            The request of the user.

        Returns
        -------
        str
            The output file path.
        """
        if not self._is_started:
            raise Exception("Please start the agent first.")
        response = self._agent.run(request)
        return response