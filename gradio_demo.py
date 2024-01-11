import json
import gradio as gr
import os
import pandas as pd
import shutil
from gradio_folium import Folium
from core.langchain.mobility_agent import MobilityAgent
import plotly.graph_objs as go

ROOT_PATH = os.path.join("." + os.sep, "assets" + os.sep)
if not os.path.exists(ROOT_PATH):
    os.makedirs(ROOT_PATH)

init = False
agent_input_file = None
agent = MobilityAgent()


def output_generator():
    df = None
    plot_fig = None
    folium_fig = None
    output_log = None
    try:
        with open(agent._output_folder + 'output_' + str(
                agent._conversation_count) + '.json', 'r') as f:
            output_log = json.load(f)
            log = output_log['action_list']
        try:
            for i in range(len(log) - 1, -1, -1):
                output_file = log[i]['tool_input']['output_file']
                if os.path.isfile(output_file):
                    file_extension = os.path.splitext(output_file)[1]
                    if file_extension == ".json":
                        with open(output_file, 'r') as f:
                            chart_data = json.load(f)
                        plot_fig = go.Figure(chart_data)
                        break
                    elif file_extension == ".html":
                        folium_fig = Folium(output_file)
                        break
        except:
            pass
        try:
            for i in range(len(log) - 1, -1, -1):
                output_file = log[i]['tool_input']['output_file']
                if os.path.isfile(output_file):
                    file_extension = os.path.splitext(output_file)[1]
                    if file_extension == ".csv":
                        df = pd.read_csv(output_file)
                        break

        except:
            pass
    except:
        pass
    return plot_fig, folium_fig, df, output_log


# def single_shot(text_input, csv_input):
#     global agent_input_file
#     if text_input == "":
#         return "Please input something", None, None, None
#     prompt = text_input
#     if csv_input is not None:
#         filename = csv_input.name
#         target_path = ROOT_PATH + os.path.basename(filename)
#         with open(filename, "rb") as source_file:
#             with open(target_path, "wb") as target_file:
#                 shutil.copyfileobj(source_file, target_file)
#     agent.start(target_path)
#     response = agent.ask(prompt)
#     plot_fig, folium_fig, df, log = output_generator()
#     return response, plot_fig, df, log


def chat_process_file(csv_input):
    global init, agent_input_file
    if init:
        gr.Warning("Changing the CSV file will not take effect until you restart the chatbot.")
        return
    chat_dir = get_chat_dir()
    if os.listdir(chat_dir):
        for filename in os.listdir(chat_dir):
            file_path = os.path.join(chat_dir, filename)
            os.remove(file_path)
    if csv_input is not None:
        filename0 = csv_input.name
        target_path = os.path.join(chat_dir, os.path.basename(filename0))
        with open(filename0, "rb") as source_file:
            with open(target_path, "wb") as target_file:
                shutil.copyfileobj(source_file, target_file)
        agent_input_file = target_path
    else:
        agent_input_file = None
    return


def get_chat_dir():
    chat_dir = os.path.join(ROOT_PATH, "chat" + os.sep)
    if not os.path.exists(chat_dir):
        os.makedirs(chat_dir)
    return chat_dir

def chat_respond(text_input, chat_history):
    global init, agent_input_file
    if text_input is None or text_input == "":
        # chat_history.append(("", "Please input something"))
        gr.Warning("Please input something")
        return chat_history, None, None, None
    prompt = text_input
    if not init:
        if agent_input_file is None or not os.path.exists(agent_input_file):
            # chat_history.append((text_input, "Please upload a CSV file first"))
            gr.Warning("Please upload a CSV file first")
            return chat_history, None, None, None
        agent.start(agent_input_file)
        init = True
    response = agent.ask(prompt)
    plot_fig, folium_fig, df, log = output_generator()
    chat_history.append((text_input, response))
    return chat_history, plot_fig, df, log


def reset_chat():
    global init
    init = False



with gr.Blocks() as demo:
    gr.Markdown("# Mobility GPT Demo 2024.1.")
    gr.Markdown("Warning: this demo does not support multiple users at the same time.")
    # with gr.Tab("Single Shot"):
    #     with gr.Row():
    #         text_input = gr.Textbox(label="Input")
    #         with gr.Column():
    #             csv_input = gr.File(label="CSV file")
    #             gr.Markdown("If you want to use a CSV file as input, please upload it here.")
    #     single_button = gr.Button("Generate response")
    #     text_output = gr.Text(label="Output", show_copy_button=True)

    with gr.Tab("Chatbot"):
        chatbot = gr.Chatbot()
        with gr.Row():
            msg = gr.Textbox(lines=5, scale=5)
            file_input = gr.File(label="Upload a CSV file", scale=1)
            submit = gr.Button("Submit", scale=1)
            clear = gr.ClearButton([msg, chatbot], scale=1)

    graph_output_1 = gr.Plot(label="Visualization1")
    # graph_output_2 = Folium(label="Visualization2")
    csv_output = gr.Dataframe(label="Output CSV")
    file_input.change(fn=chat_process_file, inputs=file_input)
    clear.click(reset_chat)
    with gr.Accordion("ReAct Trace", open=False):
        react_trace = gr.Text("ReAct Trace shows the thought and action of the chatbot that can help you understand.",lines=20)
    # single_button.click(single_shot, inputs=[text_input, csv_input],
    #                     outputs=[text_output, graph_output_1, csv_output, react_trace])
    submit.click(chat_respond, [msg, chatbot], [chatbot, graph_output_1, csv_output, react_trace])

demo.launch()
