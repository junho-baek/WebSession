# Frontend

## 웹페이지 분석하기

### 1. 개발자 도구 사용법

- F12 또는 우클릭 > 검사 클릭
- Elements 탭: HTML/CSS 구조 확인
- Network 탭: API 요청/응답 모니터링
- Console 탭: JavaScript 결과 확인

### 2. HTML 구조 분석

기본 태그 설명

1. 문서 구조 태그

```html
<!DOCTYPE html>
<!-- HTML5 문서 선언 -->
<html>
  <!-- HTML 문서의 루트 요소 -->
  <head>
    <!-- 문서의 메타데이터 -->
    <body>
      <!-- 문서의 실제 내용 -->
    </body>
  </head>
</html>
```

2. 텍스트 관련 태그

```html
<!-- 제목 태그 -->
<h1>가장 큰 제목</h1>
<h2>두 번째 제목</h2>
<h3>세 번째 제목</h3>
<h4>네 번째 제목</h4>
<h5>다섯 번째 제목</h5>
<h6>가장 작은 제목</h6>

<!-- 텍스트 서식 -->
<p>문단을 나타내는 태그</p>
<br />
<!-- 줄바꿈 -->
<hr />
<!-- 수평선 -->
<strong>굵은 글씨</strong>
<em>기울임 글씨</em>
<mark>하이라이트</mark>
<del>삭제된 텍스트</del>
<span>인라인 텍스트</span>
```

3. 목록 태그

```html
<!-- 순서 있는 목록 -->
<ol>
  <li>첫 번째 항목</li>
  <li>두 번째 항목</li>
  <li>세 번째 항목</li>
</ol>

<!-- 순서 없는 목록 -->
<ul>
  <li>항목 1</li>
  <li>항목 2</li>
  <li>항목 3</li>
</ul>

<!-- 정의 목록 -->
<dl>
  <dt>용어</dt>
  <dd>용어에 대한 설명</dd>
</dl>
```

4. 링크와 미디어 태그

```html
<!-- 링크 -->
<a href="https://example.com">외부 링크</a>
<a href="#section">내부 링크</a>

<!-- 이미지 -->
<img src="image.jpg" alt="이미지 설명" />

<!-- 비디오 -->
<video width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4" />
</video>

<!-- 오디오 -->
<audio controls>
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

5. 폼 관련 태그

```html
<form action="/submit" method="post">
  <!-- 텍스트 입력 -->
  <input type="text" name="username" placeholder="사용자명" />

  <!-- 비밀번호 입력 -->
  <input type="password" name="password" placeholder="비밀번호" />

  <!-- 라디오 버튼 -->
  <input type="radio" name="gender" value="male" /> 남성
  <input type="radio" name="gender" value="female" /> 여성

  <!-- 체크박스 -->
  <input type="checkbox" name="hobby" value="reading" /> 독서
  <input type="checkbox" name="hobby" value="gaming" /> 게임

  <!-- 선택 상자 -->
  <select name="country">
    <option value="kr">한국</option>
    <option value="jp">일본</option>
    <option value="cn">중국</option>
  </select>

  <!-- 텍스트 영역 -->
  <textarea name="message" rows="4" cols="50"></textarea>

  <!-- 제출 버튼 -->
  <input type="submit" value="제출" />
</form>
```

6. 시맨틱 태그

```html
<header>
  <!-- 헤더 영역 -->
  <nav>
    <!-- 네비게이션 -->
    <!-- 메뉴 항목들 -->
  </nav>
</header>

<main>
  <!-- 메인 콘텐츠 -->
  <article>
    <!-- 독립적인 콘텐츠 -->
    <section>
      <!-- 관련 콘텐츠 그룹 -->
      <!-- 내용 -->
    </section>
  </article>

  <aside>
    <!-- 사이드바 -->
    <!-- 부가 정보 -->
  </aside>
</main>

<footer>
  <!-- 푸터 영역 -->
  <!-- 저작권 정보 등 -->
</footer>
```

7. 테이블 태그

```html
<table>
  <thead>
    <!-- 테이블 헤더 -->
    <tr>
      <th>제목 1</th>
      <th>제목 2</th>
    </tr>
  </thead>
  <tbody>
    <!-- 테이블 본문 -->
    <tr>
      <td>내용 1</td>
      <td>내용 2</td>
    </tr>
  </tbody>
  <tfoot>
    <!-- 테이블 푸터 -->
    <tr>
      <td>합계</td>
      <td>100</td>
    </tr>
  </tfoot>
</table>
```

기본적인 HTML 구조:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>✨Welcome to WebSession✨</title>
  </head>
  <body>
    <header class="welcome-header">
      <h1 class="welcome-header__title">Welcome to YBigta WebSession✨</h1>
      <p class="welcome-header__text">
        If you have a Account, log in with your email or phone number.
      </p>
    </header>

    <form action="#" method="get" id="login-form">
      <input name="username" type="text" placeholder="Email or phone number" />
      <input name="password" type="password" placeholder="Password" />
      <input type="submit" value="Log In" />
      <a href="#">Find Account or Password</a>
    </form>

    <script></script>
  </body>
</html>
```

### 3. CSS 스타일링

CSS 선택자

1. 기본 선택자

```css
/* 전체 선택자 */
* {
  margin: 0;
  padding: 0;
}

/* 태그 선택자 */
div {
  background-color: #f0f0f0;
}

/* 클래스 선택자 */
.container {
  width: 100%;
  max-width: 1200px;
}

/* ID 선택자 */
#header {
  position: fixed;
  top: 0;
}
```

2. 결합 선택자

```css
/* 자식 선택자 (>) */
.parent > .child {
  margin: 10px;
}

/* 자손 선택자 (공백) */
.parent .descendant {
  padding: 5px;
}

/* 인접 형제 선택자 (+) */
h1 + p {
  font-size: 1.2em;
}

/* 일반 형제 선택자 (~) */
h1 ~ p {
  color: #666;
}
```

3. 가상 클래스 선택자

```css
/* 마우스 오버 시 */
.button:hover {
  background-color: #007bff;
}

/* 클릭 시 */
.button:active {
  transform: scale(0.98);
}

/* 첫 번째 요소 */
li:first-child {
  font-weight: bold;
}

/* 마지막 요소 */
li:last-child {
  border-bottom: none;
}

/* n번째 요소 */
li:nth-child(2n) {
  background-color: #f5f5f5;
}
```

4. 가상 요소 선택자

```css
/* 요소 앞에 콘텐츠 추가 */
.quote::before {
  content: '"';
  font-size: 24px;
}

/* 요소 뒤에 콘텐츠 추가 */
.quote::after {
  content: '"';
  font-size: 24px;
}

/* 첫 글자 스타일링 */
p::first-letter {
  font-size: 2em;
  font-weight: bold;
}

/* 첫 줄 스타일링 */
p::first-line {
  color: #007bff;
}
```

5. 속성 선택자

```css
/* 특정 속성을 가진 요소 */
input[type="text"] {
  border: 1px solid #ddd;
}

/* 특정 값으로 시작하는 속성 */
a[href^="https"] {
  color: green;
}

/* 특정 값으로 끝나는 속성 */
a[href$=".pdf"] {
  color: red;
}

/* 특정 값을 포함하는 속성 */
img[alt*="logo"] {
  max-width: 200px;
}
```

기본 스타일 예제:

```css
.welcome-header {
  margin: 90px 0px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.welcome-header__title {
  margin-bottom: 20px;
  font-size: 25px;
}
.welcome-header__text {
  width: 60%;
  opacity: 0.7;
}

#login-form {
  display: flex;
  flex-direction: column;
  margin: 0px 30px;
}

#login-form input {
  border: none;
  padding: 15px 0px;
  font-size: 18px;
  margin-bottom: 25px;
}
```

### 4. JavaScript 실습

DOM 조작과 API 요청 예제:

```javascript
// DOM 조작
document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector("#myButton");
  const resultDiv = document.querySelector("#result");

  button.addEventListener("click", async () => {
    try {
      const response = await fetch("http://localhost:8000/api/items");
      const data = await response.json();

      resultDiv.innerHTML = data
        .map(
          (item) => `
                <div class="item">
                    <h3>${item.title}</h3>
                    <p>${item.description}</p>
                </div>
            `
        )
        .join("");
    } catch (error) {
      console.error("에러 발생:", error);
    }
  });
});

// POST 요청 예제
async function createItem(item) {
  try {
    const response = await fetch("http://localhost:8000/api/items", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(item),
    });
    return await response.json();
  } catch (error) {
    console.error("에러 발생:", error);
  }
}
```

---

# Backend

## FastAPI 시작하기

### 1. 환경 설정

```bash
# 가상환경 생성 및 활성화

# 패키지 설치
pip install fastapi uvicorn
cd BE
pip install -r requirements.txt
```

### 2. API 엔드포인트 만들기

기본 FastAPI 앱 예제:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 데이터 모델
class Item(BaseModel):
    title: str
    description: str

# 임시 데이터 저장소
items = []

# GET 엔드포인트
@app.get("/api/items", response_model=List[Item])
async def read_items():
    return items

# POST 엔드포인트
@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

# 경로 매개변수 사용
@app.get("/api/items/{item_id}")
async def read_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### 3. CORS 설정

CORS(Cross-Origin Resource Sharing)는 웹 브라우저에서 보안상의 이유로 다른 출처(도메인, 프로토콜, 포트)의 리소스에 접근하는 것을 제한하는 정책.

FastAPI에서는 CORSMiddleware를 사용하여 CORS 설정을 할 수 있다:

```python
from fastapi.middleware.cors import
CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 실행 방법

```bash
# FastAPI 서버 실행(파일이름:app --port 8000 --reload)
uvicorn main:app --reload
```

## Swagger 문서

- 서버 실행 후 http://localhost:8000/docs 접속(8000은 포트번호)
- 모든 API 엔드포인트 테스트 가능
