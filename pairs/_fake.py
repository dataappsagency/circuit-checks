"""Deterministic embeddings, so vector-store checks need no model or account."""
import hashlib
def vec(text, dim=16):
    h = hashlib.sha256(text.encode()).digest()
    return [((h[i % len(h)] / 255.0) - 0.5) for i in range(dim)]
