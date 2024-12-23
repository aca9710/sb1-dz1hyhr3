from .base import BaseModel, UUID, Optional

class ApplicationBase(BaseModel):
    nombre: str
    carpeta: str
    idservidor: UUID

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: UUID
    
    class Config:
        from_attributes = True