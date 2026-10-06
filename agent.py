import json

from tools import AVAILABLE_TOOLS, TOOL_SCHEMAS

import streamlit as st
from groq import Groq

def dispatch(name, arguments, confirmed=False):
    """Safely run one approved tool."""

    if name not in AVAILABLE_TOOLS:
        return f"Error: no tool named {name} exists."

    if name == "book_room" and not confirmed:
        return (
            "Confirmation required before booking this room. "
            "No booking was made."
        )

    function = AVAILABLE_TOOLS[name]

    try:
        return str(function(**arguments))
    except TypeError as error:
        return f"Error: wrong arguments for {name}. {error}"
    except Exception as error:
        return f"Error: {name} failed. {error}"

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def run_agent(messages, confirmed=False):
    """Let the model call tools until it produces a final answer."""

    tool_log = []

    for _ in range(5):
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content, tool_log

        messages.append(message)

        for call in message.tool_calls:
            name = call.function.name

            try:
                arguments = json.loads(call.function.arguments)
            except json.JSONDecodeError as error:
                result = f"Error: malformed JSON arguments. {error}"

                tool_log.append({
                    "name": name,
                    "arguments": call.function.arguments,
                    "result": result,
                })

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result,
                })

                continue

            result = dispatch(
                name,
                arguments,
                confirmed=confirmed,
            )

            tool_log.append({
                "name": name,
                "arguments": arguments,
                "result": result,
            })

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(result),
            })

    return (
        "I was not able to finish that request after five tool-call rounds.",
        tool_log,
    )