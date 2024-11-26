from pydantic import BaseModel
from typing import List
from uuid import UUID

class ListUsersInputDto(BaseModel):
    pass 

class UserDto(BaseModel):
    id: UUID
    name: str

class ListUsersOutputDto(BaseModel):
    users: List[UserDto]