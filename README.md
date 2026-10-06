# Assignment 7: Agent with Tools

This project is a Streamlit study room assistant that uses an LLM agent with three tools: checking room availability, checking opening hours, and booking a room.

## How to run

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Tool safety

I deliberately did not create a `delete_all_bookings` function. A function like that could erase reservation data if it were called accidentally or maliciously.

If the model requests a tool that does not exist, the dispatch function checks the requested name against `AVAILABLE_TOOLS` before performing any lookup. It returns an error instead of executing anything. The `test_unknown_tool_is_rejected` test verifies this behavior.

A vague tool description would be:

`Check room availability.`

I improved it to:

`Check which study rooms are available on a given weekday. Use this whenever a student asks which rooms are free.`

The improved description tells the model when it should call the tool instead of only describing what the function does.