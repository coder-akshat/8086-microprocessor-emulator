class Registers8086:
    def __init__(self):
        self.AX = self.BX = self.CX = self.DX = 0
        self.SP = self.BP = self.SI = self.DI = 0
        self.CS = self.DS = self.ES = self.SS = 0
        self.IP = 0

        # Flags
        self.CF = 0  # Carry Flag
        self.PF = 0  # Parity Flag
        self.AF = 0  # Aux Carry Flag
        self.ZF = 0  # Zero Flag
        self.SF = 0  # Sign Flag
        self.OF = 0  # Overflow Flag
        self.TF = 0  # Trap Flag
        self.IF = 0  # Interrupt Enable Flag
        self.DF = 0  # Direction Flag

        # Stack: simulate 8086 stack (top = end of list)
        self.stack = []
        
        self.stack_address = []

    def push(self, value):
        value &= 0xFFFF
        self.stack.append(value)
        self.SP = (self.SP - 2) & 0xFFFF

    def pop(self):
        if self.stack:
            self.SP = (self.SP + 2) & 0xFFFF
            return self.stack.pop()
        return 0  

    def get_stack_content(self):
        return list(reversed(self.stack))
    
    def get(self, reg):
        """Retrieve the value of a register by name."""
        if reg == 'AX':
            return self.AX
        elif reg == 'BX':
            return self.BX
        elif reg == 'CX':
            return self.CX
        elif reg == 'DX':
            return self.DX
        elif reg == 'SP':
            return self.SP
        elif reg == 'BP':
            return self.BP
        elif reg == 'SI':
            return self.SI
        elif reg == 'DI':
            return self.DI
        elif reg == 'CS':
            return self.CS
        elif reg == 'DS':
            return self.DS
        elif reg == 'ES':
            return self.ES
        elif reg == 'SS':
            return self.SS
        elif reg == 'IP':
            return self.IP
        else:
            raise ValueError(f"Unknown register: {reg}")

    def set(self, reg, value):
        """Set the value of a register by name."""
        if reg == 'AX':
            self.AX = value
        elif reg == 'BX':
            self.BX = value
        elif reg == 'CX':
            self.CX = value
        elif reg == 'DX':
            self.DX = value
        elif reg == 'SP':
            self.SP = value
        elif reg == 'BP':
            self.BP = value
        elif reg == 'SI':
            self.SI = value
        elif reg == 'DI':
            self.DI = value
        elif reg == 'CS':
            self.CS = value
        elif reg == 'DS':
            self.DS = value
        elif reg == 'ES':
            self.ES = value
        elif reg == 'SS':
            self.SS = value
        elif reg == 'IP':
            self.IP = value
        else:
            raise ValueError(f"Unknown register: {reg}")

    def get_8bit_registers(self):
        return {
            'AL': self.AX & 0xFF,
            'AH': (self.AX >> 8) & 0xFF,
            'BL': self.BX & 0xFF,
            'BH': (self.BX >> 8) & 0xFF,
            'CL': self.CX & 0xFF,
            'CH': (self.CX >> 8) & 0xFF,
            'DL': self.DX & 0xFF,
            'DH': (self.DX >> 8) & 0xFF
        }

    def set_8bit_register(self, reg, value):
        if reg == 'AL':
            self.AX = (self.AX & 0xFF00) | (value & 0xFF)
        elif reg == 'AH':
            self.AX = (self.AX & 0x00FF) | ((value & 0xFF) << 8)
        elif reg == 'BL':
            self.BX = (self.BX & 0xFF00) | (value & 0xFF)
        elif reg == 'BH':
            self.BX = (self.BX & 0x00FF) | ((value & 0xFF) << 8)
        elif reg == 'CL':
            self.CX = (self.CX & 0xFF00) | (value & 0xFF)
        elif reg == 'CH':
            self.CX = (self.CX & 0x00FF) | ((value & 0xFF) << 8)
        elif reg == 'DL':
            self.DX = (self.DX & 0xFF00) | (value & 0xFF)
        elif reg == 'DH':
            self.DX = (self.DX & 0x00FF) | ((value & 0xFF) << 8)
