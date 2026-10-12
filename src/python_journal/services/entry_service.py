import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import select
from python_journal.models.entry import Entry
from python_journal.models.tag import Tag

class EntryService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _normalize_tag_names(self, names: list[str]) -> list[str]:
        return [name.casefold() for name in names]

    async def get_entries(self) -> list[Entry]:
        result = await self.session.scalars(select(Entry).options(selectinload(Entry.tags)))
        return result.all()

    async def _resolve_tag_names(self, tag_names: list[str]) -> list[Tag]:
        normalized_tag_names = self._normalize_tag_names(tag_names)
        
        existing_tags = (
            await self.session.scalars(select(Tag).where(Tag.name.in_(normalized_tag_names)))
            ).all()

        existing_names = {existing_tag.name for existing_tag in existing_tags}


        missing = [
            Tag(id=uuid.uuid4(), name=name) 
            for name in normalized_tag_names 
            if name not in existing_names
        ]

        if missing:
            self.session.add_all(missing)

        return [*missing, *existing_tags]

    async def create_entry(self, content: str, tags: list[str]):
        resolved_tag_names = await self._resolve_tag_names(tags) if tags else []

        entry = Entry(id=str(uuid.uuid4()), content=content, tags=resolved_tag_names)
        self.session.add(entry)
        await self.session.commit()

        return entry