import importlib.metadata
from typing import Literal, Optional

from packaging.version import parse
from pydantic import BaseModel


def dump_object(object):
    if parse(importlib.metadata.version("pydantic")) < parse("2.0.0"):
        return object.dict()
    else:
        return object.model_dump(exclude_none=True)


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "function", "system", "situation", "thought", "information", "functions", "function_call"]
    content: str
    name: Optional[str] = None


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: Optional[int] = None
    total_tokens: int
