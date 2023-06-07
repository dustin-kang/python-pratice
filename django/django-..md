# Django를 소개합니다.

## Django

### Django의 이점

1. 오픈소스의 Python 웹 프레임워크
2. 로그인 기능 _Authentication, Administration_
3. 꽤 높은 보안성
4. ORM을 사용한 DB 관리 시스템 _DB integration_
5. **Scalable** : 트래픽이 많아도 Handling이 가능한 프레임워크 _Youtube, Instagram, Spotify_

> **📌** [**ORM**](https://hanamon.kr/orm%EC%9D%B4%EB%9E%80-nodejs-lib-sequelize-%EC%86%8C%EA%B0%9C/) **: 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 도구로 MVC 패턴을 기술하는 도구이다.**

### Django의 단점

1. Learning Curve : 웹 개발 경험이 없는 개발자에게는 친숙하지 않다.
2. Heavy Loaded : 너무 많은 모듈이 있어 느린감이 있습니다. + 파이썬 개발

### 특징

* MVT 아키텍처 패턴
* URL Routing
* ORM
* 데이터베이스 스키마 마이그레이션이 내장되어 있습니다.
* DB : PostgreSQL, MySQL, Sqlite, Oracle
* Authentication : 서드파티 로그인 기능을 사용할 수 있습니다.
* [엄청난 패키지](https://djangopackages.org)를 제공

### MVT Pattern

<figure><img src="https://user-images.githubusercontent.com/55238671/235442028-d3bb5a14-acf4-4109-9077-fbdc5fc37acf.png" alt=""><figcaption></figcaption></figure>

## Installation & Start

<figure><img src="https://user-images.githubusercontent.com/55238671/235445460-4435a290-057a-408e-afbf-bf6586d2c076.png" alt=""><figcaption></figcaption></figure>

```python
# installation
python -m pip install Django
pip3 install Django

# start Project
django-admin startproject <project>

# start web server(default port 8000)
python manage.py runserver
# python manage.py runserver <port>
```

```python
# start app
python manage.py startapp <app_name>
```

## Reference

* [Django Pros and Cons - Sambhav Sethi](https://www.linkedin.com/pulse/pros-cons-django-framework-development-sambhav-sethi/?trk=pulse-article\_more-articles\_related-content-card)
* [Django Life Cycle](https://goutomroy.medium.com/request-and-response-cycle-in-django-338518096640)
