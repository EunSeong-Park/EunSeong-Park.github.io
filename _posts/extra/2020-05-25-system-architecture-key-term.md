---
title:  "Computer System & Architecture Key Terms"
toc: true
tags: CS:APP Computer-Architecture
---

# Intro
컴퓨터 시스템과 구조 전반에 대해 얕게, 그리고 간단하게 정리했다.

# Key Terms
## Endianness

- Big endian: LSB가 큰 주소를 가진다.
- Little endian: LSB가 작은 주소를 가진다.

## Optimization
### Optimization by Compiler
Conservative한 최적화만을 진행하며, 보통은 프로시저 단위 내에서 분석 하는 게 일반적임. 

#### Optimization Blocker

- 비효율적인 프로시저 호출은 side-effect를 우려하여 최적화를 잘 하지 못한다.
- 비효율적인 포인터 연산에서 memory aliasing에 대한 우려가 있을 경우, 최적화를 잘 하지 못한다.

### Parallelism
#### Superscalar Processor
복수의 명령어를 비순차적 파이프라이닝으로 처리하는 프로세서.

#### Data Dependance
데이터 의존성은 병렬성을 떨어뜨린다.

- Flow dependance: 어떤 명령어가 앞의 명령어의 결과를 필요로 하는 경우.
- Antidependence: 어떤 명령어의 순서를 바꿀 수 없는 경우.
- Output Dependence: 동일한 장소에 적재하는 명령어들의 순서를 바꾸거나 병렬적으로 실행할 수 없는 경우

## Memory Hierarchy
용량 대비 비쌀 수록 빠르다.

### Locality

- 시간적 지역성: 최근 참조된 메모리 위치는 가까운 미래에 다시 참조될 가능성이 높다.
- 공간적 지역성: 최근 참조된 메모리 위치의 근처 메모리도 가까운 미래에 참조될 가능성이 높다.

### Cache
