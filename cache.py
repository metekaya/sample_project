"""
Simple in-memory LRU cache with TTL eviction.
Thread-safe for single-process use via threading.Lock.
"""
import time
import threading
from collections import OrderedDict
from config import CACHE_TTL_SECONDS, CACHE_MAX_ENTRIES


class TTLCache:
    def __init__(self, max_entries: int = CACHE_MAX_ENTRIES, ttl: int = CACHE_TTL_SECONDS):
        self._store: OrderedDict = OrderedDict()
        self._max = max_entries
        self._ttl = ttl
        self._lock = threading.Lock()

    def get(self, key: str):
        with self._lock:
            if key not in self._store:
                return None
            value, expires_at = self._store[key]
            if time.time() > expires_at:
                del self._store[key]
                return None
            # Move to end (LRU touch)
            self._store.move_to_end(key)
            return value

    def set(self, key: str, value) -> None:
        with self._lock:
            if key in self._store:
                self._store.move_to_end(key)
            self._store[key] = (value, time.time() + self._ttl)
            if len(self._store) > self._max:
                self._store.popitem(last=False)  # evict oldest

    def delete(self, key: str) -> bool:
        with self._lock:
            if key in self._store:
                del self._store[key]
                return True
            return False

    def clear(self) -> None:
        with self._lock:
            self._store.clear()

    def size(self) -> int:
        with self._lock:
            return len(self._store)

    def evict_expired(self) -> int:
        """Remove all expired entries. Returns count removed."""
        now = time.time()
        with self._lock:
            expired = [k for k, (_, exp) in self._store.items() if now > exp]
            for k in expired:
                del self._store[k]
            return len(expired)


# Module-level default cache instance
default_cache = TTLCache()
