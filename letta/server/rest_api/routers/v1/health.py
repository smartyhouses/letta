from typing import TYPE_CHECKING

from fastapi import APIRouter

from letta import __version__
from letta.schemas.health import Health

if TYPE_CHECKING:
    pass

router = APIRouter(prefix="/health", tags=["health"])


# Health check
@router.get("/", response_model=Health, operation_id="health_check")
def health_check():
    return Health(
        version=__version__,
        status="ok",
    )
