// Este metódo se chama concatenar

let nome = 'Lucas'
let sobrenome = 'Moreira'

let nomeCompleto = nome + sobrenome
console.log(nomeCompleto)

// Com a interpolação, o processo fica assim: (Usamos acentos e o $)//

let fullName = `Meu nome é ${nome} ${sobrenome}.`
console.log(fullName)

// Podemos fazer isso com operadores //
let n1 = 7
let n2 = 5
let soma = `A soma de ${n1} + ${n2} é ${n1 + n2}`
console.log(soma)