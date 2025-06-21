from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
#Create quantum circuit with one qubit and one classical bit
qc=QuantumCircuit(1,1)
#create a hadamard gate
qc.h(0)
#Measure the qubit
qc.measure(0,0)
#use qiskit simulator
sim=Aer.get_backend('aer_simulator')
#Run the quantum circuit on the simulator
job=sim.run(qc,shots=1000)
results=job.result()
#Get measurement result
counts=results.get_counts(qc)
print(counts)
#Plot Histogram
plot_histogram(counts)
#Draw the circuit
qc.draw('mpl')
