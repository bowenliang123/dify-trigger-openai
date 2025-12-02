import logging
from collections.abc import Mapping
from typing import Any

from dify_plugin.entities.trigger import Variables
from dify_plugin.errors.trigger import TriggerProviderOAuthError, EventIgnoreError
from standardwebhooks import Webhook, WebhookVerificationError
from werkzeug import Request


def verify_webhook_signature(
        webhook_secret: str,
        data: str | bytes,
        headers: dict[str, Any],
) -> None:
    """
    Verify the webhook signature using the provided secret.
    :param webhook_secret:
    :param data:
    :param headers:
    :return:
    :raises TriggerProviderOAuthError: If the webhook signature is invalid.
    """
    try:
        webhook = Webhook(webhook_secret)
        webhook.verify(data, headers)
    except WebhookVerificationError as e:
        logging.exception(e)
        raise TriggerProviderOAuthError(f"Invalid webhook signature or secret, {str(e)}")


def transform_webhook(expected_event_type: str,
                      request: Request,
                      parameters: Mapping[str, Any],
                      payload: Mapping[str, Any],
                      ) -> Variables:
    if not payload:
        raise ValueError("No payload received")

    # filter by event type
    event_type = payload.get("type")
    if expected_event_type != event_type:
        raise EventIgnoreError(f"Expecting event type '{expected_event_type}', got '{event_type}' in payload.")

    return Variables(variables={**payload})
