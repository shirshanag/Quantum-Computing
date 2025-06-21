from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sim = Aer.get_backend('aer_simulator')
job = sim.run(qc, shots=1000)
results = job.result()
counts = results.get_counts(qc)
print(counts)
plot_histogram(counts)
qc.draw('mpl')

