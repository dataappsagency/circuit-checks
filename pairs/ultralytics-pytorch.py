from ultralytics import YOLO
def check():
    r = YOLO("yolo11n.pt").predict("https://ultralytics.com/images/bus.jpg", device="cpu", verbose=False)
    n = len(r[0].boxes)
    assert n > 0, "no detections"
    return f"detected {n} objects on PyTorch (CPU)"
