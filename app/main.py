from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import servers, applications, files

app = FastAPI(title="Server Management System")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(servers.router, tags=["Servers"])
app.include_router(applications.router, tags=["Applications"])
app.include_router(files.router, tags=["Files"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)