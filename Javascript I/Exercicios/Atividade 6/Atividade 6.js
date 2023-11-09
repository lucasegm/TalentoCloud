let n1 = 5;
let n2 = 3;

console.log('Exemplos de operações com Template Strings')

let soma = `A soma de ${n1} + ${n2} é ${n1 + n2}`
let sub = `A subtração de ${n1} - ${n2} é ${n1 - n2}`
let mult = `A multiplicação de ${n1} com ${n2} é ${n1 * n2}`
let div = `A divisão de ${n1} por ${n2} é ${(n1 / n2).toFixed(2)}`

console.log(soma)
console.log(sub)
console.log(mult)
console.log(div)