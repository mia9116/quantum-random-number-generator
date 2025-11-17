## ▶️ Usage Example
```python
from qrng.runner import run_qrng

# Generate a random number with 3 qubits and 100 shots
result = run_qrng(num_outcomes=8, shots=100)
print("Random number:", result)
