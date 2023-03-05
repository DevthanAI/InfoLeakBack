function setCookie(cname, cvalue, exdays) {
    let d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

let ballColor = getCookie("ballColor");
if (!ballColor) {
    ballColor = Math.random() > 0.5 ? "red" : "blue";
    setCookie("ballColor", ballColor, 100);
}

let ball = document.getElementById("ball");
ball.classList.add(ballColor + "-ball");

let cookies = {};
let cookieArray = document.cookie.split(';');

for (let i = 0; i < cookieArray.length; i++) {
    let cookie = cookieArray[i];
    let cookieParts = cookie.split('=');
    let key = cookieParts[0].trim();
    let value = cookieParts[1].trim();
    cookies[key] = value;
}

let ballCount = getCookie(ballColor);
if (ballCount === null) {
    ballCount = 0;
}
ballCount++;
setCookie(ballColor, ballCount);

// Check cookie information
console.log(ballColor, ballCount);