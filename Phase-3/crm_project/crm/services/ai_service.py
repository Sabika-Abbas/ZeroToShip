import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def generate_followup_draft(contact_name, notes_history):
    if notes_history:
        context = "\n".join([f"- {note}" for note in notes_history])
    else:
        context = "No previous interactions recorded."

    prompt = ChatPromptTemplate.from_template("""
You are a professional networking assistant helping a student follow up with a contact.

**Contact Name:** {name}
**Past Interactions:** 
{context}

**Task:** Write a warm, professional, and personalized follow-up message (2-3 short paragraphs) that:
- References the past interactions naturally
- Shows genuine interest in the contact
- Is specific, not generic
- Ends with a clear but low-pressure call to action.

**Draft:**
""")

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm | StrOutputParser()
    draft = chain.invoke({"name": contact_name, "context": context})
    return draft.strip()