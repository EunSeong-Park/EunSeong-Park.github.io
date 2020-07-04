---
title: "OpenWhisk를 통한 FaaS 서버리스 컴퓨팅"
tags: OpenWhisk FaaS Serverless Cloud-Computing
toc: true
---

# Serverless Computing
서버리스 컴퓨팅(serverless computing)은 클라우드 컴퓨팅의 일종으로, __클라우드의 provider가 자원과 서버를 관리함으로써 개발자가 서버 및 자원 관리의 책임을 갖지 않도록 하는__ 모델이자 플랫폼이다. 즉, 단어 그대로 server-less한 것은 아니나, 개발자 측에는 서버의 존재가 은닉되어 있기 때문에 서버리스라고 부른다. 꽤 절묘한 네이밍이라고 느낀다.

또한, 서버리스 컴퓨팅 플랫폼은 미리 정해진 기간, 시간, 또는 용량이 아니라 __개발자가 사용한 자원을 바탕으로 요금을 부과한다.__ 기존 방식보다 fine-grained pricing을 가능케한다고 볼 수 있다. 그것의 사용이 간헐적이거나 짧은 시간 동안만 이루어진다면 이러한 서버리스 플랫폼이 조금 더 적합할 것이다.

서버리스 컴퓨팅은 크게 두 가지 종류로 나누어 볼 수 있다. 바로 BaaS(Backend-as-a-Service)와 FaaS(Function-as-a-Service)다.

- BaaS: 위치 서비스, 인증 및 암호화, DB 등 각종 서비스를 클라우드 플랫폼에서 API의 형태로 제공해주어, 개발자는 백엔드 영역의 디테일에 대한 부담을 줄일 수 있다.
- FaaS: 개발자에 의해 함수가 작성되어, 이는 특정 이벤트 발생 시 호출되는 event-driven한 방식이다. HTTP 요청, DB 갱신 등의 이벤트에 의해서도, 일정 주기에 따라서도 호출될 수 있다.

많은 대형 클라우드 provider들이 FaaS를 지원하는 플랫폼을 제공한다. AWS Lambda, MS의 Azure Function, Apache OpenWhisk 등이 그 예시다.


# Features of FaaS
간단하게 FaaS의 주요 특징을 살펴보자.

- __Stateless__ : 함수의 실행(execution) 사이의 상태가 보존되지 않으며, 또한 그렇게 설계되어야 한다.
- __Event-driven__ : 함수는 특정 이벤트에 의해 호출(invoked)된다. 또, 함수뿐 아니라 이벤트의 종류나 방식도 임의로 설정될 수 있다.
- __Short-lived function__ : 함수의 실행 시간은 상대적으로 짧다. 이는 종종 성능 저하의 요인이 되기도 한다.
- __Fine-grained pricing__ : 가격은 함수의 실행 시간과 그것의 호출 횟수, 또 자원 (특히 메모리) 사용량에 의존한다.

이러한 플랫폼은 개발자로 하여금 서비스의 유지 및 관리 비용을 획기적으로 줄이고, 그로 인해 메인 서비스에 더욱 집중적인 투자를 할 수 있도록 돕는다. 하지만 물론 단점도 있다.

우선, FaaS 플랫폼에 의한 추가적인 성능 저하가 발생한다. (Docker 등에 의한) 컨테이너리제이션, 혹은 추가적인 분리(isolation) 또는 가상화(virtualization)로 인한 각종 오버헤드가 발생할 수 있고, 짧은 함수와 무상태성은 서버 측의 지역성(locality)을 저하시키기에 충분하다. 이는 플랫폼뿐만 아니라, 플랫폼을 제공하는 아키텍처 및 시스템의 협업도 필수적이다. 

또, 개발자가 제공하려는 서비스가 어느 정도 클라우드 플랫폼에 종속적이게 되어, 해당 플랫폼의 정책적/기술적 변화에 대응해야 한다는 문제점도 있다.

하지만 그러한 문제점에도 불구하고 FaaS는 충분히 매력적이다. (직접 써보면 더더욱 그러함을 느낄 수 있다!) 이제, OpenWhisk를 중심으로 FaaS의 특징과 동작 방식을 간단히 알아보도록 하자.


# OpenWhisk
[IBM Cloud Function](https://cloud.ibm.com/functions/)은 오픈 소스인 [Apache Openwhisk](https://github.com/apache/openwhisk)를 기반으로 한 FaaS 플랫폼이다. 