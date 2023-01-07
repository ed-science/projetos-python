class LogicGate:
    def __init__(self, gate_name):
        self.name = gate_name
        self.output = None 
    
    def getName(self):
        return self.name 
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None 
        self.pinB = None
    
    def getPinA(self):
        return self.putPinA() if self.pinA is None else self.pinA
    
    def getPinB(self):
        return self.putPinB() if self.pinB is None else self.pinB
    
    def putPinA(self):
        return int(
            input(f"Digite a entrada do Pino A para a porta {self.getName()} : ")
        )
    
    def putPinB(self):
        return int(
            input(f"Digite a entrada do Pino B para a porta {self.getName()} : ")
        )

class UnaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pinA = None 
    
    def getPinA(self):
        return self.putPinA() if self.pinA is None else self.pinA
    
    def putPinA(self):
        return int(
            input(f"Digite a entrada do Pino A para a porta {self.getName()} : ")
        )

class ANDGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        return 1 if a == 1 and b == 1 else 0

class ORGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        return 1 if a == 1 or b == 1 else 0

class NOTGate(UnaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
    
    def performGateLogic(self):
        a = self.getPinA()

        return 0 if a == 1 else 1