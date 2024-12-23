from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.db.database import get_db_connection

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/servers", response_class=HTMLResponse)
async def list_servers(request: Request):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM servidores ORDER BY nombre")
    servers = cur.fetchall()
    cur.close()
    conn.close()
    return templates.TemplateResponse("servers.html", {
        "request": request,
        "servers": servers
    })

@app.post("/servers")
async def create_server(nombre: str = Form(...), dirip: str = Form(...)):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO servidores (nombre, dirip) VALUES (%s, %s)",
        (nombre, dirip)
    )
    conn.commit()
    cur.close()
    conn.close()
    return RedirectResponse(url="/servers", status_code=303)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)