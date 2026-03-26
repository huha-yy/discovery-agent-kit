# Triage Model

## Goal

Locate the failing layer before proposing a fix.

## Recommended order

Check in this order:

1. process and port state
2. environment variables and file paths
3. database availability and lock state
4. worker and scheduler state
5. pack version online or offline state
6. account credentials and verification result
7. adapter request and response shape
8. UI or API presentation layer

## Evidence rule

Try to collect at least one fact from each relevant layer:

- runtime fact: process, port, or background worker state
- application fact: log line, stack trace, or structured error
- data fact: record state, task status, or pack status
- vendor fact: real API error, permission denial, or empty-result response

## Outcome

At the end of triage, produce:

- failing layer
- likely root cause
- confidence level
- next verification step
