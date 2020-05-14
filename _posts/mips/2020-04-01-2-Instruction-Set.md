---
title:  "2 Instruction Set"
tags: MIPS
toc: true
---

# Intro
MIPS의 ISA는 꽤 간결하다. 다 읊어도 그리 많지는 않겠지만, 그러진 않을 예정이다.


# Classification of Instructions
명령어 집합(instruction set)을 분류하는 두 가지 방법이 있다. 기능 별로 분류할 수도 있고, 명령어 구조에 따라 분류할 수도 있다.

명령어의 기능 및 역할에 따라, ALU instruction, Load/Store instruction, Flow control instruction으로 나누어 보자. 

- ALU(Arithmetic Logic Unit) : 산술적/논리적 연산을 수행하는 명령어.
- Load/Store : 레지스터와 메모리 간 데이터 이동에 관여하는 명령어.
- Flow control : 명령어 수행의 순서에 관여하여, 결과적으로 흐름(flow)을 제어하는 명령어.

물론, 이들 외에도 다른 명령어들이 있다.

- `SYSCALL` : 시스템 콜에 대응되는 명령어. 14번 레지스터(or `t6`)의 값을 파라미터로 받아, 1번 레지스터에 return value를 저장한다. 가능한 한 POSIX convention을 따르며, `exit`(0), `open`(1), `close`(2), `read`(3), `write`(4), `printf`(5),  여섯 종류의 시스템 콜이 있다.
- `BREAK` : 디버깅 등을 목적으로 예외를 거는 명령어.
- `NOP` : 아무것도 하지 않는 명령어.
- `TRAP` : `SYSCALL`의 (더 이상 사용하지 않는) alias.
- `HALT` : `SYSCALL 0`(`exit`)의 (더 이상 사용하지 않는) alias.

그리고, 명령어 구조에 따라 I 타입, R 타입, J 타입으로 분류할 수도 있다. 우선 알아둬야 할 점은, 각각의 인스트럭션은 (피연산자를 포함하여) 32 비트로 이루어진다는 것이다. 이 때, 실제 명령어 순서와 구조 내 순서가 다를 수 있으니 조심하자.

![](/imgs/mips/mips1.png)

## I-Type
Immediate 파라미터를 포함하는 명령어 타입이다.

- op : opcode(operation code).
- rs : source가 되는 레지스터. 주소 연산 시 base가 된다.
- rt : target이 되는 레지스터. (연산 결과가 rt에 저장된다.)
- imm : immediate value.

## R-Type
레지스터만을 파라미터로 사용하는 명령어 타입이다.

- op : opcode.
- rs : 첫 번째 source가 되는 레지스터.
- rt : 타겟이자 두 번째 source가 되는 레지스터.
- rd : destination이 되는 레지스터. (연산 결과가 rd에 저장된다.)
- shamt : shift amount.
- funct : opcode의 확장, 더 많은 종류의 명령어를 사용하기 위함.

## J-Type
단일 상수 파라미터를 가지는 명령어 타입이다.

- op : opcode.
- address : target address.


필요한 명령어는 문서 찾아가면서 보자.

 

