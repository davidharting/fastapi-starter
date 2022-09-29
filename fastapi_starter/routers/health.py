import typing
from dataclasses import dataclass

from fastapi import APIRouter

router = APIRouter()


@dataclass
class HealthResponse:
    status: typing.Literal["ok"] = "ok"


@router.get("/healthz")
async def root() -> HealthResponse:
    return HealthResponse()
