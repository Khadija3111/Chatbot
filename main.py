import os
import chainlit as chn
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
#first part ends   This section imports all the necessary libraries 
# and sets up the connection to the Gemini API, preparing the environment for building the chatbot.



@chn.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: chn.User,
) -> Optional[chn.User]:
    """
    Handle the oAuth callback from Github.
    Return the user object if authentication is successful, None otherwise.
    """
    print(f"Provider: {provider_id}")
    print(f"User-data: {raw_user_data}")

    return default_user

#2nd part
#  This section handles user authentication using OAuth. It's optional and likely
#  used if you want users to log in to your chatbot application with their existing accounts (e.g., GitHub).

@chn.on_chat_start
async def handle_chat_start():
    chn.user_session.set("history", [])
    await chn.Message(content="Hello! How can I help you today?").send()
#3rd part
#This section sets up the chatbot when a user starts a new conversation.
#It initializes a blank chat history and sends a friendly welcome message.

@chn.on_message
async def handle_message(message: chn.Message):
    history = chn.user_session.get("history")
    history.append({"role": "user", "content": message.content})



    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append(
            {"role": role, "parts": [{"text": msg["content"]}]}
        )

    response = model.generate_content(formatted_history)
    response_text = response.text if hasattr(response, "text") else ""

    history.append({"role": "assistant", "content": response_text})
    chn.user_session.set("history", history)
    await chn.Message(content=response_text).send()

# This is the main part of the chatbot logic. It receives the user's message, adds 
# it to the chat history, formats the history for the Gemini model, sends the history to Gemini
#  to generate a response, adds the response to the history,
#  and sends the response back to the user.  This creates the conversational loop.