from .base import BaseModel, UUID, Optional

class ServerBase(BaseModel):
    nombre: str
    dirip: str

class ServerCreate(ServerBase):
    pass

class Server(ServerBase):
    id: UUID
    
    class Config:
        from_attributes = True