# Credential Patterns

## Aliyun

- type: `aksk`
- common keys:
  - `access_key_id`
  - `access_key_secret`

## Tencent Cloud

- type: `aksk`
- common keys:
  - `secret_id`
  - `secret_key`
  - optional `token`

## Huawei Cloud

- type: `aksk` or project-based auth
- common keys:
  - `access_key_id`
  - `access_key_secret`
  - optional `project_id`

## VMware

- type: `basic`
- common keys:
  - `username`
  - `password`
  - optional endpoint or mock flags

## Rule

Normalize user input into the keys expected by the target adapter and keep any vendor-specific extra fields explicit.
