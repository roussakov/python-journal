import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from python_journal.models.entry import Entry

class EntryService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_entries(self) -> list[Entry]:
        result = await self.session.scalars(select(Entry))
        return result.all()

    async def create_entry(self, content: str):
        entry = Entry(id=str(uuid.uuid4()), content=content)
        self.session.add(entry)
        await self.session.commit()

        return entry