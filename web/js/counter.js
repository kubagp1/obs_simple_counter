const counter = document.getElementById("counter");

eel.expose(setCounter)
function setCounter(n) {
    counter.innerText = n;
}