# Implement Grovers's to search for a marked state of 2 qubit
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
#Grover oracle function for seaching mark state |11>
def grover_oracle():
  oracle=QuantumCircuit(2)
  oracle.cz(0,1)
  return oracle
  #Difffusion Operator function
def diffusion_operator():
  diffusion=QuantumCircuit(2)
  diffusion.h([0,1])
  diffusion.x([0,1])
  diffusion.cz(0,1)
  diffusion.x([0,1])
  diffusion.h([0,1])
  return diffusion
  #Initiate the Circuit and the function
qc=QuantumCircuit(2,2)
qc.h([0,1])
qc=qc.compose(grover_oracle())
qc=qc.compose(diffusion_operator())
qc.measure([0,1],[0,1])
#Activate the simulator
simulator=Aer.get_backend('aer_simulator')
job=simulator.run(qc,shots=1000)
result=job.result()
counts=result.get_counts()

qc.draw('mpl')
#Plot the measurement
print(counts)
plot_histogram(counts)
