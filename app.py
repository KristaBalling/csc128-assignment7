import streamlit as st

from agent import run_agent


st.set_page_config(
    page_title="Study Room Agent",
    page_icon="📚",
)

st.title("Study Room Agent")
st.write(
    "Ask about study room availability, opening hours, "
    "or request a room booking."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "tool_log" not in st.session_state:
    st.session_state.tool_log = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

confirmed = st.checkbox("I confirm any room booking I request.")

prompt = st.chat_input("Ask about rooms or request a booking")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response, tool_log = run_agent(
        st.session_state.messages.copy(),
        confirmed = confirmed
    )

    st.session_state.tool_log.extend(tool_log)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
    })

    with st.chat_message("assistant"):
        st.markdown(response)

    st.subheader("Tool Call Log")

    for entry in st.session_state.tool_log:
        st.write("Tool:", entry["name"])
        st.write("Arguments:", entry["arguments"])
        st.write("Result:", entry["result"])
        st.divider()