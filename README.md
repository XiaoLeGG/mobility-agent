# MobilityAgent
Mobility-Agent is an agent based on LLM(Large Language Model) implementing Langchain framework, targeting at automatically completing spatio-temporal trajectories analysis tasks through conversation.

**Paper:** []

# Install

```
git clone https://github.com/XiaoLeGG/mobility-agent.git
cd mobility-agent
conda create -n mobility-agent --file requirements.txt
```

# Run

Before running, you need to set your openai api key to environment variables "OPENAI_API_KEY".
Also you can set other environment variables like "HTTP_PROXY" or "HTTPS_PROXY" to use proxy.

```
python gradio_demo.py
```

# Reference
```
@misc{MobilityAgent2023,
    title={MobilityAgent},
    author={Tianle Lun, Yicheng Tao, Junyou Su, He Zhu, Zipei Fan},
    howpublished = {\url{https://github.com/XiaoLeGG/mobility-agent}},
    year={2023}
}
```
