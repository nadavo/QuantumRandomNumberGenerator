from QuantumRandomNumberGenerator import QuantumRandomNumberGenerator
from collections import namedtuple

"""
Generate random number between [0,N]
"""
N = 100

""" 
Rejection price [1,N] 
(increase P to reduce probability for rejection, although this increases the number of Qubits used in each round) 
"""
P = 1

"""
Credentials namedtuple for accessing IBM's Quantum Computer
"""
credentials = namedtuple("Credentials", "username password")
my_credentials = None
# my_credentials = credentials("<username>", "<password>")

"""
Boolean flag to determine if remote execution will run on IBM's simulator or on the actual hardware
"""
remote_hardware = False


def main():
    quantum_generator = QuantumRandomNumberGenerator(my_credentials, remote_hardware)
    random_number = quantum_generator.generate_random_number(N, P)
    print(f"Random number: {random_number}")


if __name__ == "__main__":
    main()
