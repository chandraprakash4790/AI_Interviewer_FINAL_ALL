
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
from app.session import InterviewSession

app = FastAPI()

@app.websocket("/ws/interview")
async def interview(ws: WebSocket):
    await ws.accept()
    session = InterviewSession()
    await ws.send_json({"type":"question","data":session.ask()})
    try:
        while True:
            msg = await ws.receive_json()
            if msg["type"] == "context":
                session.add_context(msg["data"])
            elif msg["type"] == "answer":
                q = session.follow_up(msg["data"])
                await ws.send_json({"type":"question","data":q})
            elif msg["type"] == "end":
                await ws.send_json({"type":"report","data":session.report()})
                break
    except WebSocketDisconnect:
        pass
