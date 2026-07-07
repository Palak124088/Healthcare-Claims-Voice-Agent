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

    return found(claim, "Claim retrieved successfully.")


@router.get(
    "/status/{member_id}",
    summary="Get Claim Status (GET)",
    description="Latest claim status using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_claim_status_get(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Claims are linked by the MEM-prefixed member id (Claim.memberId == "MEM1001").
    claim, err = db_guard(DatabaseService.get_claim_by_member, db_member_id)
    if err:
        return err

    if not claim:
        return none_found("Claim not found.")

    return found(claim, "Claim retrieved successfully.")


@router.get(
    "/history/{member_id}",
    summary="Claim History",
    description="All claims submitted by a member using Member ID (spoken or typed). " + STATUS_DOC,
)
def claim_history(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Claims are linked by the MEM-prefixed member id (Claim.memberId == "MEM1001").
    claims, err = db_guard(DatabaseService.get_claim_history, db_member_id)
    if err:
        return err

    if not claims:
        return none_found("No claim history found.")

    return {
        "status": "found",
        "success": True,
        "message": "Claim history retrieved successfully.",
        "totalClaims": len(claims),
        "data": claims,
    }


@router.post(
    "/submit",
    summary="Submit New Claim",
    description=(
        "Creates a new healthcare claim. Member ID and service date are spoken "
        "fields normalized and validated before anything is written. " + STATUS_DOC
    ),
)
def submit_claim(request: ClaimSubmissionRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    date_field = process_field("service_date", request.serviceDate)
    if date_field["status"] == "invalid_format":
        return invalid_format(date_field)

    claim_type = normalize_claim_type(request.claimType)
    if not validate_claim_type(claim_type):
        return {
            "status": "invalid_format",
            "field": "claim_type",
            "hint": "the type of claim, such as medical, dental, vision, or pharmacy",
            "success": False,
        }

    if request.amount <= 0:
        return {
            "status": "invalid_format",
            "field": "amount",
            "hint": "the claim amount in dollars, greater than zero",
            "success": False,
        }

    claim = {
        # store the MEM-prefixed member id, matching every other Claim.memberId
        "memberId": db_member_id,
        "claimType": claim_type,
        "provider": normalize_provider(request.provider),
        "serviceDate": date_field["value"],
        "diagnosisCode": request.diagnosisCode,
        "amount": request.amount,
        "status": "Submitted",
        "submittedDate": datetime.utcnow().strftime("%Y-%m-%d"),
    }

    result, err = db_guard(DatabaseService.submit_claim, claim)
    if err:
        return err

    return {
        "status": "submitted",
        "success": True,
        "message": "Claim submitted successfully.",
        "data": result,
    }


@router.get(
    "/{claim_id}",
    summary="Get Claim Details",
    description="Full details for one claim using its Claim ID (spoken 'C L M ...' or typed). " + STATUS_DOC,
)
def get_claim_details(claim_id: str = Path(..., description="Claim ID, e.g. CLM1001")):

    # claim_id normalizes to the exact stored PK form (Claim.id == "CLM1001").
    response, clean_claim_id = resolve_field("claim_id", claim_id)
    if response:
        return response

    claim, err = db_guard(DatabaseService.get_claim, clean_claim_id)
    if err:
        return err

    if not claim:
        return none_found("Claim not found.")

    return found(claim, "Claim retrieved successfully.")


@router.put(
    "/{claim_id}",
    summary="Update Claim",
    description="Updates an existing claim by Claim ID (spoken 'C L M ...' or typed). " + STATUS_DOC,
)
def update_claim(claim_id: str, request: ClaimUpdateRequest):

    # claim_id normalizes to the exact stored PK form (Claim.id == "CLM1001").
    response, clean_claim_id = resolve_field("claim_id", claim_id)
    if response:
        return response

    # Only apply the fields the caller actually sent (partial update).
    payload = request.model_dump(exclude_unset=True, exclude_none=True)

    if not payload:
        return {
            "status": "invalid_format",
            "field": "update",
            "hint": "at least one field to change",
            "success": False,
        }

    if "serviceDate" in payload:
        date_field = process_field("service_date", payload["serviceDate"])
        if date_field["status"] == "invalid_format":
            return invalid_format(date_field)
        payload["serviceDate"] = date_field["value"]

    if "claimType" in payload:
        payload["claimType"] = normalize_claim_type(payload["claimType"])

    if "provider" in payload:
        payload["provider"] = normalize_provider(payload["provider"])

    updated, err = db_guard(DatabaseService.update_claim, clean_claim_id, payload)
    if err:
        return err

    if not updated:
        return none_found("Claim not found.")

    return found(updated, "Claim updated successfully.")


@router.delete(
    "/{claim_id}",
    summary="Cancel Claim",
    description="Deletes a submitted claim by Claim ID (spoken 'C L M ...' or typed). " + STATUS_DOC,
)
def delete_claim(claim_id: str):

    # claim_id normalizes to the exact stored PK form (Claim.id == "CLM1001").
    response, clean_claim_id = resolve_field("claim_id", claim_id)
    if response:
        return response

    deleted, err = db_guard(DatabaseService.delete_claim, clean_claim_id)
    if err:
        return err

    if not deleted:
        return none_found("Claim not found.")

    return {
        "status": "found",
        "success": True,
        "message": "Claim deleted successfully.",
    }