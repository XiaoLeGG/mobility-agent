from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.prompts import MessagesPlaceholder
from core.langchain.callback_manager import MACallbackHandler
from core.langchain.tool_manager import collect_tools
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

class MobilityAgent():

    def __init__(self):
        self._mcbh = MACallbackHandler()
        self._cb = CallbackManager([StdOutCallbackHandler(), self._mcbh])
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

        self._prompt = """Here are some information you need to know before our work:
        [ROLE] You are a spatio-temporal data analyst. You are knowledged about the mobility data analysing.
        [HANDLING STEPS]
        1. Analyse the main idea of the request and the data features mentioned in the request.
        2. Think about how to solve the request and make a plan.
        3. Carefully choosing the parameters of each tool in the plan with considering the data features.
        4. Execute the plan with the tools to solve the request.
        [OUTPUT DATA FILE] Every output file should be csv file.
        [OUTPUT FOLDER] "output/"
        [INITIAL DATA FILE] {input_file}
        [PLAN MAKING TIPS]
        1. Preprocess the data when you think it is necessary.
        2. Write your personal codes with PythonREPLTool when there is no tool able to solve the request but remember to run TableReaderTool to read the information of the table file to help you better write codes.
        3. For PythonREPLTool, you should store the processed data in a csv file for the next step to use.
        4. Remember to consider the data features memtioned in the request when choosing parameters.
        5. The seperate symbols of the data file is ",".
        [MISTAKES YOU MAY MAKE]
        1. Overestimate the function of tools. Each tool should have been considered its parameters for better estimating its function when you choose it.
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
            callback_manager=self._cb,
            agent_kwargs = {
                'extra_prompt_messages': [MessagesPlaceholder(variable_name="memory")]
            },
            memory=self._agent_memory,
            handle_parsing_errors=lambda e: "Error occurs, you may check the existance of file and use table reader to check the data: " + str(e),
        )

        self._is_started = False
    
    def start(self, input_file: str):
        """Start the agent.
        
        Parameters
        ----------
        input_file : str
            The initial data file path to be processed.
        
        """
        self._is_started = True
        response = self._agent.run(self._prompt.format(input_file=input_file, json_template=self._json_template))
        return response

    def ask(self, request: str):
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