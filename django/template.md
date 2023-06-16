# Template 설계하기

## Django Template

장고의 Template은 MVC 패턴에서 View와 유사한 역할을 합니다.

View로 부터 전달된 데이터를 Template에 전달받아 _Dynamic_ 한 웹페이지를 보여주게 되는 것입니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235857738-9057482c-b779-4b68-9edf-0fdcc351a489.png" alt=""><figcaption></figcaption></figure>

장고의 template은 `jinja2`와 유사한 형태의 문서 작업입니다.

#### 준비 작업

1. `settings.INSTALL_APPS` 변수에 앱이 등록되어 있는지 확인했나요?

```
- INSTALL_APPS안에 'app이름.apps.Config클래스' 를 작성해주세요.

- TEMLATES 딕셔너리 안에 APP_DIRS가 True인지 확인해주세요.
```

2. template 디렉토리를 생성했나요?
3. 템플릿 파일을 전달하기 위해 views.py에 `render` 함수를 임포트 했나요?

#### `render(request, template_name, context=None)`

주어진 template과 Context\_dictionary을 결합하고 `HttpResponse` 객체를 통해 템플릿에게 전달합니다.

```python
from django.shortcuts import render
 
def index(request):
  msg = 'My Message'
    return render(request, 'index.html', {'message': msg})
```

* **template\_name** : `project/templates/`을 기준으로 템플릿 파일을 가리킵니다.
* **context** : View에서 템플릿에 전달할 데이터를 Dictionary 형태로 전달합니다. `{'템플릿에 사용할 변수':전달하는 데이터의 내용}`

[👉 render 함수](https://docs.djangoproject.com/ko/4.2/topics/http/shortcuts/#render)

### 템플릿 구조

템플릿 구조를 설계하는 방법에는 두가지 방법이 존재합니다. 두가지 방법은 어떻게 사용하느냐에 따라 가치가 달라집니다.

#### 루트 디렉토리 내 템플릿

```
DJANGO_ROOT/templates/<APP_NAME>/<TEMPLATES_FILE>
```

* 큰 프로젝트인 경우 이 디렉토리만 CDN으로 옮길 수 있기 때문에 편하다는 장점이 있습니다.

#### 앱 내 템플릿

```
<APP_NAME>/templates/<APP_NAME>/<TEMPLATES_FILE>
```

* 개인적으로 앱을 패키징할 때 좋습니다. (다른 프로젝트에 재사용할 때 편합니다.)

> 📌 Django 개발 가이드라인은 앱 내 템플릿을 작성하는 것을 추천합니다. 이유는 복수의 App들이 동일한 이름의 템플릿을 가진 경우, 잘못된 템플릿을 가져올 수 있기 때문입니다.

### 템플릿 명령어

views에서 렌더한 context들을 템플릿에 사용하거나 템플릿 자체의 명령어를 적용할 수 있습니다.

<table data-full-width="true"><thead><tr><th width="117">name</th><th>mean</th><th>command</th><th></th></tr></thead><tbody><tr><td><strong>variables</strong></td><td>context로 작성한 변수를 키로 사용하여 값을 반환합니다. <code>_</code>나 <code>.</code>를 통해 접근할 수 있습니다.</td><td><code>{{ music.artist }}</code></td><td></td></tr><tr><td><strong>filters</strong></td><td>변수에 필터를 씌어 수정합니다.</td><td><code>{{ index.message|upper }}</code></td><td>lower, length, date, escape 등이 있습니다. <a href="https://docs.djangoproject.com/ko/4.2/ref/templates/builtins/#built-in-filter-reference">참고자료</a></td></tr><tr><td><strong>tags</strong></td><td>템플릿의 로직을 제어합니다.</td><td><code>{% 명령어 %}</code></td><td><code>for...in...endfor</code>, <code>if...elif...else...endif</code>, <code>and</code> <code>or</code>, <code>in</code> <code>is</code>, <code>>&#x3C;=</code> <code>blockextends</code></td></tr><tr><td><strong>comments</strong></td><td>주석을 작성합니다.</td><td><code>{# 주석 #}</code></td><td></td></tr></tbody></table>

> 📌 Django 플러그인을 사용하면 편하게 템플릿 작업하실 수 있습니다.

#### 템플릿 상속

* block : 자식 템플릿에 의해 재정의 될 수 있는 블록을 정의하는 것
* extends : 부모 템플릿을 가져올 수 있다는 명령어

<figure><img src="https://user-images.githubusercontent.com/55238671/235877212-69430d8d-cdfa-46fa-bd0b-2d19c09ee960.png" alt=""><figcaption></figcaption></figure>

```renpy
{% raw %}
{% extends 'base.html' %}
{% block content %}
#...
{% endblock %}
{% endraw %}
```

### 템플릿 URL

[path함수의 `name`](https://github.com/dustin-kang/Programming-Team-Notes/wiki/urls\_views#pathroute-view-kwargsnone-namenone)부분을 URL로 사용할 수 있습니다.  **템플릿에 앵커(`<a href>`)를 달아 페이지 간 연결을 할 수 있습니다.**

사용하는 방법에는 두가지가 있습니다.

![image](https://user-images.githubusercontent.com/55238671/235876911-3d22ff89-782e-415a-ad95-58bc871ac071.png)

**Positional**

```python
{% raw %}
{% url 'URL_NAME' 값 %}
{% endraw %}
```

**keyword**

```python
{% raw %}
{% url 'URL_NAME' 인자1=값, 인자2=값2 %}
{% endraw %}
```

> 📌 두가지를 섞어서 사용할 수 없습니다.

```python
import os
'DIRS': [os.path.join(BASE_DIR, 'templates')]

# settings.py에 위와 같이 설정을 해주면 루트 디렉토리의 템플릿도 들여다 볼 수 있게 됩니다.
```

### 에러 페이지

에러 페이지를 만드는 두가지 방법입니다.

[사전 준비](https://github.com/dustin-kang/Programming-Team-Notes/wiki/urls\_views#url-not-found-404)

1. `404.html` 파일을 만들어줍니다.

```python
# urls
handler404 = 'project.views.error_404_view'
# views에서 템플릿을 전달하기 때문에 context가 필요한 경우에만 urls를 작성해도 됩니다.
```

2. `hander404` 함수를 사용해서 render 합니다.

```python
# views
def error_404_view(request, exception):
    return render(request, '404.html')
```

> 📌 500 Error를 발생하고자 할때 views 내 함수를 `pass` 시키면 됩니다.

### Static file

정적인 파일을 말합니다. (파싱을 하지 않고 그대로 보내는 파일을 말합니다.)

#### 사전 준비

1. INSTALLED\_APPS 내 `django.contrib.staticfiles`를 등록합니다.
2. `static` 디렉토리를 만들어줍니다.

* **STATIC\_URL** : Static 파일을 저장하는 곳
* **STATIC\_ROOT** : Static 파일을 한꺼번에 모아 한 곳으로 뭉쳐주는 역할을 합니다.
* **STATICFILES\_DIR** : static\_url 위치 말고도 다른 위치에 있는 static 파일들을 읽을 수 있게 도와줍니다.
* **MEDIA\_ROOT** : 프로젝트 파일을 업로드할 때 파일이 저장되는 곳을 말합니다.

```python
# Settings.py
# STATIC_URL = 'static/'
STATIC_ROOT = '' # 루트 디렉터리
STATIC_URL = '/static/' # 루트/static/
STATICFILES_DIRS = ('static',) # 추가적인 Static 파일 위치
```

```python
{% raw %}
{% extends 'base.html' %}
{% load static %} 

{% block content %}
    <img src="{% static 'project/django.png' %}" alt="Django image" />
{% endblock content %}
{% endraw %}
<!-- 위치는 STATIC_URL 기준입니다.  -->
```

> 📌 프로젝트 파일이 개발자 모드에서 이미지를 읽을 수 있게 `DEBUG=True`로 설정해주세요.

[👉 정적 파일 관리하기](https://docs.djangoproject.com/ko/4.2/howto/static-files/)
