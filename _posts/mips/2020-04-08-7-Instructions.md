---
title:  "7 Instructions"
tags: MIPS
toc: true
---

# Intro
정리 안하려다가 시간 남아서 했다... n번 언급하지만 EduMIPS64 기준이다. 몇 개는 더 있고, 몇 개는 더 없고 그렇다.

# Instructions
아래와 같이 operand를 나타낸다.

Operand | Description
---|---
`d` | Destination register, 연산 결과가 저장되는 장소
`s` | Source register
`t` | Target register
`imm` | Immediate value
`sa` | Shift amount
`offset(base)` | Load/Store 시 메모리 주소 (mem[base + offset])
`offset` | PC-relative addressing에서의 타겟 주소
`target` | Absolute addressing에서의 타겟 주소

아래와 같은 prefix와 postfix가 붙을 수 있다. 

Pre/Postfix | Description
---|---
Prefix `D` | Double-word 레지스터 연산
Postfix `U` | Unsigned 연산
Postfix `V` | shamt 대신 타겟 레지스터의 lower 5 byte를 사용
Postfix `I` | 맨 뒤 operand 대신 immediate value를 사용

또, pseudoinstruction을 고려하지 않고 그냥 EduMIPS64 매뉴얼에 있는 명령어를 받아 적었다. 대놓고 pseudo인 것은 뺐다.

## ALU Instruction
### Arithmetic Operation

Instruction | Description
---|---
`ADD d, s, t` (`DADD`, `ADDU`, `DADDU`, `ADDI`, `ADDIU`, `DADDI`, `DADDIU`, `DADDUI`) | d = s + t
`SUB d, s, t` (`DSUB`, `SUBU`, `DSUBU`) | d = s - t
`MULT s, t` (`DMULT`, `MULTU`, `DMULTU`, `DMULU`) | d \*= t
`DIV s, t` (`DDIV`, `DIVU`, `DDIVU`) | d /= t
`SLL d, t, sa` (`DSLL`, `SLLV`, `DSLLV`) | d = t << sa (logical)
`SRL d, t, sa` (`DSRL`, `SRLV`, `DSRLV`) | d = t >> sa (logical)
`SRA d, t, sa` (`DSRA`, `SRAV`, `DSRAV`) | d = t >> sa (arithmetic)

### Logical Operation

Instruction | Description
---|---
`AND d, s, t` (`ANDI`) | d = s & t
`OR d, s, t` (`ORI`) | d = s \| t
`XOR d, s, t` (`XORI`) | d = s ^ t

### Conditionals

Instruction | Description
---|---
`SLT d, s, t` (`SLTU`, `SLTI`, `SLTUI`) | d = (s < t)
`MOVN d, s, t` | d = (t != 0) ? s : d
`MOVZ d, s, t` | d = (t == 0) ? s : d

### Etc.

Instruction | Description
---|---
`LUI t, imm` | 16-bit의 `imm`을 `t`의 상위 16-bit에 저장, 하위 비트 clear
`MFLO d` (`MFHI`) | `LO`, 또는 `HI` 레지스터 값을 `d`에 저장.

## Load / Store Instruction

Instruction | Description
---|---
`LB d, offset(base)` (`LBU`) | d = Mem[offset(base)] (in byte)
`LH d, offset(base)` (`LHU`) | d = Mem[offset(base)] (in half word)
`LW d, offset(base)` (`LWU`) | d = Mem[offset(base)] (in word)
`LD d, offset(base)` | d = Mem[offset(base)] (in double word)
`SB t, offset(base)` | Mem[offset(base)] = t (in byte)
`SH t, offset(base)` | Mem[offset(base)] = t (in half word)
`SW t, offset(base)` | Mem[offset(base)] = t (in word)
`SD t, offset(base)` | Mem[offset(base)] = t (in double word)

## Flow Control Instruction

Instruction | Description
---|---
`JALR t` | R31(ra) = (address of next instruction), PC = t
`JAL target` | PC = target
`J target` | PC = target (unconditional)
`JR rs` | PC = rs
`B offset` | branch to offset (unconditional)
`BEQ s, t, offset` | if s == t then branch to offset
`BEQZ s, offset` | if s == 0 then branch to offset
`BGEZ s, offset` | if s > 0 then branch to offset
`BNE s, t, offset` | if s != t then branch to offset
`BNEZ s, offset` | if s != 0 then branch to offset


  
