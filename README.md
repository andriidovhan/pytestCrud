## PytestCRUD
Test user's CRUD requests using [pytest](https://docs.pytest.org/) + [GoRest(Online REST API)](https://gorest.co.in/).

### How to:
1. Create a `config.py` file according to the `config.py.example` file.
2. Build container:
```
docker build -t test-container
```
3. Run tests:
```
docker run -it --rm --name crud_user_tests test-container
```