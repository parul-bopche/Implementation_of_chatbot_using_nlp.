import streamlit as st


Home=st.Page(
    page="Pages/welcome.py",
    title="Home",
    icon="🏠"
)
Chat_Bot=st.Page(
    page="Pages/Bot.py",
    title="Chat_bot",
    icon="⁉️"
)
Chat_History=st.Page(
    page="Pages/history.py",
    title="Chat_History",
    icon="🕒"
)
About=st.Page(
    page="Pages/overview.py",
    title="About",
    icon="🧠"
)
Socials=st.Page(
    page="Pages/socials.py",
    title="Socials",
    icon="🌐"
)

pages=st.navigation([Home,Chat_Bot,Chat_History,About,Socials])
pages.run()