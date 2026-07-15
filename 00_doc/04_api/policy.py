from fastapi import APIRouter, Path

from app.models.request_models import PolicyRequest
from app.services.database_service import DatabaseService
from app.services.field_processing import process_field, to_db_member_id
from app.services.tool_helpers import (
    resolve_member,
    db_guard,
    invalid_format,
    none_found,
    found,
    STATUS_DOC,
)

router = APIRouter(
    prefix="/policy",
    tags=["Policy"]
)


@router.post(
    "/",
    summary="Get Policy Details",
    description="Returns policy details for a member using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_policy(request: PolicyRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Policy is keyed by the MEM-prefixed member id (Policy.id == "MEM1001").
    policy, err = db_guard(DatabaseService.get_policy, db_member_id)
    if err:
        return err

    )
