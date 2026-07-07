from fastapi import APIRouter, Path

from app.models.request_models import BenefitsRequest
from app.services.database_service import DatabaseService
from app.services.tool_helpers import (
    resolve_member,
    db_guard,
    none_found,
    found,
    STATUS_DOC,
)

router = APIRouter(
    prefix="/benefits",
    tags=["Benefits"]
)


@router.post(
    "/",
    summary="Get Member Benefits",
    description="Returns benefits for a member using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_benefits(request: BenefitsRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Benefits are keyed by the MEM-prefixed member id (Benefit.id == "MEM1001").
    benefits, err = db_guard(DatabaseService.get_benefits, db_member_id)
    if err:
        return err

    if not benefits:
        return none_found("Benefits information not found.")

    return found(benefits, "Benefits retrieved successfully.")


@router.get(
    "/{member_id}",
    summary="Get Benefits",
    description="Returns benefits using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_benefits_by_member(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Benefits are keyed by the MEM-prefixed member id (Benefit.id == "MEM1001").
    benefits, err = db_guard(DatabaseService.get_benefits, db_member_id)
    if err:
        return err

    if not benefits:
        return none_found("Benefits not found.")

    return found(benefits, "Benefits retrieved successfully.")