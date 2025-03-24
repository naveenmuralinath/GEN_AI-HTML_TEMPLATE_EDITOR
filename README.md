# GEN_AI-HTML_TEMPLATE_EDITOR
# **GenAI HTML Template Editor**  
**Author: Naveen Murali**  

## **📌 Project Overview**  
This is a **GenAI-powered HTML Template Editor** that allows users to:  
✅ **Upload or Paste an HTML template**  
✅ **Modify the template dynamically using AI**  
✅ **Stream real-time AI-generated changes via WebSockets**  
✅ **Interact via a FastAPI backend & Streamlit frontend**  

The application is built using:  
- **LLM Model:** Mistral-7B via Hugging Face (`mistralai/Mistral-7B-Instruct`)  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM API Integration:** Hugging Face `InferenceClient`  
- **Real-time updates:** WebSockets  

---

## **🚀 Technologies Used**
### **1️⃣ FastAPI (Backend)**
- Handles API requests  
- Provides WebSocket streaming for live modifications  
- Uses Hugging Face's **Mistral-7B model** for AI-based HTML modifications  

### **2️⃣ Hugging Face LLM (Mistral-7B)**
- **Why Mistral-7B?**  
  - Open-source & efficient  
  - Supports **text generation**  
  - Hosted via Hugging Face Inference API  
- Used via `InferenceClient` to process **modification prompts**.  

### **3️⃣ Streamlit (Frontend)**
- User uploads/pastes HTML template  
- Sends **modification prompts**  
- Displays **AI-modified HTML** in real time  

---

## **📂 Project Structure**
```
GEN_AI_HTML_TEMPLATE_EDITOR/
│── backend/
│   ├── main.py          
│   ├── ai_engine.py     
│   ├── storage.py       
│   ├── __init__.py      
│
│── frontend/
│   ├── app.py           
│
│── requirements.txt     
│── readme.md            
│── .env                 
```

---

## **💻 How to Run the Project**
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Set Up Hugging Face API Key**
- Create a `.env` file in the **root directory** and add:
  ```env
  HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
  ```

### **3️⃣ Run the Backend (FastAPI)**
```bash
uvicorn backend.main:app --reload
```
✅ Backend starts at: `http://127.0.0.1:8000`  
✅ API Docs available at: `http://127.0.0.1:8000/docs`

---

## **🌐 Running the Frontend (Streamlit)**
```bash
streamlit run frontend/app.py
```
✅ Opens in browser at `http://localhost:8501`  
✅ Allows **HTML upload, modification, and live preview**

---

## **🛠️ API Endpoints**
| **Method** | **Endpoint** | **Description** |
|---|---|---|
| `POST` | `/modify_template/` | Modify an HTML string using AI |
| `POST` | `/upload_template/` | Upload an HTML file |
| `WebSocket` | `/ws/modify_template` | Real-time AI modifications |

---

## **🧪 API Testing with Postman**
### **Modify an HTML String**
#### **📌 Endpoint:**  
```http
POST http://127.0.0.1:8000/modify_template/
```
#### **📌 Request Body (JSON)**
```json
{
    "html_content": "<html><head><title>Old Title</title></head><body><h1>Sample Page</h1></body></html>",
    "prompt_text": "Change the title to Portfolio"
}
```
#### **📌 Expected Response**
```json
{
    "modified_html": "<html><head><title>Portfolio</title></head><body><h1>Sample Page</h1></body></html>"
}
```

---

## **📌 Troubleshooting**
### **1️⃣ `404 Not Found` (Postman)**
✅ Use **POST** (not GET)  
✅ Ensure URL **matches `/modify_template/`**  
✅ Use **raw JSON** (not `form-data`)  

### **2️⃣ `HuggingFaceEndpoint` Errors**
✅ Install latest `huggingface_hub`  
```bash
pip install -U huggingface_hub
```

### **3️⃣ `WebSocket Disconnected`**
✅ Restart backend  
```bash
uvicorn backend.main:app --reload
```
✅ Ensure **correct WebSocket URL** in frontend:  
```python
ws://127.0.0.1:8000/ws/modify_template
```

---

## **🚀 Summary**
This AI-powered **HTML Template Editor** enables real-time template modification using **FastAPI, Hugging Face LLM (Mistral-7B), and Streamlit.** It supports **both file upload & text-based HTML editing.**  
💡 **Now you can modify any HTML page with AI!**  

---
📌 **Built by:** **Naveen Murali** 🚀  
💬 **Feel free to improve, extend, and contribute!**