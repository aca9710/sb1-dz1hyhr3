from .base import BaseModel, UUID, Optional

class FileBase(BaseModel):
    nombre: str
    carpeta: str
    idservidor: UUID
    idaplicacion: UUID

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: UUID
    
    class Config:
        from_attributes = True