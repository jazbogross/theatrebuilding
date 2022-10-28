var text = document.getElementById('title').innerText;
var language = window.navigator.userLanguage || window.navigator.language;
language = language.slice(0,2);
async function translate() {
    if (language == "en") {
        console.log("browser language is identical to source")
    } else {
    const res = await fetch("https://lt.vern.cc/translate", {
    method: "POST",
    body: JSON.stringify({
        q: text,
        source: "en",
        target: language,
        format: "html"
    }),
    headers: { "Content-Type": "application/json" }
    });
    const newTitle = await res.json();
    console.log(newTitle);
    const myTitle = newTitle["translatedText"];
    document.getElementById('title').innerHTML = "<h1>" + myTitle + "</h1>";

    }
}
// translate();