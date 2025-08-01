class Not():
    def __init__(self, p):
        self.p = p
    
    def evaluate(self):
        return 1 - self.p.evaluate()
    
    def backprop(self, value):
        self.p.backprop(-value)

    def step(self, size):
        self.p.step(size)

class And():
    # This value is used to prevent stall gradients when both values are at zero
    epsilon = 1e-4

    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def evaluate(self):
        return self.p.evaluate() * self.q.evaluate()
    
    def backprop(self, value):
        self.p.backprop(value * (self.q.evaluate() + self.epsilon))
        self.q.backprop(value * (self.p.evaluate() + self.epsilon))

    def step(self, value):
        self.p.step(value)
        self.q.step(value)

class Or():
    # This value is used to prevent stall gradients when both values are at zero
    epsilon = 1e-4

    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def evaluate(self):
        p = self.p.evaluate()
        q = self.q.evaluate()
        return p + q - p * q
    
    def backprop(self, value):
        self.p.backprop(value * (1 - self.q.evaluate() + self.epsilon))
        self.q.backprop(value * (1 - self.p.evaluate() + self.epsilon))

    def step(self, value):
        self.p.step(value)
        self.q.step(value)
