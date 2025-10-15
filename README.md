# simple-terminal-ai-agent

A simple terminal ai agent to help with terminal commands

## Project Setup

- install uv if you don't have it yet
`curl -LsSf https://astral.sh/uv/install.sh | sh`
`uv --version`

- clone the project
```
git clone git@github.com:YinghanTan/simple-terminal-ai-agent.git
cd simple-terminal-ai-agent
```

- install dependencies
```
uv sync
```
- create .env file from example.env by adding your DEEPSEEK_API_KEY

- run
```
uv run main.py list all md files
uv run main.py what is the name of my os
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


- uninstall ai tool
```
uv tool list
uv tool uninstall ai
uv tool list
```
