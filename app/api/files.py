from fastapi import APIRouter, HTTPException
from typing import List
from ..models.file import File, FileCreate
from ..db.database import get_db_connection

router = APIRouter()

@router.get("/files", response_model=List[File])
async def get_files():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT f.*, s.nombre as servidor_nombre, a.nombre as aplicacion_nombre
            FROM ficheros f
            LEFT JOIN servidores s ON f.idservidor = s.id
            LEFT JOIN aplicaciones a ON f.idaplicacion = a.id
            ORDER BY f.nombre
        """)
        files = cur.fetchall()
        cur.close()
        conn.close()
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/files", response_model=File)
async def create_file(file: FileCreate):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Verify server and application exist
        cur.execute("SELECT id FROM servidores WHERE id = %s", (file.idservidor,))
        if not cur.fetchone():
            raise HTTPException(status_code=404, detail="Server not found")
            
        cur.execute("SELECT id FROM aplicaciones WHERE id = %s", (file.idaplicacion,))
        if not cur.fetchone():
            raise HTTPException(status_code=404, detail="Application not found")

        cur.execute(
            """
            INSERT INTO ficheros (nombre, carpeta, idservidor, idaplicacion) 
            VALUES (%s, %s, %s, %s) 
            RETURNING *
            """,
            (file.nombre, file.carpeta, file.idservidor, file.idaplicacion)
        )
        new_file = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return new_file
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))