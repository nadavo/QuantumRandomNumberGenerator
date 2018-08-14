import numpy as np
import projectq.setups.ibm
from projectq.ops import H, Measure
from projectq import MainEngine
from projectq.backends import IBMBackend


class QuantumRandomNumberGenerator:

    def __init__(self, credentials=None, remote_hardware=False):
        self.credentials = credentials
        self.remote_hardware = remote_hardware

    def initialize_quantum_engine(self):
        """
        Quantum Engine Initializer
        (pass credentials namedtuple to use IBM's Quantum Computer with your username and password, otherwise will simulate locally)
        """
        if self.credentials:
            quantum_engine = MainEngine(IBMBackend(user=self.credentials.username,
                                                   password=self.credentials.password,
                                                   use_hardware=self.remote_hardware),
                                        engine_list=projectq.setups.ibm.get_engine_list())
        else:
            quantum_engine = MainEngine()
        return quantum_engine

    def _get_random_binary_from_qubit(self):
        """
        This Function creates a new qubit,
        applies a Hadamard gate to put it in superposition,
        and then measures the qubit to get a random
        1 or 0.
        Based on example from: https://projectq.readthedocs.io/en/latest/examples.html
        """
        engine = self.initialize_quantum_engine()
        qubit = engine.allocate_qubit()
        H | qubit
        Measure | qubit
        engine.flush()
        random_binary = int(qubit)
        if isinstance(engine.backend, projectq.backends.IBMBackend):
            engine.deallocate_qubit(qubit[0])
        return random_binary

    def generate_random_number(self, n, rejection_price=1):
        """
        Algorithm which generates an integer between [0,n] uniformally at random
        Inspired by algorithm from:
        https://stackoverflow.com/questions/13209162/creating-a-random-number-generator-from-a-coin-toss
        """
        adjusted_n = n * rejection_price
        k = np.log2(adjusted_n)
        rounded_k = int(np.ceil(k))
        print(f"Getting {rounded_k} random Qubits")
        r_num = adjusted_n+1
        rejected = 0
        wasted = 0
        while r_num > adjusted_n:
            r_temp = 0
            for i in reversed(range(rounded_k)):
                r_binary = self._get_random_binary_from_qubit()
                wasted += 1
                if r_binary:
                    r_temp += 2**i
                if r_temp > adjusted_n:
                    break
            r_num = r_temp
            rejected += 1
        print(f"Rejected: {rejected-1}")
        print(f"Wasted Qubits: {wasted-rounded_k}\n")
        return r_num//rejection_price
