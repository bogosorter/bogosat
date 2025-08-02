class Not():
    def __init__(self, p):
        self.p = p
        self.value = None
    
    def evaluate(self):
        if self.value is not None:
            return self.value
        
        self.value = 1 - self.p.evaluate()
        return self.value
    
    def backprop(self, value):
        self.p.backprop(-value)

    def step(self, size):
        self.p.step(size)
        self.value = None

class And():
    # This value is used to prevent stall gradients when both values are at zero
    epsilon = 1e-4

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.value = None
    
    def evaluate(self):
        if self.value is not None:
            return self.value
        
        self.value = self.p.evaluate() * self.q.evaluate()
        return self.value
    
    def backprop(self, value):
        self.p.backprop(value * (self.q.evaluate() + self.epsilon))
        self.q.backprop(value * (self.p.evaluate() + self.epsilon))

    def step(self, value):
        self.p.step(value)
        self.q.step(value)
        self.value = None

class Or():
    # This value is used to prevent stall gradients
    epsilon = 1e-4

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.value = None
    
    def evaluate(self):
        if self.value is not None:
            return self.value
        
        p = self.p.evaluate()
        q = self.q.evaluate()
        self.value = p + q - p * q
        return self.value
    
    def backprop(self, value):
        self.p.backprop(value * (1 - self.q.evaluate() + self.epsilon))
        self.q.backprop(value * (1 - self.p.evaluate() + self.epsilon))

    def step(self, value):
        self.p.step(value)
        self.q.step(value)
        self.value = None

class Implies():
    def __init__(self, p, q):
        self.formula = Or(Not(p), q)
        self.value = None
    
    def evaluate(self):
        if self.value is not None:
            return self.value
        
        self.value = self.formula.evaluate()
        return self.value

    def backprop(self, value):
        self.formula.backprop(value)
    
    def step(self, value):
        self.formula.step(value)
        self.value = None
