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

    if not policy:
        return none_found("Policy not found.")

    return found(policy, "Policy retrieved successfully.")


@router.get(
    "/summary/{member_id}",
    summary="Policy Summary",
    description="Returns a summarized view of the member's policy. " + STATUS_DOC,
)
def get_policy_summary(member_id: str = Path(...)):

    field = process_field("member_id", member_id)
    if field["status"] == "invalid_format":
        return invalid_format(field)

    # Policy is keyed by the MEM-prefixed member id (Policy.id == "MEM1001").
    policy, err = db_guard(DatabaseService.get_policy, to_db_member_id(field["value"]))
    if err:
        return err

    if not policy:
        return none_found("Policy not found.")

    return found(
        {
            "plan": policy.get("plan"),
            "copay": policy.get("copay"),
            "deductible": policy.get("deductible"),
            "outOfPocket": policy.get("outOfPocket"),
        },
        "Policy summary retrieved successfully.",
    )


@router.get(
    "/{member_id}",
    summary="Get Policy",
    description="Returns policy information using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_policy_by_member(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Policy is keyed by the MEM-prefixed member id (Policy.id == "MEM1001").
    policy, err = db_guard(DatabaseService.get_policy, db_member_id)
    if err:
        return err

    if not policy:
        return none_found("Policy not found.")

    return found(
        {
            "policyNumber": policy.get("policyNumber"),
            "plan": policy.get("plan"),
            "medical": policy.get("medical"),
            "dental": policy.get("dental"),
            "vision": policy.get("vision"),
            "copay": policy.get("copay"),
            "deductible": policy.get("deductible"),
            "outOfPocket": policy.get("outOfPocket"),
            "effectiveDate": policy.get("effectiveDate"),
            "expirationDate": policy.get("expirationDate"),
        },
        "Policy retrieved successfully.",
    )