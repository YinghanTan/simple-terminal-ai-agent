from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from textwrap import dedent

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel

from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider

load_dotenv()

llm = os.getenv("LLM_MODEL", "deepseek-coder")

model = OpenAIChatModel(
    llm,
    provider=DeepSeekProvider(api_key=os.getenv("DEEPSEEK_API_KEY")),
)

SYSTEM_PROMPT = dedent(
    """\
    You are a professional developer specializing in shell commands.
    Your task is to generate the correct shell commands based on the
    user's request.

    IMPORTANT: ALWAYS USE THE SAME LANGUAGE AS THE USER PROMPT IN
    YOUR RESPONSE.

     Process:

    1. Think Aloud: Use the `think` function to explain your reasoning.
    Justify why you chose a particular command, considering efficiency,
    safety, and best practices.

    2. Provide the Final Command: Use the `answer` function to present
    the final shell command concisely.
"""
)

@dataclass
class Answer:
    success: bool
    cmd: str | None
    failure: str | None


agent = Agent(
    # model=GoogleModel("gemini-2.0-flash"),
    model,
    system_prompt=SYSTEM_PROMPT,
    output_type=Answer,
)


@agent.tool_plain
def think(s: str) -> None:
    """Communicate your thought process to the user.

    Args:
        s (str): A description of your reasoning or decision-making process.
    """
    print(f"(AI Thinking): {s}\n")


@agent.tool_plain
def answer(success: bool, cmd: str | None, failure: str | None) -> Answer:
    """Provide the final shell command or explain why it couldn't be generated.

    Args:
        success (bool): Indicates whether a shell command was successfully generated.
        cmd (str | None): The generated shell command if `success` is True.
            It must be a single-line command. If `success` is False, this should be None.
        failure (str | None): If `success` is False, provide a reason why the command
            could not be generated. If `success` is True, this should be None.

    Returns:
        Answer: A structured response that will be processed for the user.
    """
    return Answer(success, cmd, failure)


def main() -> None:
    user_prompt = " ".join( sys.argv[1:])  # for english join with a space, for chinese no need space
    if len(user_prompt) == 0:
        print("No prompts")
        sys.exit(1)

    resp = agent.run_sync(user_prompt)
    ans = resp.output
    if ans.success and ans.cmd is not None:
        print(f"(AI Answer): {ans.cmd}")
        y_or_n = input("Execute? Y/N: ")
        if y_or_n in ["y", "Y"]:
            os.system(ans.cmd)
    else:
        print(f"(AI Answer): {ans.failure}")
        print("Generate failed")


if __name__ == "__main__":
    main()
