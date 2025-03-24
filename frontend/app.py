import streamlit as st
import asyncio
import websockets

def get_websocket_connection():
    return "ws://localhost:8000/ws/modify_template"

async def websocket_request(html_content, prompt_text):
    uri = get_websocket_connection()
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(f"{html_content}|{prompt_text}")
            response = []
            while True:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=10)
                    response.append(message)
                except asyncio.TimeoutError:
                    break
                except websockets.exceptions.ConnectionClosed:
                    break
            return "\n".join(response)
    except Exception as e:
        return f"Error: {str(e)}"

def process_template_modification(html_input, prompt_input):
    return asyncio.run(websocket_request(html_input, prompt_input))

def main():
    st.title("GenAI HTML Template Editor")
    
    # Ensure session state is properly initialized
    if "html_content" not in st.session_state:
        st.session_state.html_content = "<h1>Hello, World!</h1>"

    html_input = st.text_area("Edit HTML Template", value=st.session_state.html_content, height=200)
    prompt_input = st.text_input("Modification Prompt", "Make it modern")
    
    if st.button("Modify Template"):
        with st.spinner("Processing..."):
            response = process_template_modification(html_input, prompt_input)
            if response and not response.startswith("Error") and response.strip():
                st.session_state.html_content = response
            else:
                st.error("Failed to modify template. Please try again.")

    st.subheader("Modified HTML Preview")
    st.code(st.session_state.get("html_content", ""), language="html")

if __name__ == "__main__":
    main()
