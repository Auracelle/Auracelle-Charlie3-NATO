from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "running",
        "engine": "Auracelle Charlie",
        "mode": "policy stress-testing"
    }
