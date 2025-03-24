from fastapi import FastAPI, WebSocket, UploadFile, File, WebSocketDisconnect
from backend.ai_engine import modify_html
from backend.storage.storage import save_template, get_template
import json

app = FastAPI()

@app.post("/upload_template/")
async def upload_template(file: UploadFile = File(...)):
    """Endpoint to upload HTML templates."""
    result = save_template(file)
    return {"message": "Template uploaded", **result}

@app.websocket("/ws/modify_template")
async def websocket_modify_template(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            html_content, prompt_text = data.split("|", 1)
            
            async for suggestion in modify_html(html_content, prompt_text):
                await websocket.send_text(suggestion)
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error in WebSocket: {e}")
    finally:
        await websocket.close()