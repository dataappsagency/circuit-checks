import numpy as np
def train():
    import keras
    x = np.random.rand(64, 4).astype("float32"); y = (x.sum(axis=1) > 2).astype("float32")
    m = keras.Sequential([keras.Input((4,)), keras.layers.Dense(8, activation="relu"), keras.layers.Dense(1, activation="sigmoid")])
    m.compile(optimizer="adam", loss="binary_crossentropy")
    h = m.fit(x, y, epochs=2, verbose=0)
    assert keras.backend.backend() in ("torch", "tensorflow"), keras.backend.backend()
    assert len(h.history["loss"]) == 2
    return f"trained 2 epochs on the {keras.backend.backend()} backend"
