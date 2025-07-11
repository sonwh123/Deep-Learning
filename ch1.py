import torch

import torch.nn as nn
import torch.optim as optim

# 간단한 뉴럴 네트워크 클래스 정의
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# 예시: 입력 10, 은닉층 5, 출력 1
model = SimpleNN(input_size=10, hidden_size=5, output_size=1)

# 손실 함수와 옵티마이저 정의
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 더미 데이터로 학습 예시
x = torch.randn(16, 10)  # 배치 크기 16, 입력 10
y = torch.randn(16, 1)   # 배치 크기 16, 출력 1

# 순전파, 손실 계산, 역전파, 파라미터 업데이트
outputs = model(x)
loss = criterion(outputs, y)
optimizer.zero_grad()
loss.backward()
optimizer.step()

print("Loss:", loss.item())
print("hello")