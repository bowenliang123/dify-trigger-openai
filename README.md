## OpenAI Trigger

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repository:** https://github.com/bowenliang123/dify-trigger-openai

**Dify Marketplace:** https://marketplace.dify.ai/plugins/bowenliang123/openai_trigger

### OpenAI Trigger Plugin User Guide

#### What This Plugin Does
The OpenAI Trigger plugin connects your Dify workflows with [OpenAI Webhook events](https://platform.openai.com/docs/api-reference/webhook-events). When something happens in your OpenAI workspace, like receiving an update for batch, evaluation , this trigger plugin automatically starts your Dify workflows to respond to these events.


### Available Events

OpenAI's webhook events: https://platform.openai.com/docs/api-reference/webhook-events 

#### Response Events

- `response.completed`
    - Sent when a background response has been completed.
- `response.cancelled`
    - Sent when a background response has been cancelled.
- `response.failed`
    - Sent when a background response has failed.
- `response.incomplete`
    - Sent when a background response has been interrupted.

#### Batch Events

- `batch.completed`
    - Sent when a batch API request has been completed.
- `batch.cancelled`
    - Sent when a batch API request has been cancelled.
- `batch.expired`
    - Sent when a background response has failed.
- `batch.failed`
    - Sent when a batch API request has failed.

#### Finetuning Events

- `fine_tuning.job.succeeded`
    - Sent when a fine-tuning job has succeeded.
- `fine_tuning.job.failed`
    - Sent when a fine-tuning job has failed.
- `fine_tuning.job.cancelled`
    - Sent when a fine-tuning job has cancelled.
    
#### Eval Events
- `eval.run.succeeded`
    - Sent when an eval run has succeeded.
- `eval.run.failed`
    - Sent when an eval run has failed.
- `eval.run.canceled`
    - Sent when an eval run has been canceled.

#### Realtime Events
- `realtime.call.incoming`
    - Sent when Realtime API Receives a incoming SIP call.
