import streamlit as st

st.title("ℹ️ About the Project")
st.divider()

st.markdown("""
This project aims to create a **Symptom Checker Bot** that offers personalized guidance. 
Using **Natural Language Processing (NLP)** and **Logistic Regression**, the bot extracts key details from user input to generate relevant responses.

Built with **Streamlit**, the user-friendly interface allows easy interaction for users to share concerns and receive feedback.
""")

st.subheader("🔍 Project Breakdown:")

st.subheader("📊 Dataset:")
st.markdown("""
The dataset includes labeled data for training:
- **Intents**: User input categories like:
  - Mental health queries
  - Symptom checking
  - General greetings
- **Entities**: Specific details from input such as:
  - Symptoms (e.g., anxiety, headache)
  - Emotional states (e.g., stress)
  - Contextual info (e.g., duration)
- **Text**: User input, like _"I feel anxious"_ or _"I have trouble sleeping."_
""")

st.subheader("💻 Streamlit Interface:")
st.markdown("""
The **Streamlit** interface allows smooth interaction:
- **Text input** for users to describe symptoms or concerns.
- **Response area** where the bot offers insights:
  - Symptom checking: Possible causes and advice.
  - Mental health: Supportive messages and resources.
- Integrated with an NLP model for real-time, intelligent responses.
""")

st.subheader("✅ Conclusion:")
st.markdown("""
This project merges **NLP** and a user-friendly design to create a **Symptom Checker Bot** that effectively responds to user input.

### Achievements:
- Applied NLP and Logistic Regression to process input.
- Developed an accessible **Streamlit** interface for non-technical users.
- Future enhancements may include:
  - Expanding the dataset.
  - Integrating **deep learning models** for better accuracy.
  - Supporting multiple languages.

This project demonstrates how NLP can contribute to mental health and well-being.
""")
