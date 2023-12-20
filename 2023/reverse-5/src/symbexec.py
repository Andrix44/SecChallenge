from triton import *

if __name__ == "__main__":
    for start in (0x140001B99, 0x140001C97, 0x140001C3C, 0x140001C6A, 0x140001BCC):
        pc = start
        print(hex(pc))
        ctx = TritonContext(ARCH.X86_64)
        ast = ctx.getAstContext()
        ctx.setAstRepresentationMode(AST_REPRESENTATION.PCODE)
        ctx.setMode(MODE.AST_OPTIMIZATIONS, True)
        ctx.setMode(MODE.CONSTANT_FOLDING, True)
        ctx.setMode(MODE.SYMBOLIZE_INDEX_ROTATION, True)
        ctx.setMode(MODE.MEMORY_ARRAY, True)
        ctx.setMode(MODE.SYMBOLIZE_LOAD, True)
        ctx.setMode(MODE.SYMBOLIZE_STORE, True)

        ctx.setConcreteMemoryAreaValue(0x140001B99, bytes.fromhex("0FB639438D442D008D0C4040D2C740F6D7488B9588000000483B95800000000F8572FFFFFF"))
        ctx.setConcreteMemoryAreaValue(0x140001C97, bytes.fromhex("4489EF0FAFFF0FAFFF403239488B9588000000483B95800000000F8579FEFFFF"))
        ctx.setConcreteMemoryAreaValue(0x140001C3C, bytes.fromhex("438D7CAD004002394080C703488B9588000000483B95800000000F85D4FEFFFF"))
        ctx.setConcreteMemoryAreaValue(0x140001C6A, bytes.fromhex("0FB639B1044428E940D2CF488B9588000000483B95800000000F85A7FEFFFF"))
        ctx.setConcreteMemoryAreaValue(0x140001BCC, bytes.fromhex("0FB6398D0CFD0000000080E10889F8D0E889C280E20108CA89F9C0E10580E18008D189C280E20408CA8D0CBD0000000080E14008D189FAC0EA0480E20208CA242008D040C0EF034080E7104008C7488B9588000000483B95800000000F8502FFFFFF"))
        ctx.concretizeAllMemory()

        ctx.symbolizeRegister(ctx.registers.rcx, "rcx")
        ctx.symbolizeRegister(ctx.registers.r13, "r13")

        while True:
            opcode = ctx.getConcreteMemoryAreaValue(pc, 16)
            instruction = Instruction(pc, opcode)

            ctx.disassembly(instruction)
            #print(instruction)
            if(instruction.getDisassembly().startswith("cmp")):
                break

            ctx.processing(instruction)
            pc = ctx.getConcreteRegisterValue(ctx.registers.rip)

        for i, reg in sorted(ctx.getSymbolicRegisters().items()):
            print(ctx.getRegister(i), ast.unroll(reg.getAst()))

        for i, mem in sorted(ctx.getSymbolicMemory().items()):
            print(f"[{hex(i)}]", ast.unroll(mem.getAst()))
        print("-" * 160)

