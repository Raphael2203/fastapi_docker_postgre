from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from projeto.configs.database import get_session

DatabaseDepency = Annotated[AsyncSession, Depends(get_session)]