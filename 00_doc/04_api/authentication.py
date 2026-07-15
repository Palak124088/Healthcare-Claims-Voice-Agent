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
        }
