# app/api/endpoints/subscriptions.py
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

# from app import crud
# from app.api import deps
# from app.models.user import User
# from app.schemas.subscription import Subscription, SubscriptionCreate, SubscriptionUpdate

router = APIRouter()


# @router.get("/", response_model=List[Subscription])
# async def read_subscriptions(
#         db: AsyncSession = Depends(deps.get_db),
#         skip: int = 0,
#         limit: int = 100,
#         current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     获取订阅列表。
#     普通用户只能看到自己的订阅，超级用户可以看到所有订阅。
#     """
#     if crud.user.is_superuser(current_user):
#         subscriptions = await crud.subscription.get_multi(db, skip=skip, limit=limit)
#     else:
#         subscriptions = await crud.subscription.get_multi_by_owner(
#             db=db, owner_id=current_user.id, skip=skip, limit=limit
#         )
#     return subscriptions
#
#
# @router.post("/", response_model=Subscription, status_code=status.HTTP_201_CREATED)
# async def create_subscription(
#         *,
#         db: AsyncSession = Depends(deps.get_db),
#         subscription_in: SubscriptionCreate,
#         current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     创建新订阅。
#     """
#     subscription = await crud.subscription.create_with_owner(
#         db=db, obj_in=subscription_in, owner_id=current_user.id
#     )
#     return subscription
#
#
# @router.get("/{id}", response_model=Subscription)
# async def read_subscription(
#         *,
#         db: AsyncSession = Depends(deps.get_db),
#         id: int,
#         current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     通过ID获取订阅信息。
#     """
#     subscription = await crud.subscription.get(db=db, id=id)
#     if not subscription:
#         raise HTTPException(status_code=404, detail="订阅不存在")
#     if not crud.user.is_superuser(current_user) and (subscription.owner_id != current_user.id):
#         raise HTTPException(status_code=403, detail="权限不足")
#     return subscription
#
#
# @router.put("/{id}", response_model=Subscription)
# async def update_subscription(
#         *,
#         db: AsyncSession = Depends(deps.get_db),
#         id: int,
#         subscription_in: SubscriptionUpdate,
#         current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     更新订阅信息。
#     """
#     subscription = await crud.subscription.get(db=db, id=id)
#     if not subscription:
#         raise HTTPException(status_code=404, detail="订阅不存在")
#     if not crud.user.is_superuser(current_user) and (subscription.owner_id != current_user.id):
#         raise HTTPException(status_code=403, detail="权限不足")
#     subscription = await crud.subscription.update(db=db, db_obj=subscription, obj_in=subscription_in)
#     return subscription
#
#
# @router.delete("/{id}", response_model=Subscription)
# async def delete_subscription(
#         *,
#         db: AsyncSession = Depends(deps.get_db),
#         id: int,
#         current_user: User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     删除订阅。
#     """
#     subscription = await crud.subscription.get(db=db, id=id)
#     if not subscription:
#         raise HTTPException(status_code=404, detail="订阅不存在")
#     if not crud.user.is_superuser(current_user) and (subscription.owner_id != current_user.id):
#         raise HTTPException(status_code=403, detail="权限不足")
#     subscription = await crud.subscription.remove(db=db, id=id)
#     return subscription
