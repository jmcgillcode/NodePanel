# app/api/endpoints/auth.py

from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

# from app import crud
# from app.api import deps
# from app.core import security
# from app.core.config import settings
# from app.schemas.token import Token

router = APIRouter()

#
# @router.post("/login", response_model=Token)
# async def login_access_token(
#         db: AsyncSession = Depends(deps.get_db),
#         form_data: OAuth2PasswordRequestForm = Depends()
# ) -> Any:
#     """
#     OAuth2兼容的令牌登录，获取访问令牌
#     """
#     # 验证用户
#     user = await crud.user.authenticate(
#         db, email=form_data.username, password=form_data.password
#     )
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="用户名或密码不正确",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     elif not crud.user.is_active(user):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="用户未激活"
#         )
#
#     # 创建访问令牌
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return {
#         "access_token": security.create_access_token(
#             user.id, expires_delta=access_token_expires
#         ),
#         "token_type": "bearer",
#     }
