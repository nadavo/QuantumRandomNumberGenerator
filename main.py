from QuantumRandomNumberGenerator import QuantumRandomNumberGenerator

"""
Generate random number between [0,N]
"""
N = 100

""" 
Rejection price [1,N] 
(increase P to reduce probability for rejection, although this increases the number of Qubits used in each round) 
"""
P = 10

"""
Credentials dictionary for accessing IBM's Quantum Computer
credentials = {"username": "<your username>", "password": "<your password>"} 
"""
credentials = None


def main():
    quantum_generator = QuantumRandomNumberGenerator(credentials)
    random_number = quantum_generator.generate_random_number(N, P)
    print(f"Random number: {random_number}")


if __name__ == "__main__":
    main()
