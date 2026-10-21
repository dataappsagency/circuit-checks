import numpy as np, onnxruntime as ort
from sklearn.linear_model import LogisticRegression
from skl2onnx import to_onnx
def check():
    x = np.random.RandomState(0).rand(80, 3).astype("float32"); y = (x[:, 0] > 0.5).astype(int)
    clf = LogisticRegression().fit(x, y)
    sess = ort.InferenceSession(to_onnx(clf, x[:1]).SerializeToString())
    onnx_pred = sess.run(None, {sess.get_inputs()[0].name: x})[0]
    assert (onnx_pred == clf.predict(x)).all(), "predictions differ"
    return "a scikit-learn model exported to ONNX gave identical predictions in ONNX Runtime"
