# -*- coding: utf-8 -*-
"""Building Qubits and Interacting with Quantum Gates.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GTcFf1G8bUE65cwQpjxvdhg6AszzaTQ_

# **Quantum Gates**
---
<br>

### **Project Structure**
**Part 1**: [Creating, measuring, and outputing](#p1)

**Part 2**: [Quantum Circuits in Cirq](#p2)

**Part 3**: [Multiple Gates](#p3)

<br>


**Before starting, run the code below to import all necessary functions and libraries.**
"""

# @title
!pip install cirq --quiet
import cirq
import cirq_web
print("Libraries imported successfully!")

"""<a name="p1"></a>

---
## **Part 1: Creating, measuring, and outputing**
---

### **Problem #1.1**

Create a qubit, create an empty circuit, add a measurement to your circuit, and output the circuit.

#### **Solution**
"""

my_qubit = cirq.NamedQubit("q0")
my_circuit = cirq.Circuit()
my_circuit.append(cirq.measure(my_qubit))
my_circuit

"""### **Problem #1.2**

Simulate the results of `my_circuit`.

#### **Solution**
"""

sim = cirq.Simulator()
result = sim.run(my_circuit)
result

"""<a name="p2"></a>

---
## **Part 2: Quantum Circuits in Cirq**
---

### **Problem #2.1**

**Together:**
1. Create a qubit with label ``"q0"``.
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **X gate** applied to it.
4. Then print out the circuit.
5. Print out the final state vector, dirac notation and bloch sphere representations of the qubit in the circuit.

#### **Solution**
"""

qubit = cirq.NamedQubit("q0")
qc = cirq.Circuit()
qc.append( cirq.X(qubit) )
print( qc )

state_vector = cirq.final_state_vector(qc)
ket = cirq.dirac_notation( state_vector=state_vector )
print( state_vector, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=state_vector )

sim = cirq.Simulator()
result = sim.run(my_circuit)
result

"""### **Problem #2.2**

**Independently**
1. Create a qubit with label ``"q0"``.
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **H gate** applied to it.
4. Then print out the circuit.
5. Print out the state vector, dirac notation, and bloch sphere of the qubit in the quantum circuit.

#### **Solution**
"""

qubit = cirq.NamedQubit("q0")
my_quantum_circuit_H = cirq.Circuit( )
my_quantum_circuit_H.append(cirq.H(qubit))
print( my_quantum_circuit_H )

sv = cirq.final_state_vector(my_quantum_circuit_H)
ket = cirq.dirac_notation( state_vector=state_vector )
print( sv, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=state_vector )

"""### **Problem #2.3**

Append a measurement to your circuit in Problem #2.2. Simulate the results of your circuit.

#### **Solution**
"""

qc.append(cirq.measure(qubit))
sim = cirq.Simulator()
result = sim.run(my_circuit)
result

"""<a name="p3"></a>

---
## **Part 3: Multiple Gates**
---

### **Problem #3.1**

**Together:**
1. Create a qubit with label ``"q0"``
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **Z gate** applied to it.
4. Apply another **Z gate** to the qubit.
5. Then print out the circuit.
6. Print out the state vector, dirac notation, and bloch sphere of the qubit in the quantum circuit.

####**Solution**
"""

qubit = cirq.NamedQubit("q0")
qc = cirq.Circuit( )
qc.append(cirq.Z(qubit))
qc.append(cirq.Z(qubit))
print(qc )

sv = cirq.final_state_vector(qc)
ket = cirq.dirac_notation( state_vector=sv )
print( sv, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=sv )

"""### **Problem #3.2**

**Together:**
1. Create a qubit with label ``"q0"``
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **Z gate** applied to it.
4. Apply an **H gate** to the qubit.
5. Then print out the circuit.
6. Print out the state vector, dirac notation, and bloch sphere of the qubit in the quantum circuit.

#### **Solution**
"""

qubit = cirq.NamedQubit("q0")
qc = cirq.Circuit()
qc.append(cirq.Z(qubit))
qc.append(cirq.H(qubit))
print(qc)

sv = cirq.final_state_vector(qc)
ket = cirq.dirac_notation( state_vector=sv )
print( sv, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=sv )

"""### **Problem #3.3**

**Independently:**
1. Create a qubit with label ``"q0"``
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **H gate** applied to it.
4. Apply a **Z gate** to the qubit.
5. Then print out the circuit.
6. Print out the state vector, dirac notation, and bloch sphere of the qubit in the quantum circuit.

#### **Solution**
"""

qubit = cirq.NamedQubit("q0")
qc = cirq.Circuit()
qc.append(cirq.H(qubit))
qc.append(cirq.Z(qubit))
print(qc )

sv = cirq.final_state_vector(qc)
ket = cirq.dirac_notation( state_vector=sv )
print( sv, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=sv )

"""### **Problem #3.4**


**Independently:**
1. Create a qubit with label ``"q0"``
2. Create an empty quantum circuit.
3. Append the qubit you created to the empty quantum circuit with an **H gate** applied to it.
4. Apply an **X gate** to the qubit.
5. Apply a **Z gate** to the qubit.
6. Apply an **H gate** to the qubit.
7. Then print out the circuit.
8. Print out the state vector, dirac notation, and bloch sphere of the qubit in the quantum circuit.

#### **Solution**
"""

qubit = cirq.NamedQubit("q0")
qc = cirq.Circuit()
qc.append(cirq.H(qubit))
qc.append(cirq.X(qubit))
qc.append(cirq.Z(qubit))
qc.append(cirq.H(qubit))
print(qc )

sv = cirq.final_state_vector(qc)
ket = cirq.dirac_notation( state_vector=sv )
print( sv, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=sv )

"""
© 2023 The Coding School Projects"""
