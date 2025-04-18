class InstructionEngine:
    def __init__(self, registers):
        self.regs = registers
        self.stack_int = []

    def parse_and_execute(self, instruction: str):
        tokens = instruction.strip().upper().replace(',', ' ').split()
        print(f"Executing: {instruction}")
        
        if len(tokens) == 1 and tokens[0] in ['STC', 'CLC', 'STD', 'CLD', 'STI', 'CLI','STT', 'CLT', 'STZ', 'CLZ', 'STS', 'CLS','STO', 'CLO', 'STA', 'CLA', 'STP', 'CLP','RET']:
            if tokens[0] == 'STC':
                return self._stc()
            elif tokens[0] == 'CLC':
                return self._clc()
            elif tokens[0] == 'STD':
                return self._std()
            elif tokens[0] == 'CLD':
                return self._cld()
            elif tokens[0] == 'STI':
                return self._sti()
            elif tokens[0] == 'CLI':
                return self._cli()
            elif tokens[0] == 'STT':
                return self._stt()
            elif tokens[0] == 'CLT':
                return self._clt()
            elif tokens[0] == 'STZ':
                return self._stz()
            elif tokens[0] == 'CLZ':
                return self._clz()
            elif tokens[0] == 'STS':
                return self._sts()
            elif tokens[0] == 'CLS':
                return self._cls()
            elif tokens[0] == 'STO':
                return self._sto()
            elif tokens[0] == 'CLO':
                return self._clo()
            elif tokens[0] == 'STA':
                return self._sta()
            elif tokens[0] == 'CLA':
                return self._cla()
            elif tokens[0] == 'STP':
                return self._stp()
            elif tokens[0] == 'CLP':
                return self._clp()
            elif tokens[0] == 'RET':
                return self._ret()
        
        if len(tokens) == 2 and tokens[0] in ['MUL','IMUL','DIV','IDIV','INC','DEC','NOT','PUSH','POP','SAL','SAR','SHL','SHR','ROL','ROR','RCL','RCR','JMP','JE','JNE','JC','JNC','JS','JNS','JO','JNO','JP','JNP','JA','JNA','JB','JNB','CALL','LOOP','LOOPE','LOOPNE']:
            if  tokens[0] == 'MUL':
                return self._mul(tokens[1])
            elif tokens[0] == 'IMUL':
                return self._imul(tokens[1])
            elif tokens[0] == 'DIV':
                return self._div(tokens[1])
            elif tokens[0] == 'IDIV':
                return self._idiv(tokens[1])
            elif tokens[0] == 'INC':
                return self._inc(tokens[1])
            elif tokens[0] == 'DEC':
                return self._dec(tokens[1])
            elif tokens[0] == 'NOT':
                return self._not(tokens[1])
            elif tokens[0] == 'PUSH':
                return self._push(tokens[1])
            elif tokens[0] == 'POP':
                return self._pop(tokens[1])
            elif tokens[0] == 'SHL':
                return self._shl(tokens[1])
            elif tokens[0] == 'SHR':
                return self._shr(tokens[1])
            elif tokens[0] == 'SAL':
                return self._sal(tokens[1])
            elif tokens[0] == 'SAR':
                return self._sar(tokens[1])
            elif tokens[0] == 'RCL':
                return self._rcl(tokens[1])
            elif tokens[0] == 'RCR':
                return self._rcr(tokens[1])
            elif tokens[0] == 'ROL':
                return self._rol(tokens[1])
            elif tokens[0] == 'ROR':
                return self._ror(tokens[1])
            elif tokens[0] == 'JMP':
                return self._jmp(tokens[1])
            elif tokens[0] == 'JE':
                return self._je(tokens[1])
            elif tokens[0] == 'JNE':
                return self._jne(tokens[1])
            elif tokens[0] == 'JC':
                return self._jc(tokens[1])
            elif tokens[0] == 'JNC':
                return self._jnc(tokens[1])
            elif tokens[0] == 'JS':
                return self._js(tokens[1])
            elif tokens[0] == 'JNS':
                return self._jns(tokens[1])
            elif tokens[0] == 'JO':
                return self._jo(tokens[1])
            elif tokens[0] == 'JNO':
                return self._jno(tokens[1])
            elif tokens[0] == 'JP':
                return self._jp(tokens[1])
            elif tokens[0] == 'JNP':
                return self._jnp(tokens[1])
            elif tokens[0] == 'JA':
                return self._ja(tokens[1])
            elif tokens[0] == 'JNA':
                return self._jna(tokens[1])
            elif tokens[0] == 'JB':
                return self._jb(tokens[1])
            elif tokens[0] == 'JNB':
                return self._jnb(tokens[1])
            elif tokens[0] == 'CALL':
                return self._call(tokens[1])
            elif tokens[0] == 'LOOP':
                return self._loop(tokens[1])
            elif tokens[0] == 'LOOPE':
                return self._loope(tokens[1])
            elif tokens[0] == 'LOOPNE':
                return self._loopne(tokens[1])
        
        if len(tokens) < 3:
            return "Invalid instruction"

        op, dest, src = tokens[0], tokens[1], tokens[2]

        if op == 'MOV':
            return self._mov(dest, src)
        elif op == 'ADD':
            return self._add(dest, src)
        elif op == 'SUB':
            return self._sub(dest, src)
        elif op == 'ADC':
            return self._adc(dest, src)
        elif op == 'SBB':
            return self._sbb(dest, src)
        elif op == 'CMP':
            return self._cmp(dest, src)
        elif op == 'XCHG':
            return self._xchg(dest,src)
        elif op == 'AND':
            return self._and(dest, src)
        elif op == 'OR':
            return self._or(dest, src)
        elif op == 'XOR':
            return self._xor(dest, src)
        else:
            return f"Unsupported instruction: {op}"

    def update_flags(self, result, operand1=None, operand2=None, operation=''):
        full_result = result  
        result &= 0xFFFF  

        if operation not in ['MOV', 'XCHG', 'PUSH', 'POP', 'LEA', 'NOP','STC','CLC', 'STD', 'CLD', 'STI', 'CLI', 'STT', 'CLT', 'STZ', 'CLZ', 'STS', 'CLS','STO', 'CLO', 'STA', 'CLA', 'STP', 'CLP']:
            self.regs.ZF = 1 if result == 0 else 0
            self.regs.SF = 1 if (result >> 15) & 1 else 0
            self.regs.PF = 1 if bin(result & 0xFF).count('1') % 2 == 0 else 0

        if operation in ['ADD', 'ADC']:
            full_result = operand1 + operand2
            self.regs.CF = 1 if full_result > 0xFFFF else 0
            self.regs.OF = 1 if ((operand1 ^ operand2) & 0x8000 == 0) and ((operand1 ^ result) & 0x8000) else 0
            self.regs.AF = 1 if ((operand1 ^ operand2 ^ result) & 0x10) else 0

        elif operation in ['SUB', 'CMP', 'SBB']:
            full_result = operand1 - operand2
            self.regs.CF = 1 if operand1 < operand2 else 0
            self.regs.OF = 1 if ((operand1 ^ operand2) & 0x8000) and ((operand1 ^ result) & 0x8000) else 0
            self.regs.AF = 1 if ((operand1 ^ operand2 ^ result) & 0x10) else 0

        elif operation == 'INC':
            self.regs.OF = 1 if operand1 == 0x7FFF else 0
            self.regs.AF = 1 if ((operand1 ^ 1 ^ result) & 0x10) else 0

        elif operation == 'DEC':
            self.regs.OF = 1 if operand1 == 0x8000 else 0
            self.regs.AF = 1 if ((operand1 ^ 1 ^ result) & 0x10) else 0

        elif operation in ['AND', 'OR', 'XOR']:
            self.regs.CF = 0
            self.regs.OF = 0
            self.regs.AF = 0  

        elif operation == 'NOT':
            pass  

        elif operation in ['SHL', 'SAL']:
            if isinstance(operand1, str):
                operand1 = int(operand1, 16)
            if isinstance(result, str):
                result = int(result, 16)
            self.regs.CF = (operand1 >> (16 - 1)) & 1
            self.regs.OF = ((operand1 >> 15) ^ (result >> 15)) & 1

        elif operation in ['SHR', 'SAR']:
            if isinstance(operand1, str):
                operand1 = int(operand1, 16)
            if isinstance(result, str):
                result = int(result, 16)
            self.regs.CF = operand1 & 1
            self.regs.OF = 0  

        elif operation in ['ROL', 'ROR', 'RCL', 'RCR']:
            pass

        elif operation in ['MUL', 'IMUL']:
            self.regs.CF = self.regs.OF = 1 if result > 0xFFFF else 0
        
        elif operation == 'STC':
            self.regs.CF = 1
        
        elif operation == 'STP':
            self.regs.PF = 1
        
        elif operation == 'STA':
            self.regs.AF = 1
        
        elif operation == 'STZ':
            self.regs.ZF = 1
        
        elif operation== 'STS':
            self.regs.SF = 1
        
        elif operation == 'STO': 
            self.regs.OF = 1
        
        elif operation== 'CLC':
            self.regs.CF = 0
        
        elif operation == 'CLP':
            self.regs.PF = 0
        
        elif operation == 'CLA':
            self.regs.AF = 0
        
        elif operation == 'CLZ':
            self.regs.ZF = 0
        
        elif operation == 'CLS':
            self.regs.SF = 0
        
        elif operation =='CLO':
            self.regs.OF = 0
        
        elif operation == 'STD':
            self.regs.DF = 1
        
        elif operation == 'STI':
            self.regs.IF = 1
        
        elif operation == 'STT':
            self.regs.TF = 1
        
        elif operation == 'CLD':
            self.regs.DF = 0
        
        elif operation == 'CLI':
            self.regs.IF = 0
        
        elif operation == 'CLT':
            self.regs.TF = 0
    
    def _get_value(self, operand):
        if operand.startswith('[') and operand.endswith(']'):
            reg = operand[1:-1]  
            value = getattr(self.regs, reg, None)
            if value is None:
                raise ValueError(f"Invalid register in indirect addressing: {reg}")
            return value
        try:
            return int(operand.replace('H', ''), 16)
        except ValueError:
            pass
        return getattr(self.regs, operand, None)

    def _set_value(self, dest, value):
        if hasattr(self.regs, dest):
            setattr(self.regs, dest, value & 0xFFFF)
        else:
            raise ValueError(f"Unsupported destination operand: {dest}")
    
    def _mov(self, dest, src):
        src_val = self._get_value(src)
        if src_val is None:
            return f"Invalid source: {src}"

        if hasattr(self.regs, dest):
            setattr(self.regs, dest, src_val & 0xFFFF)
            return f"{dest} = {hex(src_val)}"
        return f"Invalid destination: {dest}"

    def _add(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        if src_val is None or dest_val is None:
            return "Invalid register/operand"
        result = (dest_val + src_val) & 0xFFFF
        setattr(self.regs, dest, result)
        self.update_flags(result, dest_val, src_val, operation='ADD')
        return f"{dest} += {hex(src_val)} => {hex(result)}"

    def _adc(self, dest, src):
        dest_val = self._get_value(dest)
        src_val = self._get_value(src)
        carry = self.regs.CF if hasattr(self.regs, 'CF') else 0
        result = dest_val + src_val + carry
        setattr(self.regs, dest, result & 0xFFFF)
        self.update_flags(result, dest_val, src_val, operation='ADC')
        return f"{dest} = {result & 0xFFFF} (with carry)"
    
    def _sub(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        if src_val is None or dest_val is None:
            return "Invalid operands"
        result = (dest_val - src_val) & 0xFFFF
        self.update_flags(result, dest_val, src_val, operation='SUB')
        setattr(self.regs, dest, result)
        return f"{dest} = {hex(result)}"

    def _sbb(self, dest, src):
        dest_val = self._get_value(dest)
        src_val = self._get_value(src)
        borrow = self.regs.CF if hasattr(self.regs, 'CF') else 0
        result = dest_val - src_val - borrow
        setattr(self.regs, dest, result & 0xFFFF)  
        self.update_flags(result, dest_val, src_val, operation='SBB')
        return f"{dest} = {result & 0xFFFF} (with borrow)"

    def _cmp(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        result = (dest_val - src_val) & 0xFFFF
        self.update_flags(result, dest_val, src_val, operation='SUB')
        return f"{dest} compared with {src}"
    
    def _xchg(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        setattr(self.regs, dest, src_val)
        setattr(self.regs, src, dest_val)
        return f"{dest} exchanged with {src}"

    def _mul(self, dest):
        ax = self._get_value('AX')
        dest_val = self._get_value(dest)

        result = ax * dest_val
        self.regs.AX = result & 0xFFFF
        self.regs.DX = (result >> 16) & 0xFFFF

        self.update_flags(result, ax, dest_val, operation='MUL')

        return f"Result of MUL: AX = {hex(self.regs.AX)}, DX = {hex(self.regs.DX)}"

    def _imul(self, dest):
        ax = self._get_value('AX')
        dest_val = self._get_value(dest)
        signed_ax = ax if ax < 0x8000 else ax - 0x10000
        signed_op = dest_val if dest_val < 0x8000 else dest_val - 0x10000
        result = signed_ax * signed_op
        self.regs.AX = result & 0xFFFF
        self.regs.DX = (result >> 16) & 0xFFFF
        self.regs.CF = self.regs.OF = int(result < -32768 or result > 32767)
        self.update_flags(result, signed_ax, signed_op, operation='IMUL')
        return f"Result of IMUL: AX = {hex(self.regs.AX)}, DX = {hex(self.regs.DX)}"

    def _div(self, dest):
        dest_val = self._get_value(dest)
        if dest_val == 0:
            raise ZeroDivisionError("Division by zero")
        dividend = (self._get_value('DX') << 16) | self._get_value('AX')
        quotient = dividend // dest_val
        remainder = dividend % dest_val
        if quotient > 0xFFFF:
            raise OverflowError("Quotient too large for AX")
        self.regs.AX = quotient & 0xFFFF
        self.regs.DX = remainder & 0xFFFF
        return f"Result of DIV: AX (Quotient) = {hex(self.regs.AX)}, DX (Remainder) = {hex(self.regs.DX)}"

    def _idiv(self, dest):
        dest_val = self._get_value(dest)
        if dest_val == 0:
            raise ZeroDivisionError("Division by zero")
        dividend = (self._get_value('DX') << 16) | self._get_value('AX')
        if self._get_value('DX') & 0x8000:
            dividend -= (1 << 32)
        signed_op = dest_val if dest_val < 0x8000 else dest_val - 0x10000
        quotient = int(dividend / signed_op)
        remainder = int(dividend % signed_op)
        if quotient < -32768 or quotient > 32767:
            raise OverflowError("Quotient out of 16-bit range")
        self.regs.AX = quotient & 0xFFFF
        self.regs.DX = remainder & 0xFFFF
        return f"Result of IDIV: AX (Quotient) = {hex(self.regs.AX)}, DX (Remainder) = {hex(self.regs.DX)}"

    def _inc(self, dest):
        dest_val = self._get_value(dest)
        result = (dest_val + 1) & 0xFFFF  
        setattr(self.regs, dest, result)
        self.update_flags(result, dest_val, 1, operation='INC')
        return f"Result of INC: {dest} = {hex(result)}"

    def _dec(self, dest):
        dest_val = self._get_value(dest)
        result = (dest_val - 1) & 0xFFFF  
        setattr(self.regs, dest, result)
        self.update_flags(result, dest_val, 1, operation='DEC')
        return f"Result of DEC: {dest} = {hex(result)}"
    
    def _and(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        result = dest_val & src_val
        result &= 0xFFFF 
        self.update_flags(result, operation='AND')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _xor(self, dest, src):
        src_val = self._get_value(src)
        dest_val = self._get_value(dest)
        result = dest_val ^ src_val
        result &= 0xFFFF 
        self.update_flags(result, operation='XOR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _or(self, dest, src):
        val1 = self._get_value(dest)
        val2 = self._get_value(src)
        result = val1 | val2
        result &= 0xFFFF 
        self.update_flags(result, operation='OR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"
    
    def _not(self, dest):
        val = self._get_value(dest)
        result = (~val) & 0xFFFF
        self.update_flags(result, operation='NOT')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def get(self, reg):
        return getattr(self.regs, reg)

    def set(self, reg, value):
        setattr(self.regs, reg, value)

    def push(self, value):
        value &= 0xFFFF  
        self.regs.stack.append(value)
        self.regs.SP = (self.regs.SP - 2) & 0xFFFF  

    def pop(self):
        if self.regs.stack:
            self.regs.SP = (self.regs.SP + 2) & 0xFFFF  
            return self.regs.stack.pop()
        return 0  

    def _push(self, reg):
        value = self.get(reg)  
        self.push(value)
        self.update_flags(value, operation='PUSH')  
        return f"PUSH {reg}"

    def _pop(self, reg):
        value = self.pop()  
        self.set(reg, value)
        self.update_flags(value, operation='POP') 
        return f"POP {reg}"

    def _shl(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for SHL"
        self.regs.CF = (val >> (16 - count)) & 1
        result = (val << count) & 0xFFFF
        self.update_flags(result, val2, operation='SHL')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"
    
    def _sal(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for SAL"
        result = (val << count) & 0xFFFF
        self.update_flags(result, val2, operation='SAL')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _shr(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for SHR"
        self.regs.CF = (val >> (count - 1)) & 1
        result = (val >> count) & 0xFFFF
        self.update_flags(result, val2, operation='SHR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _sar(self, dest, count=1):
        val = val2=self._get_value(dest)
        if val is None:
            return "Invalid operand for SAR"
        sign = val & 0x8000
        for _ in range(count):
            self.regs.CF = val & 1
            val = (val >> 1) | sign
        result = val & 0xFFFF
        self.update_flags(result, val2, operation='SAR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _rol(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for ROL"
        count %= 16
        result = ((val << count) | (val >> (16 - count))) & 0xFFFF
        self.regs.CF = (result >> 0) & 1
        self.update_flags(result, val2, operation='ROL')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _ror(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for ROR"
        count %= 16
        result = ((val >> count) | (val << (16 - count))) & 0xFFFF
        self.regs.CF = (result >> 15) & 1
        self.update_flags(result, val2, operation='ROR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _rcl(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for RCL"
        for _ in range(count):
            carry = self.regs.CF
            msb = (val >> 15) & 1
            val = ((val << 1) | carry) & 0xFFFF
            self.regs.CF = msb
        result = val
        self.update_flags(result, val2, operation='RCL')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    def _rcr(self, dest, count=1):
        val = val2= self._get_value(dest)
        if val is None:
            return "Invalid operand for RCR"
        for _ in range(count):
            carry = self.regs.CF
            lsb = val & 1
            val = (val >> 1) | (carry << 15)
            self.regs.CF = lsb
        result = val & 0xFFFF
        self.update_flags(result, val2, operation='RCR')
        self._set_value(dest, result)
        return f"{dest} = {hex(result)}"

    
    # Flag instructions
    def _stc(self): self.update_flags(0, operation='STC'); return "STC"
    def _clc(self): self.update_flags(0, operation='CLC'); return "CLC"
    def _std(self): self.update_flags(0, operation='STD'); return "STD"
    def _cld(self): self.update_flags(0, operation='CLD'); return "CLD"
    def _sti(self): self.update_flags(0, operation='STI'); return "STI"
    def _cli(self): self.update_flags(0, operation='CLI'); return "CLI"
    def _stt(self): self.update_flags(0, operation='STT'); return "STT"
    def _clt(self): self.update_flags(0, operation='CLT'); return "CLT"
    def _stz(self): self.update_flags(0, operation='STZ'); return "STZ"
    def _clz(self): self.update_flags(0, operation='CLZ'); return "CLZ"
    def _sts(self): self.update_flags(0, operation='STS'); return "STS"
    def _cls(self): self.update_flags(0, operation='CLS'); return "CLS"
    def _sto(self): self.update_flags(0, operation='STO'); return "STO"
    def _clo(self): self.update_flags(0, operation='CLO'); return "CLO"
    def _sta(self): self.update_flags(0, operation='STA'); return "STA"
    def _cla(self): self.update_flags(0, operation='CLA'); return "CLA"
    def _stp(self): self.update_flags(0, operation='STP'); return "STP"
    def _clp(self): self.update_flags(0, operation='CLP'); return "CLP"
    
    def _jmp(self, label):
        if label not in self.labels:
            return f"Label not found: {label}"
        self.regs.IP = self.labels[label]
        return "JUMPED"
    
    #Conditional Jumps
    def _je(self, label): return self._jmp(label) if self.regs.ZF == 1 else "Skipped JE"
    def _jne(self, label): return self._jmp(label) if self.regs.ZF == 0 else "Skipped JNE"
    def _jc(self, label): return self._jmp(label) if self.regs.CF == 1 else "Skipped JC"
    def _jnc(self, label): return self._jmp(label) if self.regs.CF == 0 else "Skipped JNC"
    def _js(self, label): return self._jmp(label) if self.regs.SF == 1 else "Skipped JS"
    def _jns(self, label): return self._jmp(label) if self.regs.SF == 0 else "Skipped JNS"
    def _jo(self, label): return self._jmp(label) if self.regs.OF == 1 else "Skipped JO"
    def _jno(self, label): return self._jmp(label) if self.regs.OF == 0 else "Skipped JNO"
    def _jp(self, label): return self._jmp(label) if self.regs.PF == 1 else "Skipped JP"
    def _jnp(self, label): return self._jmp(label) if self.regs.PF == 0 else "Skipped JNP"
    def _ja(self, label): return self._jmp(label) if self.regs.CF == 0 and self.regs.ZF == 0 else "Skipped JA"
    def _jna(self, label): return self._jmp(label) if self.regs.CF == 1 or self.regs.ZF == 1 else "Skipped JNA"
    def _jb(self, label): return self._jmp(label) if self.regs.CF == 1 else "Skipped JB"
    def _jnb(self, label): return self._jmp(label) if self.regs.CF == 0 else "Skipped JNB"

    def _call(self, label):
        if label not in self.labels:
            return f"Label not found: {label}"
        
        return_address = self.regs.IP + 1
        self.stack_int.append(return_address)  
        self.regs.IP = self.labels[label]
        return "JUMPED"
    
    def _ret(self):
        if not self.stack_int:
            return "Stack underflow on RET"
        self.regs.IP = self.stack_int.pop()
        return "JUMPED"
    
    def _loop(self, label):
        self.regs.CX = (self.regs.CX - 1) & 0xFFFF  
        if self.regs.CX != 0:
            if label not in self.labels:
                return f"Label not found: {label}"
            self.regs.IP = self.labels[label]
            return "JUMPED"
        return  

    def _loope(self, label):
        if self.regs.ZF == 1 and self.regs.CX > 0:
            self.regs.CX -= 1
            return self._jmp(label)
        return "Skipped LOOPE"

    def _loopne(self, label):
        if self.regs.ZF == 0 and self.regs.CX > 0:
            self.regs.CX -= 1
            return self._jmp(label)
        return "Skipped LOOPNE"

    
    def run_program(self, program_lines):
        self.labels = {}  
        self.program = []  
        self.regs.IP = 0  
        for line in program_lines:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"): 
                label = line[:-1]
                self.labels[label] = len(self.program)  
            else:
                self.program.append(line) 
        while self.regs.IP < len(self.program):
            current_instruction = self.program[self.regs.IP]
            result = self.parse_and_execute(current_instruction)  
            if result != "JUMPED":
                self.regs.IP += 1  
