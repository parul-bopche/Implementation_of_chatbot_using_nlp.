import streamlit as st


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## Welcome to Your Personal Health Companion!
    
    This tool is designed to assist you with:
    - Identifying potential health concerns
    - Offering symptom-based guidance
    - Providing wellness tips and recommendations
    
    ### How to Use
    1. Enter your symptoms in the chat box below.
    2. Receive potential insights based on your input.
    3. Explore suggestions to better understand your health.
    
    **Note:** 
    - This tool is not a substitute for professional medical advice.
    - Always consult a healthcare provider for serious or concerning symptoms.
    """)


st.link_button("Start Chatting", "https://chatbot-sym.streamlit.app/Bot", icon="💬", type="primary", help="At your own risk")
