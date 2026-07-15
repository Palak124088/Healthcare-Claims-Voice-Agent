from datetime import datetime

from fastapi import APIRouter, Path

from app.models.request_models import (
    ClaimStatusRequest,
    ClaimSubmissionRequest,
    ClaimUpdateRequest,
)

from app.services.database_service import DatabaseService
from app.services.field_processing import process_field
from app.services.tool_helpers import (
    resolve_member,
    resolve_field,
    db_guard,
    invalid_format,
    none_found,
    found,
    STATUS_DOC,
)

from app.utils.normalizers import (
    normalize_claim_type,
    normalize_provider,
)

from app.utils.validators import validate_claim_type

router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


@router.post(
    "/status",
    summary="Get Claim Status",
    description="Latest claim status for a member using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_claim_status(request: ClaimStatusRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Claims are linked by the MEM-prefixed member id (Claim.memberId == "MEM1001").
    claim, err = db_guard(DatabaseService.get_claim_by_member, db_member_id)
    if err:
        return err

    if not claim:
        return none_found("No claims found for this member.")

    }
