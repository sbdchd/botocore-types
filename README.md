# botocore-types

## generating stubs

1. stubgen

2. delete the `docs` folder as that's internal

3. replace vendored imports with normal package imports. Don't want to have
   to type `requests` when types for it already exist in `typeshed`.
