console.log("Hello World"); // 프린트
// DOM 요소 선택
const loginForm = document.getElementById("login-form");
const usernameInput = loginForm.querySelector('input[name="username"]');
const passwordInput = loginForm.querySelector('input[type="password"]');

// 폼 유효성 검사 함수
function validateForm(username, password) {
  if (!username || username.length < 3) {
    alert("사용자명은 3글자 이상이어야 합니다.");
    return false;
  }
  if (!password || password.length < 6) {
    alert("비밀번호는 6글자 이상이어야 합니다.");
    return false;
  }
  return true;
}

// 로그인 성공 시 실행될 함수
function handleLoginSuccess(username) {
  alert(`${username}님, 환영합니다!👀👀`);
}

// 폼 제출 이벤트 처리
loginForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const email = document.querySelector('input[type="email"]').value;
  const password = document.querySelector('input[type="password"]').value;
  const username = document.querySelector('input[type="text"]').value;

  //   try {
  //     const response = await fetch("http://localhost:8000/api/user/login", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({
  //         email,
  //         password,
  //         username,
  //       }),
  //     });
  //     //
  //     const data = await response.json();

  //     if (response.ok) {
  //       handleLoginSuccess(data.username);
  //       // 로그인 성공 후 리다이렉트 또는 다른 처리
  //     } else {
  //       alert(data.detail);
  //     }
  //   } catch (error) {
  //     console.error("로그인 에러:", error);
  //     alert("로그인 처리 중 오류가 발생했습니다.");
  //   }

  // 임의로 성공 처리
  handleLoginSuccess(username);
});

// 개발용 콘솔 로그
console.log("로그인 폼 JavaScript 로드 완료");
