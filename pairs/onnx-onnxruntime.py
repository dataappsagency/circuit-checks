import numpy as np, onnx, onnxruntime as ort
from onnx import TensorProto, helper
def check():
    g = helper.make_graph([helper.make_node("Add", ["a", "b"], ["c"])], "add",
        [helper.make_tensor_value_info("a", TensorProto.FLOAT, [2]), helper.make_tensor_value_info("b", TensorProto.FLOAT, [2])],
        [helper.make_tensor_value_info("c", TensorProto.FLOAT, [2])])
    model = helper.make_model(g, opset_imports=[helper.make_opsetid("", 13)]); onnx.checker.check_model(model)
    out = ort.InferenceSession(model.SerializeToString()).run(None, {"a": np.array([1, 2], "float32"), "b": np.array([3, 4], "float32")})[0]
    assert out.tolist() == [4, 6], out
    return "ran an ONNX graph in ONNX Runtime: [1,2]+[3,4]=[4,6]"
