# Drift Checklist

Check for these common drift types:

- outdated class or module names
- APIs described but not implemented
- implementation exists but design never updated
- validation evidence described as real-cloud when only mock evidence exists
- default-disabled features described as delivered default behavior
- pagination, filters, and runtime defaults inconsistent across docs
- old port, path, startup, or database statements

Recommended output:

- drift item
- source document
- actual behavior
- correction action
- whether it changes delivery scope or just wording
