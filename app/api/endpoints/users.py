# app/api/endpoints/users.py

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
#
# from app import crud
# from app.api import deps
# from app.models.user import User
# from app.schemas.user import User as UserSchema, UserCreate, UserUpdate

router = APIRouter()

# @router.get("/", response_model=List[UserSchema])
# async def read_users(
#     db: AsyncSession = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: User = Depends(deps.get_current_active_superuser),
# ) -> Any:
#     """
#     获取所有用户列表，仅限超级用户。
#     """
#     users = await crud.user.get_multi(db, skip=skip, limit=limit)
#     return users
#
# @router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
# async def create_user(
#     *,
#     db: AsyncSession = Depends(deps.get_db),
#     user_in: UserCreate,
#     current_user: User = Depends(deps.get_current_active_superuser),
# ) -> Any:
#     """
#     创建新用户，仅限超级用户。
#     """
#     user = await crud.user.get_by_email(db, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="该邮箱已被注册",
#         )
#     user = await crud.user.create(db, obj_in=user_in)
#     return user
#
# @router.get("/me", response_model=UserSchema)
# async def read_user_me(
#     current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     获取当前登录用户信息。
#     """
#     return current_user
#
# @router.put("/me", response_model=UserSchema)
# async def update_user_me(
#     *,
#     db: AsyncSession = Depends(deps.get_db),
#     user_in: UserUpdate,
#     current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     更新当前登录用户信息。
#     """
#     user = await crud.user.update(db, db_obj=current_user, obj_in=user_in)
#     return user
#
# @router.get("/{user_id}", response_model=UserSchema)
# async def read_user_by_id(
#     user_id: int,
#     current_user: User = Depends(deps.get_current_active_user),
#     db: AsyncSession = Depends(deps.get_db),
# ) -> Any:
#     """
#     通过ID获取用户信息。
#     """
#     user = await crud.user.get(db, id=user_id)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="用户不存在",
#         )
#     if user.id != current_user.id and not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=403,
#             detail="权限不足",
#         )
#     return user