from fastapi import APIRouter, Path

from app.services.database_service import DatabaseService
from app.services.tool_helpers import resolve_member, db_guard, found, STATUS_DOC

router = APIRouter(
    prefix="/member",
    tags=["Member"]
)


@router.get(
    "/{member_id}",
    summary="Get Member Details",
    description="Returns member profile information using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_member_details(member_id: str = Path(...)):

    # resolve_member already loaded the member (Member.id == "MEM1001") and
    # returns tool_error/none_found/invalid_format as needed.
    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    member, err = db_guard(DatabaseService.get_member, db_member_id)
    if err:
        return err

    return found(
        {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "policyNumber": member.get("policyNumber"),
            "plan": member.get("plan"),
            "email": member.get("email"),
            "phone": member.get("phone"),
            "dob": member.get("dob"),
            "zipCode": member.get("zipCode"),
            "createdAt": member.get("createdAt"),
            "updatedAt": member.get("updatedAt"),
        },
        "Member details retrieved successfully.",
    )


@router.get(
    "/",
    summary="Get All Members",
    description="Returns all registered members.",
)
def get_all_members():

    members, err = db_guard(DatabaseService.get_all_members)
    if err:
        return err

    return {
        "status": "found" if members else "none_found",
        "success": True,
        "message": "Members retrieved successfully.",
        "count": len(members),
        "data": members,
    }