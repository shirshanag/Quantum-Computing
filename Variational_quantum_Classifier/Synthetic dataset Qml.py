#Generate dataset
X,y=make_classification(
    n_samples=100,
    n_features=2,#Total no of features
    n_redundant=0,#No redundant data
    n_informative=2,#Ensure sum <= total
    random_state=42,
    n_clusters_per_class=1
)
#Normalise the data
scaler=StandardScaler()
X=scaler.fit_transform(X)
#Split into training and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#Define Quantum feature map
feature_map=ZZFeatureMap(feature_dimension=2,reps=2,entanglement='linear')
#Define VQC
ansatz=RealAmplitudes(num_qubits=2,reps=3,entanglement='linear')
#Initialize State vector sampler
sampler=StatevectorSampler()
#Define Fidelity Quantum Kernel
quantum_kernel=FidelityQuantumKernel(feature_map=feature_map,fidelity=sampler)
#Instantiate the optimizer
optimizer=COBYLA(maxiter=100)
#Define a custom Pass manager for transpilation
pass_manager=PassManager([
    Optimize1qGatesDecomposition(basis=['u3','cx']),
    CommutativeCancellation()
])
#Define Variational Quantum classifier
vqc=VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer,
    sampler=sampler,
    pass_manager=pass_manager # To Avoid Transpilation warning
)
#Train the model
vqc.fit(X_train,y_train)
#Evaluate the model
y_pred=vqc.predict(X_test)
#Accuracy
accuracy=np.mean(y_pred==y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")
vqc.circuit.draw(output='mpl')
