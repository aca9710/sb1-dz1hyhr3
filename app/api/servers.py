from fastapi import APIRouter, HTTPException
from typing import List
from ..models.server import Server, ServerCreate
from ..db.database import get_db_connection

router = APIRouter()

@router.get("/servers", response_model=List[Server])
async def get_servers():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM servidores ORDER BY nombre")
        servers = cur.fetchall()
        cur.close()
        conn.close()
        return servers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/servers", response_model=Server)
async def create_server(server: ServerCreate):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO servidores (nombre, dirip) VALUES (%s, %s) RETURNING *",
            (server.nombre, server.dirip)
        )
        new_server = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return new_server
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))