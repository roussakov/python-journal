from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from python_journal.db import get_session
from python_journal.services.entry_service import EntryService


def get_entry_service(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> EntryService:
    return EntryService(session)