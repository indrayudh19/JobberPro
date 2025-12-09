"""
Pydantic models for the India Job Map API.
"""

from pydantic import BaseModel, HttpUrl
from typing import Optional


class JobPin(BaseModel):
    """Model representing a job pin on the map."""
    
    id: str
    company_name: str
    job_title: str
    latitude: float
    longitude: float
    job_url: str
    location_name: str
    description: Optional[str] = None


class JobPinResponse(BaseModel):
    """Response model for the /pins endpoint."""
    
    pins: list[JobPin]
    total: int
