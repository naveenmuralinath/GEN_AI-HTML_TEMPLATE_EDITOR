import streamlit as st
import asyncio
import websockets
import json

st.title("GenAI-Powered HTML Editor")

html_input = st.text_area("Paste your HTML Template", 
                          value="<html><head><title>Old Title</title></head><body><h1>Sample Page</h1></body></html>", 
                          height=200)

prompt_text = st.text_area("Describe changes:", "Change the title to Fire Fire")

async def stream_modifications():
    """WebSocket function to modify HTML template in real-time"""
    uri = "ws://127.0.0.1:8000/ws/modify_template"
    
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"html_content": html_input, "prompt_text": prompt_text})) 
        
        modified_html = ""
        
        while True:
            try:
                suggestion = await websocket.recv()
                if suggestion == "END":  
                    break
                modified_html += suggestion + "\n"
            except websockets.exceptions.ConnectionClosed:
                break

        return modified_html.strip()  # Trim unnecessary spaces

if st.button("Modify Template"):
    with st.spinner("Processing..."):
        response = asyncio.run(stream_modifications())

        if response:
            st.success("Modification completed!")

            # Shows HTML Code Output
            st.subheader("Modified HTML Code")
            st.code(response, language="html")

            # Shows HTML UI Preview
            st.subheader("Live HTML Preview")
            st.components.v1.html(response, height=400, scrolling=True)  # Render HTML as UI
        else:
            st.error("No response received.")