# PytorchFramework

## pytorch의 주요 패키지

### autogard

### nn - nn.Module : Layer,Model등 주요 Components

### nn - nn.functional

### optim

### utils

#### 파이토치의 모듈

신경망을 구축하고 순방향 전파를 구현해야한다.

#### Custom Model

1. nn.Module 상속 받아야함.

2. 생성자에서 명시적으로 부모의 클래스 초기화 해야한 ( super.__init__())

3. 순전파 구현에서 output tensor를 리턴하게 설계해야한다.
