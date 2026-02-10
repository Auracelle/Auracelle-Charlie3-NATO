"""
Auracelle Charlie – Web Service Entrypoint

This file is the canonical entrypoint used by most PaaS providers
(Render, Railway, Fly.io, Azure App Service).
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
