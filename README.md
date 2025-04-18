# 8086-microprocessor-emulator

A Python-based emulator simulating the **Intel 8086 microprocessor**, complete with GUI, assembler-level support, and real-time memory/register visualization. Built as an educational tool to understand low-level architecture, this project mimics the behavior of registers, flags, instructions, and stack operations — all in a user-friendly interface.

---

## Features

-  Emulation of 8086 registers (AX, BX, CX, DX, etc.)
-  Status flags: ZF, CF, SF, OF, PF
-  1MB Simulated Memory and Stack Support
-  40+ Assembly Instructions: `MOV`, `ADD`, `MUL`, `CALL`, `RET`, `LOOP`, `SHL`, `JMP`, etc.
-  Conditionals: `JE`, `JNE`, `JC`, `JNC`, etc.
-  Loops: `LOOP`, `LOOPE`, `LOOPNE`
-  GUI built with Tkinter for code input/output
-  Displays real-time register/memory updates

## Tech Stack

| Component       | Tool           |
|----------------|----------------|
| Language        | Python 3.12     |
| GUI Framework   | Tkinter         |
| IDE             | VS Code         |
| OS              | Windows 11      |
| Version Control | Git             |

## Challenges Faced
-  Implementing accurate flag logic across operations
-  Managing stack and return addresses
-  Real-time GUI updates from backend
-  Creating a flexible instruction decoding engine

## Learning Outcomes
-  Better understanding of microprocessor internals
-  OOP, Parsing, GUI development in Python
-  Assembly-level code interpretation
-  Real-time systems simulation

## Future Scope
-  Add more instruction sets (string, interrupt-based)
-  Implement two-pass assembler
-  Add .asm file support and export logs
-  Step-by-step debugger with breakpoints
-  Extend support for 8051 microcontroller

