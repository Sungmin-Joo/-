# 나만의 파파고
> 파파고 오픈 api를 활용한 나만의 파파고 만들기


파이썬과 파파고 apen api를 활용하여 프로젝트를 진행하였다.  
target text와 result text를 전환하는 기능, 'Enter'키 바인딩 등 최대한 많이 구현 해 보았다.


## 개발 환경

* Python:  
  - Python  3.7.4  
    
* OS:  
  - Window 10 Edu 64bit  
    
* Used Modules:  
  - tkinter(Python)  
  - NAVER PAPAGO open api
  
  
## 사용 예제

 자신이 발급받은 api를 코드의 'X-Naver-Client-Id' 와 'X-Naver-Client-Secret'에 기입한다.  
 ```python
header = {
    'X-Naver-Client-Id' : 'ENTER YOUR ID',
    'X-Naver-Client-Secret' : 'ENTER YOUR SECRET'
}
```

## 개발 환경 설정

 ### Python 설치  
 #### Python 설치는 공식 [홈페이지](https://www.python.org/) 에서 설치할 수 있다.
  
 ### PAPAGO api clinet ID 발급
 #### [네이버 개발자 센터]( https://developers.naver.com/)에서 발급받을 수 있다.  
 #### 자세한 방법은 [NAVER open api guide](https://github.com/naver/naver-openapi-guide/tree/master/ko/papago-apis)를 참고
 


## 정보

 주성민(Joo Sung Min) – big-joo_dev@naver.com  
 버그가 있다면 제보를 부탁 드립니다.  
   
  BSD 3-Clause License 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.

 [LICENSE](https://github.com/Sungmin-Joo/TERA_macro/blob/master/LICENSE)
 
 *(오픈소스 라이센스 관련 지식이 부족하여 모듈에 적용되는 라이센스들이 호환되도록 유지함)
