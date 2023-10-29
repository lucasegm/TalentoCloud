// && = and //
// || = or //
// ! = negativação da pergunta true //
// % = retorna o resto de uma divisão, ou seja se ao dividir um número entre 2, se o resto for - quer dizer que ele é par //

let idadeMotorista = 17;
let idadehabilitacao = 18;
let habilitacao = idadehabilitacao >= idadeMotorista;

console.log(habilitacao)

// Estas sao duas formas de realizar a mesma operacao //

let idade = 17;
let idadeCarteira = 18;
let carteira = idadeCarteira - idade;

if(idade >= 18){
    console.log('Aprovado');
} else{
    console.log('Tente novamente daqui há ' + carteira + ' ano')
}

