from fastapi import APIRouter, HTTPException
from typing import List
from ..models.application import Application, ApplicationCreate
from ..db.database import get_db_connection

router = APIRouter()

@router.get("/applications", response_model=List[Application])
async def get_applications():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT a.*, s.nombre as servidor_nombre 
            FROM aplicaciones a 
            LEFT JOIN servidores s ON a.idservidor = s.id 
            ORDER BY a.nombre
        """)
        applications = cur.fetchall()
        cur.close()
        conn.close()
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/applications", response_model=Application)
async def create_application(application: ApplicationCreate):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO aplicaciones (nombre, carpeta, idservidor) 
            VALUES (%s, %s, %s) 
            RETURNING *
            """,
            (application.nombre, application.carpeta, application.idservidor)
        )
        new_application = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return new_application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))