from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/respond")
def respond(msg: Message):
    return {
        "reply": f"你說了：{msg.message}，我是角色A的回應。",
        "mood": "neutral",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/reset")
def reset():
    return {}

@app.get("/health")
def health():
    return {"status": "ok"}
