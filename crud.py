from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas

#read
async def get_items(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Item).offset(skip).limit(limit))
    return result.scalars().all()

#create
async def create_item(db: AsyncSession, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
#update
async def update_item(db: AsyncSession, item_id: int, item: schemas.ItemUpdate):
    db_item = await db.get(models.Item, item_id)
    if db_item:
        for key, value in item.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
    return db_item
#delete
async def delete_item(db: AsyncSession, item_id: int):
    db_item = await db.get(models.Item, item_id)
    if db_item:
        await db.delete(db_item)
        await db.commit()
    return db_item