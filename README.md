# Sample Project

A small Flask-based Python API used as a test target for Synapse agent runs.

## Structure

```
main.py         Flask app — all API endpoints
utils.py        Utility functions: clamp, flatten, slugify
stats.py        Statistics: mean, median, mode
validators.py   Input validation for all endpoints
errors.py       Centralised error response helpers
cache.py        Thread-safe in-memory LRU cache with TTL
config.py       Configuration from environment variables
tests.py        pytest suite covering all endpoints
requirements.txt  pip dependencies
```

## Known Issues

- `stats.py` — `mean()` has an off-by-one bug (divides by `len-1` instead of `len`)
- `stats.py` — `median()` and `mode()` raise `NotImplementedError`
- `utils.py` — `slugify()` uses `_` as word separator instead of `-`
- `main.py` — endpoints do no input validation (pass raw user input directly to functions)
- `errors.py` — exists but is not wired into any endpoint yet

## Run

```bash
pip install -r requirements.txt
python main.py            # starts on port 5000
pytest tests.py -v        # run test suite
```

## API Endpoints

| Method | Path | Body | Description |
|--------|------|------|-------------|
| GET | /health | — | Health check |
| POST | /greet | `{"name": "Alice"}` | Greeting |
| POST | /add | `{"a": 2, "b": 3}` | Addition |
| POST | /clamp | `{"value": 5, "min": 0, "max": 10}` | Clamp a value |
| POST | /flatten | `{"nested": [1, [2, 3]]}` | Flatten nested list |
| POST | /slugify | `{"text": "Hello World!"}` | URL-safe slug |
| POST | /mean | `{"numbers": [1,2,3]}` | Arithmetic mean |
| POST | /median | `{"numbers": [1,2,3]}` | Median (not implemented) |
| POST | /mode | `{"numbers": [1,2,2,3]}` | Mode (not implemented) |
