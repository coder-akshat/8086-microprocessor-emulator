class Memory8086:
    def __init__(self, size=1024 * 1024):  
        self.memory = bytearray(size)

    def read(self, address, size=1):
        value = int.from_bytes(self.memory[address:address + size], byteorder='big')
        return f'{value:0{size * 2}X}' 

    def write(self, address, value, size=1):
        if isinstance(value, str):
            value = int(value, 16)  
        self.memory[address:address + size] = value.to_bytes(size, byteorder='big')

    def get_physical_address(self, segment, offset):
        if isinstance(segment, str):
            segment = int(segment, 16)
        if isinstance(offset, str):
            offset = int(offset, 16)
        address = (segment << 4) + offset
        return address

    def get_physical_address_hex(self, segment, offset):
        addr = self.get_physical_address(segment, offset)
        return f'{addr:05X}'  

    def read_at_segment_offset(self, segment, offset, size=1):
        addr = self.get_physical_address(segment, offset)
        return self.read(addr, size)

    def write_at_segment_offset(self, segment, offset, value, size=1):
        addr = self.get_physical_address(segment, offset)
        self.write(addr, value, size)
