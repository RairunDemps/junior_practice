function displayMeow() {
    document.getElementById("demo").innerHTML = "Meow";
}

function displayWoof() {
    document.getElementById("demo").innerHTML = "Woof";
}

const btn = document.querySelector("button");
function greet(event) {
  console.log("greet:", event);
}
btn.onclick = greet;


const eventButton = document.getElementById("eventButton");
function greet2(event) {
  console.log("greet2:", event);
  controller.abort();
}
eventButton.addEventListener("click", greet2);

const controller = new AbortController();
const abortButton = document.getElementById("abortButton");
function greet3(event) {
  console.log("greet3:", event)
}
abortButton.addEventListener(
  "click",
  (event) => {
    console.log("greet3:", event);
  },
  { signal: controller.signal }
)
