---
title:  "1 Source Files Format"
tags: MIPS
toc: true
---

# Intro
앞서 언급했듯, 여기선 MIPS64를 기반으로 한 EduMIPS64 시뮬레이터를 사용할 것이고, 참고 자료로 EduMIPS64 매뉴얼과 학교의 컴퓨터 구조 렉쳐 노트를 사용할 것이다. (혹시 몰라 렉쳐 노트는 참고만 하고, 캡쳐 등을 하지 않을 생각이다)

아무튼 이번엔 MIPS 소스 파일이 어떻게 구성되어 있는지 간단히 알아보도록 하자.


# Source Files Format
소스 파일은 크게 두 섹션(section)으로 나뉜다. `.data` 섹션과 `.code` 섹션이다. EduMIPS64에선 각 섹션에 메모리 제한을 두고, 그것이 하드코딩 되어 있다. `.data` 섹션은 640 kB, `.code` 섹션은 128 kB로 제한되어 있다.

## `.data` Section
`.data` 섹션은 프로그램 실행(execution) 전에 미리 채워져 있을 데이터들을 지정한다. 일반적인 형식은 아래와 같다.

    [Label:] .datatype value1 [, value2 [, ...]]
    
Bracket은 생략 가능한 부분이다. `Label`로 레이블링을 하여 이후에 쉽게 참조할 수 있고(레이블은 그것이 있는 주소에 대응된다(imm)), `.datatype`으로 데이터의 형식을 명시하며(e.g. `.byte`, `.word`, `asciiz`, etc.), `value`로 데이터의 값을 명시한다.

데이터 타입의 종류들을 알아보자.

Type | Directive | Description
---|---|---
Byte | `.byte` | 단일 바이트의 데이터 (8 bits)
Half word | `.word16` | 2 바이트의 데이터 (16 bits)
Word | `.word32` | 4 바이트의 데이터 (32 bits)
Double word | `.word` or `.word64` | 8 바이트의 데이터 (64 bits)
Free space | `.space` | 메모리 내의 free space, 일종의 placeholder다. (in byte)
ASCII | `.ascii` | ASCII char를 포함하는 string
ASCIIZ | `.asciiz` | Null-terminated string, null byte는 string 끝에 자동적으로 붙는다.

`.space`는 주소나 `syscall` 파라미터 등을 저장할 때 유용하다. 주소 등을 저장할 땐 보통 4 바이트를 할당해서 비워놓는다.

데이터 선언 시 주의해야 할 점이 있다. 어떤 데이터 리스트를 선언할 때, multiple directive를 사용하는지, single directive를 여러 번 사용하는지에 따라 결과가 달라질 수 있다. 예시를 확인해보자.

    .data
    .byte 1, 2, 3, 4
    .byte 1
    .byte 2
    .byte 3
    .byte 4

이렇게 데이터를 선언하면, [1, 2, 3, 4] 인 정수 배열이 똑같이 두 번 나열될 것 같지만, 실제론 아래와 같이 메모리가 할당된다.

    0:  0 0 0 0 4 3 2 1
    8:  0 0 0 0 0 0 0 1
    16: 0 0 0 0 0 0 0 2
    24: 0 0 0 0 0 0 0 3
    32: 0 0 0 0 0 0 0 4

이는 datatype identifier를 만날 경우 64-bit double word에서 시작하기 때문이다. 이를 잘못 이해하면 예상치 못한 결과가 나올 수 있으니 주의하자.

## `.code` Section
`.code` Section은 프로그램 실행 시작 후 사용될 인스트럭션들을 포함한다. 각 인스트럭션들의 일반적인 형식은 아래와 같다.

    [label:] instruction [parameter1 [, parameter2 [, parameter3]]]
    
모든 인스트럭션이 세 개를 초과한 파라미터를 갖지 않으며, 그 수는 인스트럭션의 종류에 의존한다. 그리고 파라미터는 크게 세 종류로 나누어 볼 수 있다.

- Register : 레지스터는 `$(num)`, 또는 `r(num)` (case-insensitive하다)로 나타낸다. 이 때 `num`은 0 부터 31 사이의 값이다. (e.g. `r4`, `R4`, `$4`)
- Immediate : 일종의 상수로, 숫자일 수도, 레이블일 수도 있다. Base 10과 16(`0x` prefix) 모두 가능하다.
- Memory : `Base(offset)`과 같은 방식으로 나타내어지는 주소에 대응된다. Base와 offset은 레지스터 값일 수도, 레이블일 수도, 상수일 수도 있다.

### Register
MIPS엔 32-bit 크기의 레지스터 32개가 있다. 0부터 31까지 넘버링되며, (속도가 빠르므로) 자주 접근되는 정수 데이터에 사용된다. 앞서 언급했듯 prefix `$`, `r`, `R`로 레지스터를 나타내며, 각각의 레지스터는 그것의 용도에 관한 관습 내지는 규칙이 있다.

Register | Alias | Purpose | Callee-Saved
---|---|---|---
0 | zero | 이 레지스터는 0을 저장하며, 바꿀 수 없다. | N/A
1 | at | Assembler temporary, 어셈블러에 의해 사용됨. | N
2-3 | v0-v1 | 서브루틴의 return value. | N
4-7 | a0-a3 | 서브루틴의 argument. | N
8-15, 24-25 | t0-t7, t8-t9 | Temporaries. | N
16-23 | s0-s7 | Callee-saved temporaries | Y
26-27 | k0-k7 | OS 커널에 의해 보존됨. | N/A
28 | gp | Global pointer, 메모리 내 전역 변수에 대한 포인터. | Y
29 | sp | Stack pointer. | Y
30 | fp | Frame pointer, 해당 프로시저의 스택 프레임에 대한 포인터. | Y
31 | ra | Return address, 리턴 주소를 저장함. | N/A

### Memory
메모리는 array나 structure 같이 composite한 데이터도 저장할 수 있다. 대신, 레지스터에 비해서 속도가 느리기 때문에 자주 접근되는 데이터라면 레지스터를 활용하는 게 좋고, 산술 연산(arithmetic operation)을 위해선 레지스터로 데이터를 가져온 다음, 연산 후 다시 저장하는 load/store의 과정이 필요하다.

메모리는 byte-addressed이므로 각각의 주소는 1 byte에 해당되고, word-aligned이므로 주소는 반드시 4의 배수여야 한다. 또한, MIPS는 big-endian 주소 방식이기 때문에, MSB가 가장 작은 address를 가진다.




