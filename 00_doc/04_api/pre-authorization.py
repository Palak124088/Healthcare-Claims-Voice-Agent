from fastapi import APIRouter, Path

from app.models.request_models import PreAuthorizationRequest
from app.services.database_service import DatabaseService
from app.services.tool_helpers import (
    resolve_member,
    db_guard,
    none_found,
    found,
    STATUS_DOC,
)

router = APIRouter(
    prefix="/preauthorization",
    tags=["Pre Authorization"]
)


@router.post(
    "/",
    summary="Get Pre-Authorization",
    description="Returns pre-authorization details using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_preauthorization(request: PreAuthorizationRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Pre-auth rows are matched on the MEM-prefixed member id
    # (PreAuthorization.memberId == "MEM1001").
    preauth, err = db_guard(DatabaseService.get_preauthorization, db_member_id)
    if err:
        return err

    if not preauth:
        return none_found("Pre-authorization not found.")

    return found(preauth, "Pre-authorization retrieved successfully.")


@router.get(
    "/{member_id}",
    summary="Get Pre-Authorization",
    description="Returns pre-authorization details using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_preauthorization_by_member(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Pre-auth rows are matched on the MEM-prefixed member id
    # (PreAuthorization.memberId == "MEM1001").
    preauth, err = db_guard(DatabaseService.get_preauthorization, db_member_id)
    if err:
        return err

    if not preauth:
        return none_found("Pre-authorization not found.")

    return found(preauth, "Pre-authorization retrieved successfully.")