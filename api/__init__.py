from fastapi import APIRouter

# from api.user.v1.user import user_router as user_v1_router
# from api.auth.auth import auth_router
from api.item.item import item_router

router = APIRouter()
router.include_router(item_router, prefix="/item", tags=["Item"])

__all__ = ["router"]
