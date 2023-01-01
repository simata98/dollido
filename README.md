# 빅프 markdown

---

# Dollido KT AIVLE Big Project

## 소개

> 기존 유실물 찾기 서비스의 불편함을 해소하고 개선하고자, 습득자는 유실물을 간편하게 등록하고 분실자는 간단한 인증을 통해 유실물을 찾아가고자 본 서비스를 고안하게 되었습니다.
> 

## 기존 사례 분석

![lost112.png](/markdown/lost112.png)

### 기존 서비스의 문제점

1. 회원가입, 로그인 유효성 검사 기능의 부재
2. 경찰서 마다 카테고리별 지칭명이 서로 달라 찾는데 어려움
3. 잃어버린 물건을 찾으러 경찰서에 방문 필수
4. 게시물마다 일부 정보의 부재(사진, 물품명, 보관장소 등)
5. 웹과 앱의 연동 부재
6. 경찰관들이 분실물을 수동으로 정보를 기입해야하는 문제

### 이번 프로젝트에서 개선할 점

1. 회원가입, 로그인 기능 강화 및 보안성 강화
2. 습득물건을 사용자가 자발적으로 신고 후 직접 찾을 수 있도록 기능 개선
3. 분류된 결과를 자동으로 기입하여 편의성 개선
4. 웹과 앱의 연동

## 프론트엔드(FrontEnd)

### 회원가입 및 로그인

![Untitled](/markdown/Untitled.png)

개인 정보 제공 동의 후 회원가입이 가능하며,  모든 동의를 받으면 회원가입 페이지로 진입할 수 있습니다.

[React App - Chrome 2023-01-01 20-33-20.mp4](/markdown/React_App_-_Chrome_2023-01-01_20-33-20.mp4)

회원가입 진행시 유효성 검사를 실시간으로 진행하며, 모든 유효성 검사를 충족시 회원가입을 진행합니다.

![Untitled](/markdown/Untitled%201.png)

데이터베이스에 저장되어 있는 계정이 유효한 계정일 때 메인페이지로 이동합니다.

### 메인페이지

[제작중]

### 경찰청 분실물 조지

![Untitled](/markdown/Untitled%202.png)

경찰청 분실물 API([https://www.data.go.kr/data/15000799/openapi.do?recommendDataYn=Y](https://www.data.go.kr/data/15000799/openapi.do?recommendDataYn=Y))를 사용하여 Dollido 서비스에 등록되지 않은 물건들의 정보도 확인할 수 있는 페이지입니다.

### 돌리도(Dollido) 분실물 조회 페이지
