from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import string

class SimpleQuantumPasswordManager:
    def generate_password(self, length=12):
        """Versión simplificada en un solo archivo"""
        char_set = string.ascii_letters + string.digits
        
        passwords = []
        for _ in range(length):
            qc = QuantumCircuit(1, 1)
            qc.h(0)
            qc.measure(0, 0)
            
            simulator = AerSimulator()
            compiled_circuit = transpile(qc, simulator)
            job = simulator.run(compiled_circuit, shots=1)
            result = job.result()
            counts = result.get_counts()
            
            random_num = int(list(counts.keys())[0], 9)
            char_index = random_num % len(char_set)
            passwords.append(char_set[char_index])
        
        return ''.join(passwords)

# Uso
if __name__ == "__main__":
    manager = SimpleQuantumPasswordManager()
    print("Contraseña generada:", manager.generate_password(16))
