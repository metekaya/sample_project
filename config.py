"""
Application configuration loaded from environment variables.
Defaults are suitable for local development.
"""
import os

# Server
HOST = os.getenv("APP_HOST", "0.0.0.0")
PORT = int(os.getenv("APP_PORT", "5000"))
DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"

# Limits
MAX_LIST_SIZE = int(os.getenv("MAX_LIST_SIZE", "1000"))
MAX_STRING_LEN = int(os.getenv("MAX_STRING_LEN", "500"))
CLAMP_RANGE_LIMIT = float(os.getenv("CLAMP_RANGE_LIMIT", "1e9"))

# Cache
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "300"))
CACHE_MAX_ENTRIES = int(os.getenv("CACHE_MAX_ENTRIES", "256"))
