# TODO

- Return type
- Assert messages
- Docs for each method

# Principles

## Right-BICEP

- Are the returned results **right**?
- Are the results at **boundaries** correct? The boundaries can be identified by following these aspects (CORRECT):
    - Conformance: Compliance with a formal definition of the type
    - Ordering (for example, of an ordered list)
    - Range
    - References (to external objects or methods) 
    - Existence (of a method, parameter)
    - Cardinality: Tests with 0, 1 and N elements
    - Time
- Check for **inverse** relationships, where the opeerations supports it.
- **Cross-check** results using other means.
- Force **error** condition to happen.
- Are **performance** characteristics verified?

## FIRST

- Fast
- Isolated
- Repeatable
- Self-validating
- Timely

---

N tests
each test has its own principles an techniques of unit testing