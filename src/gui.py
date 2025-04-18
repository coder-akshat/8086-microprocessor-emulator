import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from .registers import Registers8086
from .memory import Memory8086
from .instruction_engine import InstructionEngine

class EmulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8086 Emulator GUI")
        title = tk.Label(self.root,text="8086 MICROPROCESSOR EMULATOR",bg="black",fg="white",font=("Courier New", 20, "bold"))
        title.grid(row=0, column=0, columnspan=10, pady=15)
        self.root.configure(bg="black")

        # Add style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.TLabel", foreground="white", background="black", font=("Courier New", 15,"bold"))
        style.configure("Custom.TLabelframe", background="black", foreground="white", font=("Times New Roman", 18, "bold"))
        style.configure("CustomHeading.TLabelframe.Label", foreground="white", background="black", font=("Courier New", 18, "bold"))
        style.configure("Accent.TButton", background="#007acc", foreground="white", font=("Times New Roman", 15, "bold"))
        style.map("Accent.TButton", background=[("active", "#005f99")])

        self.header_font = tkfont.Font(family="Times New Roman", size=17, weight="bold")
        self.normal_font = tkfont.Font(family="Times New Roman", size=15)

        self.regs = Registers8086()
        self.engine = InstructionEngine(self.regs)
        self.memory = Memory8086()
        
        self.create_gpr_frame()
        self.create_index_pointer_frame()
        self.create_segments_frame()
        self.create_flags_display()
        self.create_stack_frame()
        self.create_memory_frame()
        self.create_program_box()

    def create_gpr_frame(self):
        frame = ttk.LabelFrame(self.root, text="REGISTERS", style="Custom.TLabelframe")
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="REGISTERS", style="CustomHeading.TLabelframe.Label"))

        self.entries = {}
        row = 0
        for reg in ['AX', 'BX', 'CX', 'DX']:
            ttk.Label(frame, text=reg, style="Custom.TLabel").grid(row=row, column=0, sticky='w')
            entry = ttk.Entry(frame, width=10, font=self.normal_font)
            entry.insert(0, "0000")
            entry.grid(row=row, column=1)
            self.entries[reg] = entry
            row += 1

        ttk.Button(frame, text="Update", command=self.update_registers, style="Accent.TButton").grid(row=row, column=0, columnspan=2, pady=5)

    def create_index_pointer_frame(self):
        frame = ttk.LabelFrame(self.root, text="IDX & PTR", style="Custom.TLabelframe")
        frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="IDX & PTR", style="CustomHeading.TLabelframe.Label"))

        row = 0
        for reg in ['SP', 'BP', 'SI', 'DI']:
            ttk.Label(frame, text=reg, style="Custom.TLabel").grid(row=row, column=0, sticky='w')
            entry = ttk.Entry(frame, width=10, font=self.normal_font)
            entry.insert(0, "0000")
            entry.grid(row=row, column=1)
            self.entries[reg] = entry
            row += 1

        ttk.Button(frame, text="Update", command=self.update_registers, style="Accent.TButton").grid(row=row, column=0, columnspan=2, pady=5)

    def create_segments_frame(self):
        frame = ttk.LabelFrame(self.root, text="SEGMENTS", style="Custom.TLabelframe")
        frame.grid(row=1, column=2, padx=10, pady=10, sticky="n")
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="SEGMENTS", style="CustomHeading.TLabelframe.Label"))

        row = 0
        for reg in ['IP', 'CS', 'DS', 'ES', 'SS']:
            ttk.Label(frame, text=reg, style="Custom.TLabel").grid(row=row, column=0, sticky='w')
            entry = ttk.Entry(frame, width=10, font=self.normal_font)
            entry.insert(0, "0000")
            entry.grid(row=row, column=1)
            self.entries[reg] = entry
            row += 1

        ttk.Button(frame, text="Update", command=self.update_registers, style="Accent.TButton").grid(row=row, column=0, columnspan=2, pady=5)

    def create_flags_display(self):
        frame = ttk.LabelFrame(self.root, text="FLAGS", style="Custom.TLabelframe")
        frame.grid(row=1, column=4, padx=10, pady=10, sticky="n")
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="FLAGS", style="CustomHeading.TLabelframe.Label"))

        self.flag_labels = {}

        status_box = ttk.LabelFrame(frame, text="STATUS", style="Custom.TLabelframe")
        status_box.grid(row=1, column=0, padx=5, pady=5, sticky="n")
        status_box.configure(style="Custom.TLabelframe")
        status_box.configure(labelwidget=ttk.Label(status_box, text="STATUS", style="CustomHeading.TLabelframe.Label"))

        for i, flag in enumerate(["CF", "PF", "AF", "ZF", "SF", "OF"]):
            label = ttk.Label(status_box, text=f"{flag} = 0", style="Custom.TLabel")
            label.grid(row=i, column=0, sticky="w")
            self.flag_labels[flag] = label

        control_box = ttk.LabelFrame(frame, text="CONTROL", style="Custom.TLabelframe")
        control_box.grid(row=1, column=1, padx=5, pady=5, sticky="n")
        control_box.configure(style="Custom.TLabelframe")
        control_box.configure(labelwidget=ttk.Label(control_box, text="CONTROL", style="CustomHeading.TLabelframe.Label"))

        for i, flag in enumerate(["TF", "IF", "DF"]):
            label = ttk.Label(control_box, text=f"{flag} = 0", style="Custom.TLabel")
            label.grid(row=i, column=0, sticky="w")
            self.flag_labels[flag] = label

    def create_stack_frame(self):
        frame = ttk.LabelFrame(self.root, text="STACK", style="Custom.TLabelframe")
        frame.grid(row=2, column=1, padx=5, pady=5, sticky="n")
        frame.configure(labelwidget=ttk.Label(frame, text="STACK", style="CustomHeading.TLabelframe.Label"))

        self.stack_box = tk.Text(frame, height=10, width=20, bg="black", fg="white", insertbackground="white", font=self.normal_font)
        self.stack_box.pack(padx=5, pady=5)

        ttk.Button(frame, text="Refresh Stack", command=self.refresh_stack_display, style="Accent.TButton").pack(pady=5)
    
    def create_memory_frame(self):
        frame = ttk.LabelFrame(self.root, text="ADDRESS CALCULATION", style="Custom.TLabelframe")
        frame.grid(row=1, column=3, padx=5, pady=5, sticky="n")
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="ADDRESS CALCULATION", style="CustomHeading.TLabelframe.Label"))

        ttk.Label(frame, text="Segment:", style="Custom.TLabel").grid(row=0, column=0)
        self.seg_entry = ttk.Entry(frame, width=6, font=self.normal_font)
        self.seg_entry.insert(0, "1000")
        self.seg_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Offset:", style="Custom.TLabel").grid(row=1, column=0)
        self.off_entry = ttk.Entry(frame, width=6, font=self.normal_font)
        self.off_entry.insert(0, "0020")
        self.off_entry.grid(row=1, column=1)

        self.addr_label = ttk.Label(frame, text="Physical Address: ----", style="Custom.TLabel")
        self.addr_label.grid(row=2, column=0, columnspan=2, pady=5)

        ttk.Button(frame, text="Compute", command=self.compute_physical_address, style="Accent.TButton").grid(row=3, column=1, columnspan=1, padx=5, pady=5)
        
    def refresh_stack_display(self):
        self.stack_box.delete("1.0", tk.END)
        stack_content = self.regs.get_stack_content()

        display = []
        sp = self.regs.SP
        for i, value in enumerate(stack_content):
            addr = (sp + i * 2) & 0xFFFF  # mimic 8086 16-bit wrap
            display.append(f"{hex(addr)}: {format(value, '04X')}")

        if not display:
            self.stack_box.insert(tk.END, "Stack is empty.")
        else:
            self.stack_box.insert(tk.END, "\n".join(display))

    def create_program_box(self):
        frame = ttk.LabelFrame(self.root, text="PROGRAM INPUT", style="Custom.TLabelframe")
        frame.grid(row=2, column=3, columnspan=2, padx=5, pady=5)
        frame.configure(style="Custom.TLabelframe")
        frame.configure(labelwidget=ttk.Label(frame, text="PROGRAM INPUT", style="CustomHeading.TLabelframe.Label"))

        self.program_box = tk.Text(frame, height=10, width=60, bg="black", fg="white", insertbackground="white", font=self.normal_font)
        self.program_box.pack(padx=5, pady=5)

        tk.Button(frame, text="Run Program", command=self.run_program, bg="#007acc", fg="white", font=self.header_font).pack(pady=5)

    def update_registers(self):
        for reg, entry in self.entries.items():
            try:
                value = int(entry.get(), 16)
                setattr(self.regs, reg, value)
            except:
                entry.delete(0, tk.END)
                entry.insert(0, "0000")

    def compute_physical_address(self):
        try:
            seg = int(self.seg_entry.get(), 16)
            off = int(self.off_entry.get(), 16)
            addr = self.memory.get_physical_address(seg, off)
            self.addr_label.config(text=f"Physical Address: {hex(addr)}")
        except:
            self.addr_label.config(text="Invalid Input")

    def refresh_register_entries(self):
        for reg, entry in self.entries.items():
            value = getattr(self.regs, reg)
            entry.delete(0, tk.END)
            entry.insert(0, format(value, '04X'))

        for flag in self.flag_labels:
            value = getattr(self.regs, flag)
            self.flag_labels[flag].config(text=f"{flag} = {value}")

    def run_program(self):
        program = self.program_box.get("1.0", tk.END).strip().split('\n')
        output = self.engine.run_program(program)
        self.refresh_register_entries()

