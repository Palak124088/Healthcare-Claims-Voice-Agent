from fastapi import APIRouter

from app.models.request_models import (
    AuthenticationRequest,
    VoiceAuthenticationRequest,
)
from app.services.database_service import DatabaseService
from app.services.authentication_service import handle_authentication

from app.utils.normalizers import (
    normalize_member_id,
    normalize_date,
    normalize_zip,
    normalize_ssn
)

from app.utils.validators import (
    validate_member_id,
    validate_date,
    validate_zip,
    validate_ssn
)

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"]
)


@router.post(
    "/voice",
    summary="Authenticate Member (Voice)",
    description=(
        "Single entry point for the voice agent. Accepts raw spoken or typed "
        "inputs and a session id. The backend normalizes, validates (including "
        "a real calendar check on the date of birth), counts failed attempts in "
        "session state, and decides escalation. The agent only collects input "
        "one field at a time and reacts to the returned status: "
        "invalid_format | no_match | matched | escalate | tool_error."
    ),
)
def authenticate_voice(request: VoiceAuthenticationRequest):

    return handle_authentication(
        session_id=request.sessionId,
        raw_inputs={
            "member_id": request.memberId,
            "dob": request.dob,
            "zip_code": request.zipCode,
            "last4SSN": request.last4SSN,
        },
    )


@router.post(
    "/",
    summary="Authenticate Member",
    description="Authenticates a healthcare member using Member ID, DOB, ZIP Code and Last 4 SSN."
)
def authenticate(request: AuthenticationRequest):

    member_id = normalize_member_id(request.memberId)
    dob = normalize_date(request.dob)
    zip_code = normalize_zip(request.zipCode)
    ssn = normalize_ssn(request.last4SSN)

    if not validate_member_id(member_id):
        return {
            "success": False,
            "code": "INVALID_MEMBER_ID",
            "message": "Invalid Member ID."
        }

    if not validate_date(dob):
        return {
            "success": False,
            "code": "INVALID_DOB",
            "message": "Invalid Date of Birth."
        }

    if not validate_zip(zip_code):
        return {
            "success": False,
            "code": "INVALID_ZIP",
            "message": "Invalid ZIP Code."
        }

    if not validate_ssn(ssn):
        return {
            "success": False,
            "code": "INVALID_SSN",
            "message": "Invalid Last 4 SSN."
        }

    member = DatabaseService.get_member(member_id)

    if not member:
        return {
            "success": False,
            "code": "MEMBER_NOT_FOUND",
            "message": "Member not found."
        }

    if (
        member.get("dob") != dob or
        member.get("zipCode") != zip_code or
        member.get("last4SSN") != ssn
    ):
        return {
            "success": False,
            "code": "AUTHENTICATION_FAILED",
            "message": "Authentication failed. Please verify your details."
        }

    return {
        "success": True,
        "code": "AUTHENTICATED",
        "message": "Authentication successful.",
        "data": {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "plan": member.get("plan"),
            "policyNumber": member.get("policyNumber"),
            "email": member.get("email"),
            "phone": member.get("phone")
        }
    }


@router.get(
    "/member/{member_id}",
    summary="Verify Member",
    description="Verifies whether a member exists."
)
def verify_member(member_id: str):

    member_id = normalize_member_id(member_id)

    if not validate_member_id(member_id):
        return {
            "success": False,
            "code": "INVALID_MEMBER_ID",
            "message": "Invalid Member ID."
        }

    member = DatabaseService.get_member(member_id)

    if not member:
        return {
            "success": False,
            "code": "MEMBER_NOT_FOUND",
            "message": "Member not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Member verified successfully.",
        "data": {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "plan": member.get("plan"),
            "policyNumber": member.get("policyNumber")
        }
    }