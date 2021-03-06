---
title: "OpenWhisk를 통한 FaaS 서버리스 컴퓨팅"
tags: OpenWhisk FaaS Serverless Cloud-Computing
toc: true
---

# Serverless Computing
서버리스 컴퓨팅(serverless computing)은 클라우드 컴퓨팅의 일종으로, __클라우드의 provider가 자원과 서버를 관리함으로써 개발자가 서버 및 자원 관리의 책임을 갖지 않도록 하는__ 모델이자 플랫폼이다. 즉, 단어 그대로 server-less한 것은 아니나, 개발자 측에는 서버의 존재가 은닉되어 있기 때문에 서버리스라고 부른다. 꽤 절묘한 네이밍이라고 느낀다.

또한, 서버리스 컴퓨팅 플랫폼은 미리 정해진 기간, 시간, 또는 용량이 아니라 __개발자가 사용한 자원을 바탕으로 요금을 부과한다.__  기존 방식보다 fine-grained pricing을 가능케한다고 볼 수 있다. 그것의 사용이 간헐적이거나 짧은 시간 동안만 이루어진다면 이러한 서버리스 플랫폼이 조금 더 적합할 것이다.

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
[IBM Cloud Function](https://cloud.ibm.com/functions/)은 오픈 소스인 [Apache Openwhisk](https://github.com/apache/openwhisk)를 기반으로 한 FaaS 플랫폼이다. 가입하면 부분 무료로 사용할 수 있다. 비용이 상당한 함수를 반복적/주기적으로 호출하지 않는 이상 무료로 봐도 무방하다.

![](/imgs/lab/faas1.png)

위와 같이 CLI를 사용할 수도 있지만, 웹 브라우저에서도 직접 함수를 포함한 액션(action)을 작성하고, 트리거를 설정하고 호출하는 일련의 과정을 모두 할 수 있다. 여기서는 웹 브라우저에서 OpenWhisk를 사용해보자.

FaaS와 OpenWhisk에 대한 설명과 사용법은 [여기](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-getting-started)에 굉장히 잘 설명되어 있다. 그래서 기본적인 부분만 짚어보며 OpenWhisk를 사용해볼 것이다.

## Action
__액션(action)은 실행되는 함수들을 포함하는 작은 코드 단위다.__ IBM Cloud Function에서는 JS, Ruby, Python, Go 등 다양한 언어를 지원하고, 각 액션에 대한 메모리/시간 제한 등을 설정할 수 있다. 액션은 코드로 제공될 수도, Docker image로 제공될 수도 있다. Docker image같은 경우엔 CLI를 사용하자.

![](/imgs/lab/faas2.png)

웹에서는 액션 탭에서 액션을 작성 및 관리할 수 있다. <u>Create</u>에서 액션을 작성해보자. 간결한 형태의 에디터가 제공되므로, 간단한 함수라면 직접 웹에서 코딩할 수 있다.

![](/imgs/lab/faas3.png)

주석에 나와있듯이, 함수의 매개변수(parameter)와 리턴(return)값은 JSON 형태여야 한다. 또, 파라미터를 임의로 주어 실행할 수 있다. 여기서는 별도의 파라미터 없이 위의 코드를 그대로 사용한다.

![](/imgs/lab/faas4.png)

와! 새로운 액션이 생겼다. 앞서 언급했듯 메모리와 시간 제한을 설정할 수 있으니 필요하다면 한 번 시도해보자.

## Event
__이벤트(event)는 단어 그대로 내/외부에서 발생한 어떠한 사건이다.__ 어떤 데이터베이스의 레코드 변경이 될 수도, Github에서의 새로운 커밋, 또는 HTTP 요청 등이 될 수도 있고, 단순한 주기적인 클러킹이 될 수도 있다. 

__트리거(trigger)는 자신과 연관된 특정한 이벤트에 반응하여 실행되고__, __룰(rule)은 트리거의 실행을 기반으로 액션을 호출한다.__ 우리는 적절한 룰과 트리거의 구성을 통해 다채롭고 효과적인 event-driven한 서버리스를 경험할 수 있다. 웹에서는 이 요소들이 약간 모호하지만, CLI를 쓰면 명확히 구분될 수 있고, 동시에 잘 구분되어야 한다.

## Example: hello, world!
가장 간단한 예시로, 1분에 한 번씩 hello-world하는 기능을 구현해보자. 트리거 탭에서 "Periodic"을 선택한다.

![](/imgs/lab/faas5.png)

호출되는 시간은 패턴, 혹은 cron expression으로 표현될 수 있는데 조금 더 직관적인 패턴을 사용한다. 이렇게 작성함으로써 월요일 중, 매시간, 매분마다 `{name:world}` 형태의 JSON을 파라미터로 함수를 호출시킬 것이다. 

![](/imgs/lab/faas6.png)

그리고 위와 같이 액션을 작성하고, 다시 트리거로 돌아가 해당 액션을 연관시키자.

![](/imgs/lab/faas7.png)

이제 조금 기다렸다가 "모니터" 탭에서 함수가 어떻게 실행되었는지 살펴본다.

![](/imgs/lab/faas9.png)

오!

## Background
OpenWhisk 내부에서는 다음과 같은 과정을 거쳐 우리에게 서비스를 제공한다. 공식 문서에 자세히 나와있으므로 간단하게만 살펴본다.

![](/imgs/lab/faas8.png)

HTTP request의 형태로 주어진 명령은 NGINX에서 리버스 프록싱(reverse proxing)되고 SSL 처리가 이루어진 뒤 컨트롤러(controller)로 전달된다. 

전달받은 요청을 기반으로, 컨트롤러는 이후에 수행할 동작을 결정하고 이후의 호출 과정까지 계속 어느정도 연관된다. 

Document-oriented database인 CouchDB에서 사용자 인증 및 권한 작업을 수행하고, 정상적으로 절차가 이루어졌다면 액션을 로드한다. 

Consul은 로드 밸런싱(load balancing)을 수행하며 사용 가능한 인보커(invoker)를 탐색하고 선택한다. 이후 Kafka는 각각의 호출에 대해 활성화 ID(activation ID)를 부여하고, 메모리 등의 리소스를 고려하며 액션과 파라미터를 포함하는 메세지를 컨트롤러로부터 받아 인보커에게 전달한다.

인보커(invoker)는 Docker 컨테이너에 코드를 삽입하고 파라미터를 입력하는 방식으로 함수를 실행한다. (최적화를 생각하지 않는다면) 함수 리턴 후 컨테이너는 삭제되고, 그것의 활성화 ID, 종료 상태 코드, 리턴값 등은 CouchDB에 저장된다.

이후 그 레코드에서 REST API를 통해 그 결과를 가져올 수 있다.


