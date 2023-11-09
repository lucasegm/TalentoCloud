let elementoJavaScript = document.createElement("li");

elementoJavaScript.innerText = "Javascript"
elementoJavaScript.id = "ling.js"

let listaLinguagens = document.querySelector(".lista-linguagens");
listaLinguagens.appendChild(elementoJavaScript);

console.log(elementoJavaScript)

const postagemJavaScript = document.createElement("div")

postagemJavaScript.innerHTML = `
<h2 class="post-titulo">Javascript</h2>
<p class="post-texto"> JavaScript é uma linguagem de programação</p>
`
const postagens = document.querySelector(".postagens");
postagens.appendChild(postagemJavaScript);

console.log(postagemJavaScript)

