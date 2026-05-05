# numpy_interop.py — Verify torch.from_numpy() and Tensor.numpy() interop.

import numpy as np

print("=== from_numpy: 1-D array ===")
arr = np.array([1.0, 2.0, 3.0], dtype=np.float32)
t = torch.from_numpy(arr)
print("numpy array:", arr.tolist())
print("tensor:", t)
print("> shape correct:", t.shape == (3,))
print("> values correct:", t.allclose(torch.tensor([1.0, 2.0, 3.0])))

print("\n=== from_numpy: 2-D array ===")
arr2d = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
t2d = torch.from_numpy(arr2d)
print("numpy array:", arr2d.tolist())
print("tensor:", t2d)
print("> shape correct:", t2d.shape == (2, 2))
print("> values correct:", t2d.allclose(torch.tensor([[1.0, 2.0], [3.0, 4.0]])))

print("\n=== numpy(): tensor -> ndarray ===")
t3 = torch.tensor([10.0, 20.0, 30.0])
a3 = t3.numpy()
print("tensor:", t3)
print("numpy type:", type(a3).__name__)
print("numpy values:", a3.tolist())
print("> type is ndarray:", isinstance(a3, np.ndarray))
print("> values correct:", a3.tolist() == [10.0, 20.0, 30.0])

print("\n=== numpy(): 2-D tensor ===")
t4 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
a4 = t4.numpy()
print("numpy shape:", list(a4.shape))
print("numpy values:", a4.tolist())
print("> shape correct:", list(a4.shape) == [2, 2])
print("> values correct:", a4.tolist() == [[1.0, 2.0], [3.0, 4.0]])

print("\n=== numpy(): requires grad error ===")
t5 = torch.tensor([1.0, 2.0], requires_grad=True)
try:
    t5.numpy()
    print("> ERROR: should have raised RuntimeError")
except RuntimeError as e:
    print("Got expected RuntimeError:", str(e)[:50])
    print("> requires_grad error raised correctly:", True)

print("\n=== numpy() after detach ===")
t6 = torch.tensor([5.0, 6.0], requires_grad=True)
a6 = t6.detach().numpy()
print("values:", a6.tolist())
print("> detach().numpy() works:", a6.tolist() == [5.0, 6.0])

print("\n=== round-trip: numpy -> tensor -> numpy ===")
original = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=np.float32)
roundtrip = torch.from_numpy(original).numpy()
print("original:", original.tolist())
print("round-trip:", roundtrip.tolist())
print("> round-trip correct:", original.tolist() == roundtrip.tolist())

print("\nAll numpy_interop checks passed.")
