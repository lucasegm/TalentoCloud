function calcularOperacoes(n1, n2) {
    let operacoes = [];
    operacoes.push(`A soma de ${n1} + ${n2} é ${n1 + n2}`);
    operacoes.push(`A subtração de ${n1} - ${n2} é ${n1 - n2}`);
    operacoes.push(`A multiplicação de ${n1} com ${n2} é ${n1 * n2}`);
    operacoes.push(`A divisão de ${n1} por ${n2} é ${(n1 / n2).toFixed(2)}`);
    return operacoes;
  }
  
  let n1 = 5;
  let n2 = 3;
  
  console.log('Exemplos de operações com Template Strings');
  
  let operacoes = calcularOperacoes(n1, n2);
  
  for (let operacao of operacoes) {
    console.log(operacao);
  }