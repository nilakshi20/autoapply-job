from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    linkedin_job_id: Mapped[str] = mapped_column(String(100), unique=True)

    title: Mapped[str] = mapped_column(String(255))

    company: Mapped[str] = mapped_column(String(255))

    location: Mapped[str] = mapped_column(String(255))

    job_url: Mapped[str] = mapped_column(String(500))

    easy_apply: Mapped[bool] = mapped_column(Boolean)

    status: Mapped[str] = mapped_column(String(50), default="pending")

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )