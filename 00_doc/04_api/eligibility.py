from fastapi import APIRouter, Path

from app.models.request_models import EligibilityRequest
from app.services.database_service import DatabaseService
from app.services.tool_helpers import (
    resolve_member,
    db_guard,
    none_found,
    found,
    STATUS_DOC,
)

router = APIRouter(
    prefix="/eligibility",
    tags=["Eligibility"]
)


@router.post(
    "/",
    summary="Check Eligibility",
    description="Checks member eligibility using Member ID (spoken or typed). " + STATUS_DOC,
)
def check_eligibility(request: EligibilityRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Eligibility is keyed by the MEM-prefixed member id (Eligibility.id == "MEM1001").
    eligibility, err = db_guard(DatabaseService.get_eligibility, db_member_id)
    if err:
        return err

    if not eligibility:
        return none_found("Eligibility information not found.")
    return found(eligibility, "Eligibility retrieved successfully.")
