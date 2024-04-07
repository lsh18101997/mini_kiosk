# mini_kiosk

## 2024.04.03

장고 프로젝트 생성(모델링 고민중)

## 2024.04.04

모델링 완료

## 2024.04.05

메뉴 페이지 및 상세 페이지 생성과 두 페이지간 연결 완료

## 2024.04.07

메뉴 페이지 및 상세 페이지 HTML, CSS 작업 완료

상세 페이지에서 주문하기 버튼을 클릭하면 주문 완료 알림과 함께 

DB의 해당 메뉴의 invertory 필드의 값이 감소하도록 설계함

## 이슈

값이 감소하도록 설계할 때, POST를 사용하여 구현하고자 하였으나, 

MultikeysError가 반복적으로 발생함. 시간 내에 해결 실패하여 save()와 연산자로만 구현 완료함

![MenuList Image](C:/Users/PC2301/Desktop/%EB%AF%B8%EB%8B%88%ED%82%A4%EC%98%A4%EC%8A%A4%ED%81%AC1.JPG "메뉴 리스트")
![Order Image](C:/Users/PC2301/Desktop/%EB%AF%B8%EB%8B%88%ED%82%A4%EC%98%A4%EC%8A%A4%ED%81%AC2.JPG "주문 화면")
