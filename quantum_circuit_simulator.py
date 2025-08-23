import numpy as np

class Qubit:
    """
    Class representing a single qubit.
    """

    def __init__(self):
        self.state = np.array([[1], [0]])  # Initialize to |0> state

    def apply_gate(self, gate):
        """
        Apply a quantum gate to the qubit.
        """
        self.state = np.dot(gate, self.state)


class QuantumCircuit:
    """
    Class for simulating a quantum circuit.
    """

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = [Qubit() for _ in range(num_qubits)]
        self.circuit = []

    def add_gate(self, gate, target_qubit):
        """
        Add a gate to the circuit.
        """
        self.circuit.append((gate, target_qubit))

    def run(self):
        """
        Simulate the quantum circuit.
        """
        for gate, target_qubit in self.circuit:
            self.qubits[target_qubit].apply_gate(gate)

    def get_state(self):
        """
        Return the state of the entire circuit.
        """
        state_vector = np.array([1] + [0] * (2 ** self.num_qubits - 1))
        for qubit in self.qubits:
            state_vector = np.kron(state_vector, qubit.state.flatten())
        return state_vector


class QuantumGates:
    """
    Common quantum gates.
    """
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)  # Hadamard gate
    X = np.array([[0, 1], [1, 0]])  # Pauli-X (NOT) gate
    Z = np.array([[1, 0], [0, -1]])  # Pauli-Z gate
    I = np.array([[1, 0], [0, 1]])  # Identity gate
    CX = np.array([[1, 0, 0, 0],  # CNOT gate
                   [0, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 1, 0]])

def run_sample_circuit():
    """
    Example of simulating a quantum circuit.
    """
    # Create a circuit with 2 qubits
    circuit = QuantumCircuit(2)

    # Apply gates: H on qubit 0, CNOT on qubits 0 and 1
    circuit.add_gate(QuantumGates.H, 0)
    circuit.add_gate(QuantumGates.CX, (0, 1))

    # Simulate the circuit
    circuit.run()

    # Get the final state
    final_state = circuit.get_state()
    print("Final state vector:\n", final_state)


if __name__ == "__main__":
    run_sample_circuit()
