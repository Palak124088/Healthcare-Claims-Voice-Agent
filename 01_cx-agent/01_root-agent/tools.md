# update_root_state

from typing import Dict, Any

def update_root_state(
    requested_intent: str = "",
    consent_status: str = "",
    increment_consent_attempts: bool = False,
    increment_outofscope_attempts: bool = False,
    increment_unclear_attempts: bool = False,
) -> Dict[str, Any]:
    """
    Updates Root agent session state for the Healthcare Claims Voice Assistant.
    Records the caller's intent and consent status, and reliably increments the retry
    counters for consent declines, out-of-scope requests, and unclear intents. Counters
    are incremented in code so they are accurate and do not depend on the model counting.

    Args:
        requested_intent: The caller's supported intent, e.g. "claim_status",
            "eligibility_check", "benefits_inquiry", "provider_lookup". Leave empty to skip.
        consent_status: "granted" or "declined". Leave empty to skip.
        increment_consent_attempts: True to add 1 to the consent decline counter.
        increment_outofscope_attempts: True to add 1 to the out-of-scope counter.
        increment_unclear_attempts: True to add 1 to the unclear-intent counter.

    Returns:
        A dictionary with the current intent, consent status, and the three counters.
    """

    # Field groups, like the teammate's tool but only the fields this agent needs.
    string_fields = {"requested_intent", "consent_status"}
    number_fields = {"consent_attempts", "outofscope_attempts", "unclear_attempts"}

    allowed_intents = [
        "claim_status", "claim_history", "claim_submission", "claim_update",
        "claim_deletion", "eligibility_check", "benefits_inquiry",
        "provider_lookup", "pre_authorization_status",
    ]

    saved = {}

    def save(name, value):
        # Empty strings are ignored, so a skipped argument does not overwrite state.
        if value is not None and value != "":
            set_variable(name, value)
            saved[name] = value

    def increment(name):
        current = get_variable(name) or 0
        new_value = int(current) + 1
        set_variable(name, new_value)
        saved[name] = new_value
        return new_value

    # Set the intent, validated against the allowed list.
    if requested_intent:
        if requested_intent in allowed_intents:
            save("requested_intent", requested_intent)
        else:
            save("requested_intent", "unsupported")

    # Set consent status.
    save("consent_status", consent_status)

    # Increment counters in code.
    if increment_consent_attempts:
        increment("consent_attempts")
    if increment_outofscope_attempts:
        increment("outofscope_attempts")
    if increment_unclear_attempts:
        increment("unclear_attempts")

    return {
        "saved": saved,
        "requested_intent": get_variable("requested_intent"),
        "consent_status": get_variable("consent_status"),
        "consent_attempts": get_variable("consent_attempts") or 0,
        "outofscope_attempts": get_variable("outofscope_attempts") or 0,
        "unclear_attempts": get_variable("unclear_attempts") or 0,
    }