# URL과 View 설계하기

## 프로세스

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

## URLs

> 사이트의 위치를 파악하고 **`views`와 연결(routing)** 하는 역할을 합니다.

```python
from django.urls import include, path

urlpatterns = [
    path('index/', views.index, include('polls.urls')),
    path('bio/<username>', views.bio),
    path('bio/<slug:title>/', views.article, name='article-detail'),
    path('blog/', include('blog.urls')).
]
```

#### `path(route, view, kwargs=None, name=None)`

* **path\_coverters** : 장고에서 path 함수를 통해 route를 편하게 사용할 수 있는 문법입니다. `<slug:title>` 이외에도 다양한 종류가 있습니다.

#### `repeat(route, view, kwargs=None, name=None)`

* `'bio/<username>'` 대신에 정규 표현식을 사용할 수 있습니다. 끝에 `$`을 붙여줍니다.
* `r'^bio/(?P<username>\w+)/$'`

### 페이지 에러 Redirect

#### URL NOT FOUND (404)

장고는 라우팅 위치가 존재하지 않은 경우, 아래와 같은 방법으로 사용할 수 있습니다.

1. `urls.py`에서 `handler404` 변수를 사용합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235652772-4797d1fc-6c76-4077-9393-f8d669a56c59.png" alt=""><figcaption></figcaption></figure>

2. `settings.py`에서 두가지를 수정합니다.
   * DEBUG = False
   * ALLOWED\_HOSTS = \['\*'] : 어디서든지 장고 웹사이트를 접근할 수 있다는 의미입니다.
3. `HttpResponseNotFound`를 사용합니다.

#### Redirect

> 해당 URL을 다른 URL로 자동적으로 바꾸고 싶을 때 사용하는 함수입니다.

* `HttpResponseRedirect`를 사용합니다.
* [Http 상태코드](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)를 사용합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235665296-3aa58ced-9322-4fc1-a2de-5905dfac9fa5.png" alt=""><figcaption></figcaption></figure>

#### Reverse Url

* template에서 `name` 인자를 사용하면 하드코드한 값을 대입하는 대신 name을 통해 파싱이 가능합니다.

<figure><img src="https://user-images.githubusercontent.com/55238671/235664494-dd92cd76-4228-4cfb-867b-2291fb6f593b.png" alt=""><figcaption></figcaption></figure>

## Views

> 비지니스 로직이나 파이썬의 프로그래밍을 담습니다. Views에는 FBV와 CBV가 있습니다.

| - | FBVs                | CBVs                           |
| - | ------------------- | ------------------------------ |
|   | 정말 단순하게 시용할 때       | DRY 법칙 허용 (반복 코드 피함)           |
|   | 코드를 재사용하거나 확장하기 어려움 | Generic Views 제공 (패턴화된 방법을 사용) |
|   | 복잡한 뷰를 설계할 때 사용     | CRUD 작업이 단순하다.                 |

> CBV가 FBV를 대체하는 방법은 아닙니다.

### FBVs

```python
# 전체적인 느낌만 보세요.
def my_first_view(request):
    template_name = 'form.html' # 사용자에게 보여줄 템플릿을 리턴할 때
    form_class = MyForm

    form = form_class

    if request.method == 'POST': # 반복되는 코드가 발생할 수도 있음.
        form = form_class(request.POST)
        if form.is_vaild():
            form.save()
            return HttpResponseRedirect(reverse('list_view'))

        return render(request, template_name, {'form': form})
```

### CBVs

```python
# 전체적인 느낌만 보세요.
class MyFirstView(View):
    template_name = 'form_html'
    form_class = MyForm

    def get(self, request, *args, **kwargs): # 프로토콜이 Get인 경우
        form = self.form_class
        return render(request, template_name, {'form': form})
    
    def post(self, request, *args, **kwargs): # 프로토콜이 POST인 경우
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_view'))
        else:
            return render(request, self.template_name, {'form': form})
```

## Urls과 Views의 관계

<figure><img src="https://user-images.githubusercontent.com/55238671/235667656-b16c46c4-8ec6-4590-b54b-221432d9cf3b.png" alt=""><figcaption></figcaption></figure>

### 참고자료

* [path\_converters - 꿍꿍이의 개발일지](https://stg0123.github.io/study/25/)

\
\
