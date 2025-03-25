import streamlit as st
import requests
import base64
from langchain_google_genai import GoogleGenerativeAI

# Retrieve API keys securely from Streamlit secrets
STABILITY_API_KEY = st.secrets["STABILITY_API_KEY"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Load user credentials from Streamlit secrets
USERS = {
    st.secrets["authentication"]["user1"]: st.secrets["authentication"]["password1"],
    st.secrets["authentication"]["user2"]: st.secrets["authentication"]["password2"]
}

# User authentication
def authenticate():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.sidebar.success(f"Welcome, {username}!")
            st.balloons()
        else:
            st.sidebar.error("Invalid credentials. Try again.")

authenticated = st.session_state.get("authenticated", False)
if not authenticated:
    authenticate()
    st.stop()

# Initialize LangChain's Gemini model
llm = GoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=GEMINI_API_KEY)

# Function to call LangChain Gemini model
def get_gemini_response(prompt):
    try:
        response = llm.invoke(prompt)
        return response if response else "No response received from Gemini API."
    except Exception as e:
        return f"Error: {str(e)}"

# Stability AI Image Generation (Updated for SD3)
def generate_image(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "accept": "image/*"
    }
    files = {"none": ""}
    data = {
        "prompt": prompt,
        "output_format": "jpeg"
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        return response.content  # Return image data directly
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("🔮 Future AI GPT")

prompt = st.text_input("💡 Enter your creative prompt:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎨 Generate Image"):
        if prompt:
            image_data = generate_image(prompt)
            if isinstance(image_data, bytes):  # If image data is received
                st.image(image_data, caption="Generated Image", use_container_width=True)
                
                # Provide download button
                st.download_button(
                    label="⬇️ Download Image",
                    data=image_data,
                    file_name="generated_image.jpeg",
                    mime="image/jpeg"
                )
            else:
                st.error(image_data)  # Show error message if generation fails
        else:
            st.warning("⚠️ Please enter a prompt.")

with col2:
    if st.button("📄 Generate Text"):
        if prompt:
            response_text = get_gemini_response(prompt)
            if "Error:" not in response_text:
                st.markdown("### ✍️ AI Response")
                st.write(response_text)
                
                # Provide copy button
                st.code(response_text, language="text")
                st.download_button(
                    label="📋 Copy Text",
                    data=response_text,
                    file_name="ai_response.txt",
                    mime="text/plain"
                )
            else:
                st.error(response_text)
        else:
            st.warning("⚠️ Please enter a prompt.")