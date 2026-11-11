# 라우팅
라우팅은 클라이언트가 서버로 보내는 HTTP 요청을 처리하는 프로세스이다. 
HTTP 요청이 지정한 라우트로 전송되면 미리 정의된 로직이 해당 요청을 처리해 반환한다. 


# APIRouter 클래스 
APIRouter 클래스는 다중 라우팅을 위한 경로 처리 클래스이며 fastapi 패지키에 포함되어 있다. 
APIRouter를 통해 애플리케이션 라우팅과 로직을 독립적으로 구성하고 모듈화할 수 있다. 
```python
from fastapi import APIRouter

router = APIRouter()
@router.get("/hello")
async def say_hello() -> dict:
  return {
    "message": "Hello!"
  }
```

**include_router()**
```
include_router(router1, router2, ...) 메서드는 APIRouter 클래스로 정의한 라우트를 메인 애플리케이션의 인스턴스로 추가한다. 이렇게 하면 라우트를 전체 애플리케이션에서 사용할 수 있다. 
```


# pydantic 모델
FastAPI에서는 정의된 데이터만 전송되도록 요청 바디를 검증할 수 있다. 요청 데이터가 적절한지 확인하고 악의적인 공격의 위험을 줄여주므로 매우 중요한 기능이다. 
**모델**은 데이터가 어떻게 전달되고 처리돼야 하는지를 정의하는 구조화된 클래스이다. 

**pydantic**
```
pydantic은 파이썬의 타입 어노테이션을 사용해 데이터를 검증하는 파이썬 라이브러리다. 
```

```python
from pydantic import BaseModel

class PackBook(BaseModel):
  id: int
  Name: str
  Publishers: str
  Isbn: str
```
다음과 같이 각각의 필들에 대한 자료형을 정의할 수 있다. 


# 경로 매개변수와 쿼리 매개변수
## 경로 매개변수
경로 매개변수는 리소스를 식별하기 위해 API 라우팅에 사용된다. 이 매개변수는 식별자 역할을 하며 웹 애플리케이션이 추가 처리를 할 수 있도록 연결 고리가 되기도 한다. 
```python
@router.get("/hello/{hello_id}")
```
여기서 {hello_id}가 경로 매개변수이다. 

## 쿼리 매개변수
쿼리 매개변수는 선택 사항이며 보통 URL에서 ? 뒤에 온다. 제공된 쿼리를 기반으로 특정한 값을 반환하거나 요청을 필터링할 때 사용된다. 
```python
async query_route(query: str = Query(None):
  return query
```


# 요청 바디
요청 바디는 POST와 UPDATE 등 라우팅 메서드를 사용해 API로 전달되는 데이터이다. 
```
POST 메서드는 새로운 데이터를 서버에 추가할 때 사용되고, UPDATE 메서드는 서버상에 있는 기존 데이터를 변경할 때 사용된다.
```


# FastAPI 자동 문서화
## 스웨거
스웨거는 인터랙티브 문서를 제공하여 API를 테스트 할 수 있도록 도와준다. 애플리케이션 주소 끝에 /docs를 붙이면 된다. 
```
http://127.0.0.1:8000/docs
```

## ReDoc
ReDoc 문선느 모델, 라우트, API에 관한 정보를 더 직관적이고 상세하게 전달한다. 애플리케이션 주소 끝에 /redoc를 붙이면 된다. 
```
http://127.0.0.1:8000/redoc
```
