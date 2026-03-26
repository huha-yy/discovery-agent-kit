# Specification Chain

For a Discovery-style project, the spec chain should normally be checked in this order:

1. SOW or external requirement baseline
2. project specification
3. overview design
4. detailed design
5. implementation and tests
6. acceptance and validation artifacts

Expected rule:

- upper-layer documents define scope
- lower-layer documents explain realization
- acceptance documents describe evidence

If acceptance claims exceed implementation, acceptance is wrong.
If design claims exceed implementation, design is stale unless the gap is explicitly marked planned or deferred.
