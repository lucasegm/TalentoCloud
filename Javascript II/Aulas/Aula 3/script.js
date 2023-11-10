let numero = document.querySelector("h1")
let botao = document.querySelector("button")
let contagem =0;

function adicionarUm(){
    contagem = contagem + 1
    numero.innerText = contagem
}

adicionarUm()

botao.addEventListener("click", adicionarUm);


 
// temos a funcao anonima 

// botao.addEventListener("click", function(){
//  contagem = contagem + 1;
//  numero.innerText = contagem;
// }); 



// E a arrow function

//botao.addEventListener("click", () => {
//    contagem = contagem + 1;
//    numero.innerText = contagem;
//});