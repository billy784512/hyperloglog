from typing import Protocol
import hashlib
import mmh3

class Hasher(Protocol):
    def hash_value(self, data: bytes) -> int:
        ...

class MurmurHasher:
    def hash_value(self, data: bytes) -> int:
        h64, _ = mmh3.hash64(data, seed=0, signed=False)
        return h64
    
class Sha256Hasher:
    def hash_value(self, data: bytes) -> int:
        digest = hashlib.sha256(data.encode("utf-8")).digest()
        return int.from_bytes(digest[:8], byteorder="big")
