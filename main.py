from fastapi import FastAPI
from api.health import router as health_router
from api.metrics import router as metrics_router
from api.policy import router as policy_router

app = FastAPI(
    title="Auracelle Charlie Research Engine",
    description="Policy Stress-Testing & Computational Governance API",
    version="1.0.0"
)

app.include_router(health_router, prefix="/v1")
app.include_router(metrics_router, prefix="/v1")
app.include_router(policy_router, prefix="/v1")
