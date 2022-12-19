const CheckSpaces = (str) => str.trim() !== '';

function goToHome() {
  window.location.href = 'http://localhost:8080';
}

async function registRequest() {

  let fullName = document.getElementById("InputFull_name").value;
  let log = document.getElementById("InputLogin").value;
  let passw = document.getElementById("InputPassword").value;

  if (CheckSpaces(fullName) && CheckSpaces(log) && CheckSpaces(passw)) {

    let user = {
      full_name: fullName,
      login: log,
      password: passw,
    };

    let response = await fetch('./api/user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(user)
    });
    console.log(response.json())
    if (confirm("Вы успешно зарегистрировались на сайте! Перейти на страницу с авторизацией?")) {
      goToHome();
    }
  } else {
    alert('Поле не заполнено!!');
  }

}

let objUser;
async function loginInRequest() {
  let log = document.getElementById("InputLogin1").value;
  let pas = document.getElementById("InputPassword1").value;
  if (CheckSpaces(log) && CheckSpaces(pas)) {
    let response = await fetch(`./api/user/${log}/${pas}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
    });
    try {
      let result = await response.json();
      objUser = {
        name: result.full_name,
        login: result.login,
        password: result.password,
      }
      document.getElementById('main').innerHTML = 
      `
      <h1>Привет,  ${objUser.name}</h1>
      <h2>Ваш пароль: ${objUser.password}</h2>
      <h2>Ваш логин: ${objUser.login}</h2>
      <a href="http://localhost:8080"><button class="btn btn-primary">Выйти из аккаунта</button></a>
      `;
      } catch {
      window.location.href = 'http://localhost:8080/notregist.html';
    }
  } else {
    alert('Поле не заполнено!!');
  }
}