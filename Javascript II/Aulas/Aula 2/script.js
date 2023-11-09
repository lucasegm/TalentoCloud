let div = document.querySelector("div")

let incluiClasse = div.classList.contains("borda-azul")

console.log(incluiClasse)

div.classList.add("texto-novo")
div.classList.remove("borda-azul")

// a variavel div está recebendo a classe texto-novo, e borda-azul, que já estão feitas no css//

div.classList.toggle("borda-azul")
div.classList.toggle("borda-azul")

// a funcao toggle verifica que o elemento possui a classe
// se possuir ele remove, se não ele adiciona. //


