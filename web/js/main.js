const addButton = document.getElementsByClassName("addButton")[0];
const removeButton = document.getElementsByClassName("removeButton")[0];
const counter = document.getElementsByClassName("counter")[0];

const resetButton = document.getElementsByClassName("resetButton")[0];

const klState = document.getElementsByClassName("klState")[0];

const klSwitch = document.getElementsByClassName("klSwitch")[0];

const listenedKey = document.getElementsByClassName("listenedKey")[0];
const changeLK = document.getElementsByClassName("changeLK")[0];

async function updateCounter(){
    counter.innerText = await eel.getCounterValue()()
}
updateCounter()

async function updateState(){    
    if (await eel.checkKLThread()()) {
        klState.innerText = "On"
        klState.classList.remove("red")
        klState.classList.add("green")
        klSwitch.innerText = "Turn off"
    } else {
        klState.innerText = "Off"
        klState.classList.remove("green")
        klState.classList.add("red")
        klSwitch.innerText = "Turn on"
    }
}
updateState()

setInterval(updateState, 5000)

eel.expose(setCounter)
function setCounter(n) {
    counter.innerText = n;
}

addButton.addEventListener("click", function(){
    eel.add1()
});

removeButton.addEventListener("click", function(){
    eel.remove1()
});

resetButton.addEventListener("click", function(){
    if (confirm("Are you sure you want to reset counter?")) {
        eel.resetCounter()
    }
});

klSwitch.addEventListener("click", async function(){
    klSwitch.disabled = true;

    if(klSwitch.innerText == "Turn off") {
        await eel.stopKL()()
    } else {
        await eel.startKL()()
    }
    await updateState()
    klSwitch.disabled = false;
});

changeLK.addEventListener("click", async function(){
    listenedKey.innerText = await eel.changeLK()();
});