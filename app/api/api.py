# app/api/api.py
from fastapi import APIRouter

# 导入各个端点路由
from app.api.endpoints import auth, users, subscriptions

# 创建主API路由器
api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(users.router, prefix="/users", tags=["用户"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["订阅"])