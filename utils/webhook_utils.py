from collections.abc import Mapping
from typing import Any

import standardwebhooks
from dify_plugin.entities.trigger import Variables
from dify_plugin.errors.trigger import TriggerProviderOAuthError
from werkzeug import Request


def verify_webhook_signature(
        webhook_secret: str,
        data: str | bytes,
        headers: dict[str, Any],
) -> None:
    try:
        webhook = standardwebhooks.Webhook(webhook_secret)
        webhook.verify(data, headers)
    except standardwebhooks.WebhookVerificationError as e:
        raise TriggerProviderOAuthError(f"Invalid webhook signature or secret, {str(e)}")


def transform_webhook(request: Request, parameters: Mapping[str, Any], payload: Mapping[str, Any]) -> Variables:
    payload = request.get_json(silent=True) or {}

    # Verify webhook signature
    webhook_secret = parameters.get("webhook_secret", "")
    verify_webhook_signature(webhook_secret, request.data, request.headers)

    return Variables(variables={**payload})
