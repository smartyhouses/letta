from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from letta.orm.sqlalchemy_base import SqlalchemyBase

if TYPE_CHECKING:
    from letta.orm.job import Job


class JobUsageStatistics(SqlalchemyBase):
    """Tracks usage statistics for jobs, with future support for per-step tracking."""

    __tablename__ = "job_usage_statistics"

    id: Mapped[int] = mapped_column(primary_key=True, doc="Unique identifier for the usage statistics entry")
    job_id: Mapped[str] = mapped_column(
        ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, doc="ID of the job these statistics belong to"
    )
    step_id: Mapped[Optional[str]] = mapped_column(
        nullable=True, doc="ID of the specific step within the job (for future per-step tracking)"
    )
    completion_tokens: Mapped[int] = mapped_column(default=0, doc="Number of tokens generated by the agent")
    prompt_tokens: Mapped[int] = mapped_column(default=0, doc="Number of tokens in the prompt")
    total_tokens: Mapped[int] = mapped_column(default=0, doc="Total number of tokens processed by the agent")
    step_count: Mapped[int] = mapped_column(default=0, doc="Number of steps taken by the agent")

    # Relationship back to the job
    job: Mapped["Job"] = relationship("Job", back_populates="usage_statistics")
