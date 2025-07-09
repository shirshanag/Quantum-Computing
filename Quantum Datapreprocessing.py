#Custom Fidelity Function for Quantum Kernel
def custom_fidelity(sampler,circuit1, circuit2):
  combined_circuit=circuit1.compose(circuit2.inverse())
  job=sampler.run([combined_circuit])
  result=job.result()
  probabilities=result.quasi_dists[0]
  fidelity=probabilities.get(0,0)
  return fidelity
#Make synthetic dataset
X,y=make_moons(n_samples=200,noise=0,random_state=42)
#Standardise Data
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
#Train-Test split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)
#Initialise the updated sampler
sampler=StatevectorSampler()
from qiskit.circuit.library import ZZFeatureMap
feature_map = ZZFeatureMap(feature_dimension=2, reps=3, entanglement='linear')

#Define fidelity quatum kernel based on custom fidelity quantum kernel
class CustomFidelityQuantumKernel(FidelityQuantumKernel):
    def __init__(self, feature_map, sampler):
        super().__init__(feature_map=feature_map, fidelity=None) 
        self.sampler = sampler

    def _compute_fidelity(self, circuit_1, circuit_2):
        return custom_fidelity(self.sampler, circuit_1, circuit_2)

#Compute quantum kernel matrix
quantum_kernel=CustomFidelityQuantumKernel(feature_map=feature_map,sampler=sampler)
#Compute Quantum Kernel Matrix
X_train_kernel=quantum_kernel.evaluate(X_train)
X_test_kernel=quantum_kernel.evaluate(X_test,X_train)
#Train Classical SVM using quantum kernel
svm=SVC(kernel='precomputed')
svm.fit(X_train_kernel,y_train)
#Predict on test set
y_pred=svm.predict(X_test_kernel)
#Compute the accuracy
accuracy=np.mean(y_pred==y_test)
print("Accuracy:",accuracy*100,"%")
