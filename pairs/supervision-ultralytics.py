import supervision as sv
from ultralytics import YOLO
def check():
    r = YOLO("yolo11n.pt").predict("https://ultralytics.com/images/bus.jpg", device="cpu", verbose=False)[0]
    d = sv.Detections.from_ultralytics(r)
    assert len(d) > 0, "no detections"
    return f"Supervision read {len(d)} Ultralytics detections"
