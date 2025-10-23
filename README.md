# simple-terminal-ai-agent

A simple terminal ai agent to help with terminal commands


## Project Setup

- install uv if you don't have it yet
```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```

- clone the project
```
git clone git@github.com:YinghanTan/simple-terminal-ai-agent.git
cd simple-terminal-ai-agent
```

- create .env file from example.env by adding your DEEPSEEK_API_KEY or GEMINI_API_KEY
    -  Instructions to generate GEMINI_API_KEY - https://www.youtube.com/watch?v=o8iyrtQyrZM
    -  Instructions to generate DEEPSEEK_API_KEY - https://www.youtube.com/watch?v=CpZFf6JkHgY


- install dependencies
```
uv sync
```

- run
```
uv run ai.py list all md files
uv run ai.py what is the name of my os
```


- build
```
uv build
```

- install as tool
```
uv tool install dist/ai-0.1.0-py3-none-any.whl
uv tool list
```
- test installed ai tool
```
ai how much ram do i have
ai find out how much space i have left
ai tar gz README.md
ai show a nice list of git commits with graphs and dates
```

- uninstall ai tool
```
uv tool list
uv tool uninstall ai
uv tool list
```
