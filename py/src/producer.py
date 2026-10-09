from model.sketch import Sketch
from hash.hasher import Hasher


class Producer:
    precision_bits: int
    sketch: Sketch
    hasher: Hasher

    def __init__(self, m: int, hasher: Hasher):
        if (m < 2 or m > 32):
            raise ValueError("")
        
        # numer of bucket must be power of 2
        if (m & m-1) != 0:
            raise ValueError("")
        
        self.precision_bits = m.bit_length()-1
        self.sketch = Sketch(m, [0]*m)
        self.hasher = hasher

    def calculate(self, data) -> None:
        h = self.hasher.hash_value(data)
        remain_bits = 64 - self.precision_bits

        bucket_idx = h >> remain_bits
        remainder = h & ((1 << remain_bits) - 1)

        incoming_rank = remain_bits - remainder.bit_length() + 1
        self.sketch.ranks[bucket_idx] = max(incoming_rank, self.sketch.ranks[bucket_idx])

    def complete(self) -> Sketch:
        return self.sketch