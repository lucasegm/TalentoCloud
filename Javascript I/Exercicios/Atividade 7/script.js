const elementoH1 = document.createElement("div")

elementoH1.innerHTML = `
<h1>Timão Camisas</h1>
`
const titulo = document.querySelector("body")
titulo.appendChild(elementoH1)

const elementoVenda = document.createElement("div")

elementoVenda.id = "produtos"
elementoVenda.innerHTML = `
    <div>
        <img src="camisa 1.jpg" width="200px" height="200px">
        <h3>Camisa 1 - Jogador</h3>
        <p>R$ 250,00</p>
        <button><a href="">Comprar</a></button>
    </div>
`

const produto = document.querySelector("body")
produto.appendChild(elementoVenda);

let produto2 = document.createElement("div")

produto2.innerHTML = `
        <br>
        <img src="camisa 2.jpg" width="200px" height="200px">
        <h3>Camisa 2 - Jogador</h3>
        <p>R$ 230,00</p>
        <button><a href="">Comprar</a></button>
`

let camisa2 = document.querySelector("#produtos")
camisa2.appendChild(produto2)
