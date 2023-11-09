let elementoH1 = document.getElementById("titulo")
let elementoUl = document.querySelector("ul")
let elementoA = document.querySelector("a")
let elementoOl = document.getElementById("lista-ordenada")

console.log(elementoH1)
console.log(elementoUl)
console.log(elementoA)
console.log(elementoOl)

elementoH1.innerText = "Bem vindo ao FutebolMax"
elementoUl.innerHTML = `
<h3>Top 3 Jogadores do Ano</h3>
<ul>
<li>Messi</li>
<li>Halland</li>
<li>Mbappé</li>
</ul>
`

elementoA.innerText = "Site PROZ"

elementoOl.innerHTML = `
<h3>Gols mais bonitos do ano</h3>
<ol>
    <li><a href="https://www.youtube.com/watch?v=zNR5j-QHJ7U" target="_blank">Messi</a></li>
    <li><a href="https://www.youtube.com/shorts/ljmURBqccO0" target="_blank">Halland</a></li>
    <li><a href="https://www.youtube.com/watch?v=mAHbXeCRPm0" target="_blank">Mbappé</a></li>
</ol>
`
