import pennylane as qml # 일반적으로 qml이란 이름으로 가져옵니다. Quantum Machine Learning의 약자입니다.
import numpy as np

dev = qml.device("default.qubit", wires=3) # device를 정의합니다.

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0) # 0번 와이어에 Hadamard 게이트를 적용합니다.)
    qml.S(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    return qml.probs()

print(qml.draw(circuit)())
qml.draw_mpl(circuit)()