const allButtons = document.getElementsByClassName("playButton");
const request = new XMLHttpRequest();

for (button in allButtons) {
    if (typeof(allButtons[button]) == "object") {
        allButtons[button].addEventListener('click', (event) => {
            const requestURL = `http://127.0.0.1:5000/content/getvoiceover/${event["target"].id}`;
            request.open("GET", requestURL);
            request.responseType = "text";
            request.send();
            request.onload = function () {
                let link = request.response;
                playSound(link);
                playSound(link);
            };
        });
    };
};

function playSound(link) {
    const sound = new Audio(link);
    sound.play();
};