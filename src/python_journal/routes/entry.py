from typing import Annotated
from fastapi import APIRouter, Body, Depends

from python_journal.dependecies.entry_service import get_entry_service
from python_journal.schemas.entry import CreateEntryRequest, EntriesResponse, EntryResponse
from python_journal.services.entry_service import EntryService

router = APIRouter(prefix="/entries")

@router.get("/", response_model=EntriesResponse)
async def read_entries(entries_service: Annotated[EntryService, Depends(get_entry_service)]):
    list = await entries_service.get_entries();
    return EntriesResponse(list=list);

@router.post("/", response_model=EntryResponse)
async def create_entry(entry: CreateEntryRequest, entries_service: Annotated[EntryService, Depends(get_entry_service)]):
    return await entries_service.create_entry(content=entry.content, tags=entry.tags);