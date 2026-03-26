# Acceptance Levels

## Real-cloud validation

The system runs successfully against a real account and either:

- returns real resources and persists them
- or completes a valid empty-result execution path with real credentials and runtime evidence

## Empty-result validation

The runtime path is real and successful, but the current account or region has no resources of that type.

## Mock-only validation

The code exists and may have tests, but no real account evidence exists.

## Missing

The adapter, pack, runtime path, or evidence is absent.
