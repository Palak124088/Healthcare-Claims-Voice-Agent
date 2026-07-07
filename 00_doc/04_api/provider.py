from fastapi import APIRouter, Path, Query

from app.models.request_models import ProviderLookupRequest
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
    normalize_provider,
    normalize_state,
    normalize_npi,
)

router = APIRouter(
    prefix="/providers",
    tags=["Provider Lookup"]
)


@router.post(
    "/",
    summary="Provider Lookup",
    description="Returns provider details for a member using Member ID (spoken or typed). " + STATUS_DOC,
)
def provider_lookup(request: ProviderLookupRequest):

    response, db_member_id = resolve_member(request.memberId)
    if response:
        return response

    # Providers are linked by the MEM-prefixed member id (Provider.memberId == "MEM1001").
    provider, err = db_guard(DatabaseService.get_provider, db_member_id)
    if err:
        return err

    if not provider:
        return none_found("Provider not found.")

    return found(provider, "Provider retrieved successfully.")


# NOTE: literal routes are declared BEFORE "/{member_id}" so paths like
# /providers/search or /providers/id/PR1001 are not swallowed by the
# member-id path parameter.
@router.get(
    "/id/{provider_id}",
    summary="Get Provider by Provider ID",
    description="Returns a provider by its Provider ID (spoken 'P R ...' or typed). " + STATUS_DOC,
)
def get_provider_by_provider_id(provider_id: str = Path(..., description="Provider ID, e.g. PR1001")):

    # provider_id normalizes to the exact stored PK form (Provider.id == "PR1001").
    response, clean_provider_id = resolve_field("provider_id", provider_id)
    if response:
        return response

    provider, err = db_guard(DatabaseService.get_provider_by_id, clean_provider_id)
    if err:
        return err

    if not provider:
        return none_found("Provider not found.")

    return found(provider, "Provider retrieved successfully.")


@router.get(
    "/search",
    summary="Search Providers",
    description="Search providers by provider name, city, state or ZIP code. " + STATUS_DOC,
)
def search_provider(
    providerName: str | None = Query(None),
    city: str | None = Query(None),
    state: str | None = Query(None),
    zipCode: str | None = Query(None),
):

    zip_clean = None
    if zipCode:
        zip_field = process_field("zip_code", zipCode)
        if zip_field["status"] == "invalid_format":
            return invalid_format(zip_field)
        zip_clean = zip_field["value"]

    # Provider.zipCode is stored as the 5-digit string, so the cleaned zip matches directly.
    providers, err = db_guard(
        DatabaseService.search_provider,
        provider_name=normalize_provider(providerName) if providerName else None,
        city=city.title() if city else None,
        state=normalize_state(state) if state else None,
        zip_code=zip_clean,
    )
    if err:
        return err

    return {
        "status": "found" if providers else "none_found",
        "success": True,
        "count": len(providers),
        "data": providers,
    }


@router.get(
    "/npi/{npi}",
    summary="Search Provider by NPI",
    description="Returns provider details using NPI. " + STATUS_DOC,
)
def get_provider_by_npi(npi: str = Path(...)):

    # Provider.npi is stored as the 10-digit string.
    provider, err = db_guard(DatabaseService.search_provider_by_npi, normalize_npi(npi))
    if err:
        return err

    if not provider:
        return none_found("Provider not found.")

    return found(provider, "Provider retrieved successfully.")


@router.get(
    "/network/{state}",
    summary="Providers by State",
    description="Returns all providers available in a particular state.",
)
def get_network_providers(state: str = Path(...)):

    providers, err = db_guard(DatabaseService.search_provider, state=normalize_state(state))
    if err:
        return err

    return {
        "status": "found" if providers else "none_found",
        "success": True,
        "count": len(providers),
        "data": providers,
    }


@router.get(
    "/city/{city}",
    summary="Providers by City",
    description="Returns all providers available in a city.",
)
def get_city_providers(city: str = Path(...)):

    providers, err = db_guard(DatabaseService.search_provider, city=city.title())
    if err:
        return err

    return {
        "status": "found" if providers else "none_found",
        "success": True,
        "count": len(providers),
        "data": providers,
    }


@router.get(
    "/zipcode/{zip_code}",
    summary="Providers by ZIP Code",
    description="Returns providers for a ZIP Code (spoken or typed, leading zeros kept). " + STATUS_DOC,
)
def get_zip_providers(zip_code: str = Path(...)):

    zip_field = process_field("zip_code", zip_code)
    if zip_field["status"] == "invalid_format":
        return invalid_format(zip_field)

    # Provider.zipCode is stored as the 5-digit string (leading zeros preserved).
    providers, err = db_guard(DatabaseService.search_provider, zip_code=zip_field["value"])
    if err:
        return err

    return {
        "status": "found" if providers else "none_found",
        "success": True,
        "count": len(providers),
        "data": providers,
    }


@router.get(
    "/{member_id}",
    summary="Get Provider",
    description="Returns provider information using Member ID (spoken or typed). " + STATUS_DOC,
)
def get_provider(member_id: str = Path(...)):

    response, db_member_id = resolve_member(member_id)
    if response:
        return response

    # Providers are linked by the MEM-prefixed member id (Provider.memberId == "MEM1001").
    provider, err = db_guard(DatabaseService.get_provider, db_member_id)
    if err:
        return err

    if not provider:
        return none_found("Provider not found.")

    return found(provider, "Provider retrieved successfully.")