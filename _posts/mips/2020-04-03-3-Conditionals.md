---
title:  "3 Conditionals"
tags: MIPS
toc: true
---

# Intro
조건부 명령 수행은 프로그램에서 빠질 수 없는 요소다. MIPS에선 어떻게 조건부 개념이 적용될까?


# Branch / Jump Instruction
물론, 레퍼런스를 찾아보면 더 다양하고 자세한 설명이 있지만, (내가) 자주 쓰는 명령어를 중심으로 설명을 해본다.

Instruction | Description
---|---
`b offset` | 무조건적(unconditional) 분기.
`beq rs, rt, offset` | rs == rt면 분기한다.
`bne rs, rt, offset` | rs != rt면 분기한다.
`beqz rs, offset` | rs == 0이면 분기한다.
`bgtz rs, offset` | rs > 0이면 분기한다.
`j target` | 무조건적 점프.
`jal target` | 다음 명령어 주소를 `ra`(31번)에 넣고 `target`으로 점프.
`jr ra` | `ra`에 해당하는 주소를 PC에 대입한다. (리턴)

`b`와 `j`를 보면, 둘이 같은 명령어같다는 느낌을 받는다. 하지만 몇 가지 차이가 있는데, 우선 `b`는 I-type 명령어, `j`는 J-type 명령어기 때문에, `b`는 주소가 들어갈 수 있는 비트가 적어 가능한 주소 범위가 `j`보다 좁다.

또한, `b`는 PC-relative 방식, `j`는 절대 주소 방식을 이용한다는 점에도 차이가 있다. 전자의 경우, target address를 PC + offset x 4로 지정하여 분기한다. 이 때, PC는 이미 다음 명령어의 주소를 가리키고 있음을 기억하자. 후자의 경우, PC를 target x 4로 설정하여 점프한다.

예를 들어, `100`에서 `120`으로 이동하는 상황을 생각해보자.

- Branch : PC는 현재 `104`이므로 `4`만큼 offset을 주어 104 + 4x4 = `120`
- Jump : target을 `30`으로 설정해 30x4 = `120`

추가로, branch의 주소 부분 비트가 타겟에 비해 너무 적다면, 어셈블러는 이를 적절히 jump로 변환한다.

# Set Instruction
조건에 따라 값을 세팅하는 명령어도 있다.

Instruction | Description
---|---
`slt rd, rs, rt` | rs < rt면 rd를 1로, 아니면 0으로 세팅한다. (set less than)
`slti rd, rs, imm` | rs < imm면 rd를 1로, 아니면 0으로 세팅한다.

이 명령어는 꽤 유용한데, `slt` 등에 의해 세팅된 레지스터 값으로 `bne` 등의 분기를 이용해 실제론 없는 `blt`(branch if less than)과 같은 기능을 구현할 수 있기 때문이다.

그렇다면 왜 `blt`같은 명렁어는 없는가? 하면, 이는 MIPS가 그러한 간결함을 추구하기 때문이다. 분기와 비교를 합친 명령어는 체계를 복잡하게 하고, 이는 다른 명령어로도 충분히 구현할 수 있다. 


# Implementation
이제 위 명령어들을 바탕으로, 일반적인 고급 언어에서 사용하는 것들을 구현해보자.

## Conditional Expression

    abs = (a>b) ? a-b : b-a;
    
C에서 쓰이는 조건 연산자(conditional expression)다. 이를 MIPS 코드로 구현해보자.

Var | Reg
--- | ---
abs | s0
a | s1
b | s2

              ;; set if a<b
              slt   $t0, $s1, $s2
              bne   $t0, Greater
              
              ;; if a<b then abs = b-a 
              sub   $s0, $s2, $s1
              j     Exit
              
              ;; if a>b then abs = a-b
    Greater:  sub   $s0, $s1, $s2
    Exit:     ...
    
여기서 분기나 점프 대상을 레이블로 지정하면, 어셈블러가 주소를 계산하여 점프한다. 

## Loop
While 루프는 그 구현 방법이 명확해 보인다. 시작점과 루프 탈출 지점을 레이블링 해놓고, 루프 끝 직전에 조건을 검사해, 조건이 참이라면 루프 시작점 레이블로 돌아가면 된다. 또는, 조건이 거짓이면 루프 밖으로 나가고, 참이면 처음으로 무조건 점프하는 방법도 있다.

    while (arr[i] == k) i += 1;
 
무슨 목적의 코드인지는 모르겠지만, 이를 MIPS 코드로 옮겨보자.
 
Var | Reg
---|---
i | s3
k | s5
address of arr | s6

                ;; shift left logical
                ;; branch에서 i*4를 base에 더해야 하므로 i << 2
    Loop: sll   $t1, $s3, 2
                ;; base(arr) + i*4 => arr[i]
          add   $t1, $t1, $s6
                ;; arr[i]의 값을 t0에 로드.
          lw    $t0, 0($t1)
          bne   $t0, $s5, Exit
          addi  $s3, $s3, 1
          j     Loop
    Exit: ...
    
For 루프는 따로 구현하지 않을 예정이다. 어차피 카운터 변수만 하나 놓고 마지막에 비교하면 끝이니..

    
# 마치며
다음은 프로시저 호출에 대해 알아보자. 그러면서 스택, 힙에 대한 내용 조금과, 재귀까지 구현해보려 한다.
