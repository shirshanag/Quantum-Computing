#Import the Libraries

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#Two qubit Quantum Circuit
qc=QuantumCircuit(2)

#Apply Quantum Gates

qc.h(0)
qc.cx(0,1)
qc.measure_all()

#Simulate the result

sim=Aer.get_backend('aer_simulator')
job=sim.run(qc,shots=1000)
results=job.result()

#Draw the Circuit

qc.draw('mpl')

#Print and Plot the Counts 

print(counts)
plot_histogram(counts)
