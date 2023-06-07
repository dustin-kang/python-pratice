# HTML과 Box Model

## HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!-- 문서의 문자 인코딩 방식 -->
    <title>Document</title> <!-- 문서의 제목으로 탭에 표시됨.-->
</head>
<body>
Hello World 
</body>
</html>
```

[**TAG**](https://www.w3schools.com/tags/default.asp)

**List**

* `<ul>, <ol>`, `<li>`

**Div Span**

* `<div>` : html 태그를 그룹으로 나눌때 사용
* `<span>` : 인라인 블록을 바꿀 때 사용

**Attributes**

```html
<img src="" alt="source가 없는 경우 나타내는 텍스트">
<a href="" target="_blank"></a>
```

* src과 alt를 Attribute라고 합니다.
* src에 절대적인 링크나 상대적인 링크(HTTPS)를 설정할 수 있습니다.
* `target` 속성은 문서가 열릴 위치를 명시합니다. 탭으로 열거나 윈도우 전체를 오픈하거나를 의미합니다.

#### Form Table

* Table : `<table><thead><th></th></thead> <tbody><tr><td></td></tr></tbody> </table>`
* Form : 데이터를 서버로 보낼 때 모아서 보내주는 역할을 합니다. [`input`](https://www.w3schools.com/tags/tag\_input.asp)

```html
<form>
    <label for="username">Username:</label>
    <input type="text" name="username" value="기본값 or freeset" required placeholder="쓰기전에 기본값 보여짐"> <!-- required : 입력하지 않았을 때 입력하라는 규칙 생성 -->
    <button type="submit">SUBMIT</button> <!-- 서버로 보낼 때 submit 타입 -->
</form>

<!-- Query : /form.html?username=____&password=____ -->
```

## CSS

#### CSS Specify

```css
/* Here is CSS Comment */

h1 {
    color: red;
    text-decoration: underline;
    font-size: 50;
}

p {
    background-color: antiquewhite;
    border-style: dashed;
}

.inner { 
    /* div class= inner */
    background-color: orange;
    border-width: 5px;
    border-style: double;
}

.outer > p {
    /* div class=outer 안에 <p> 태그 */
    font-size: 30px;
}

#smaller {
    /* id = smaller */
    color:green;
}

p + h2 {
    /* <p> 바로 다음 <h2> (동등한 level) */
    color: blue;
}

ul li  a {
    /* ul < li < a */
    color : violet;
}

```

#### Font

```css
/* css 폴더 안에 font 다운  */
@font-face {
    font-family: 'Roboto-Black';
    src: url('Roboto/Roboto-Black.ttf') format('truetype'); /*Roboto 폴더안에 robot-Black.ttf import*/
}

p {
    font-family: 'Roboto-Black';
    font-size: 1em; /* em : 기존 폰트 사이즈에서 몇 배 크기를 의미. 즉, 2em 일 경우 10pt 였다면 20pt로 변경 */
}
```

#### Box Model

<figure><img src="https://user-images.githubusercontent.com/55238671/235436657-205dccac-afb3-4e5c-a3bf-b217434dc913.png" alt=""><figcaption></figcaption></figure>

* `width` `height` : margin과는 다르게 화면대비 크기를 의미함.

## BootStrap

## Refer

* [HTML - W3school](https://www.w3schools.com/html/)
* [CSS - Mozilla developer site](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [bootstrap v.5.0](https://getbootstrap.kr/docs/5.0/getting-started/introduction/)
