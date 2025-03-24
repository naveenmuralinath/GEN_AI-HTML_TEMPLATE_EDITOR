from fastapi import FastAPI, WebSocket, UploadFile, File, WebSocketDisconnect
from pydantic import BaseModel
from backend.ai_engine import modify_html
from backend.storage.storage import save_template, get_template
import json
import asyncio

app = FastAPI()

class ModifyRequest(BaseModel):
    html_content: str
    prompt_text: str

@app.post("/modify_template/")
async def modify_template(request: ModifyRequest):
    """Modify an HTML template using AI based on user input."""
    
    response_generator = await modify_html(request.html_content, request.prompt_text)  

    modified_html = ""
    async for chunk in response_generator:  
        modified_html += chunk + "\n"
    
    return {"modified_html": modified_html}

@app.websocket("/ws/modify_template")
async def websocket_modify_template(websocket: WebSocket):
    """WebSocket to modify an HTML template in real-time."""
    await websocket.accept()
    
    try:
        data = await websocket.receive_json()
        html_content = data.get("html_content")
        prompt_text = data.get("prompt_text")

        response_generator = await modify_html(html_content, prompt_text)  

        async for suggestion in response_generator:
            await websocket.send_text(suggestion)

        await websocket.send_text("END")  
        await websocket.close()

    except WebSocketDisconnect:
        print("🔴 WebSocket Disconnected")
    except Exception as e:
        print(f"⚠️ Error in WebSocket: {str(e)}")
    finally:
        await websocket.close()