import streamlit as st

st.set_page_config(page_title="AI Interview Question Generator")

st.title("🤖 AI Interview Question Generator")

skill = st.text_input("Enter Skill (Python, Java, SQL, HTML, CSS)")

level = st.selectbox(
    "Select Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

questions = {
    "python": {
        "Easy": [
            "What is Python?",
            "What are Python data types?",
            "What is a list in Python?"
        ],
        "Medium": [
            "What is OOP in Python?",
            "Explain decorators.",
            "What is exception handling?"
        ],
        "Hard": [
            "Explain multithreading.",
            "What are generators?",
            "Explain GIL in Python."
        ]
    },
    "java": {
        "Easy": [
            "What is Java?",
            "What is JVM?",
            "What is a class?"
        ],
        "Medium": [
            "Explain inheritance.",
            "What is polymorphism?",
            "What is encapsulation?"
        ],
        "Hard": [
            "Explain multithreading.",
            "What is garbage collection?",
            "Difference between HashMap and Hashtable?"
        ]
    },
    "sql": {
        "Easy": [
            "What is SQL?",
            "What is a table?",
            "What is a primary key?"
        ],
        "Medium": [
            "Difference between WHERE and HAVING?",
            "What is JOIN?",
            "What is normalization?"
        ],
        "Hard": [
            "Explain indexing.",
            "What are stored procedures?",
            "What is query optimization?"
        ]
    }
}

if st.button("Generate Questions"):
    skill_lower = skill.lower()

    if skill_lower in questions:
        st.subheader("Interview Questions")

        for q in questions[skill_lower][level]:
            st.write("•", q)
    else:
        st.error("Skill not available. Try Python, Java, or SQL.")