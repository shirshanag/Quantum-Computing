from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

qc=QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

simulator=Aer.get_backend('aer_simulator')

qc=qc.copy()
qc.save_statevector()

job=simulator.run(qc,shots=100)
result=job.result()
count=result.get_counts()
print(count)

flavors={"0":"Chocolate","1":"Vanilla"}
labels=[flavors.get(key,key) for key in count.keys()]
plt.bar(labels,count.values(),color=['Brown','Green'])
plt.title("Quantum Machine: Chocolate and Vanilla Flavors")
plt.xlabel("Flavors")
plt.ylabel("Counts")
plt.show()
