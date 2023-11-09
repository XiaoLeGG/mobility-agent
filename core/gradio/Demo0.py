import os
os.system("pip freeze > requirements.txt")
import gradio as gr
import random
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from core.langchain.compression_tool import CompressionTool
from core.langchain.filtering_tool import FilteringTool
from core.langchain.stop_detection_tool import StopDetectionTool

llm = ChatOpenAI(temperature=0)
tools = [CompressionTool(), FilteringTool(), StopDetectionTool()]
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True,
    return_intermediate_steps=True
)


def single_shot(text_input, csv_input):
    # 指定要保存的文件名
    filename = csv_input.name
    # 检查文件是否已经存在，如果存在则不覆盖
    if not os.path.exists(filename):
        # 将文件内容写入到文件中
        with open(filename, 'wb') as f:
            f.write(csv_input)
    response = agent({
        "input": (text_input+"The input file path is \""+filename+"\",please output a csv file as \"output.csv\".")
    })
    print(response["intermediate_steps"])
    df = pd.read_csv('output.csv')
    return response["output"], None, df


def random_response(message, history):
    return random.choice(["Yes", "No"])


with gr.Blocks() as demo:
    gr.Markdown("# Mobility AI Demo 11.9")
    with gr.Tab("Single Shot"):
        with gr.Row():
            text_input = gr.Textbox(label="Input")
            csv_input = gr.File(label="CSV file")
        with gr.Row():
            text_output = gr.Text(label="Output")
            graph_output = gr.Plot(label="Visualization")
        csv_output = gr.Dataframe(label="Output CSV")
        single_button = gr.Button("Generate response")
    with gr.Tab("Chatbot"):
        chatbot = gr.ChatInterface(random_response, additional_inputs=gr.File(label="CSV file"))
        chat_button = gr.Button("Show Visualization")
        graph_output2 = gr.Plot(label="Visualization")

    with gr.Accordion("Developer"):
        gr.Markdown("LunTianLe TaoYiCheng SuJunYou")

    single_button.click(single_shot, inputs=[text_input, csv_input], outputs=[text_output, graph_output,csv_output])

demo.launch()
