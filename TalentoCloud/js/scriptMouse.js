let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};
 
function atualizarSubtotal(){
  quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
  valorSubtotal.innerText = subtotalInfo.valor;
}

atualizarSubtotal();


//variaveis/dados
let btnAdicionarProduto01 = document.querySelector('#btn-adicionar-produto-01');
let quantidadeProduto01 = document.querySelector('#quantidade-produto-01');
let valorProduto01 = 11.66;

//Funcoes
function adicionarUm(){
  //Manipular input (adicionar 1)
  quantidadeProduto01.value = Number(quantidadeProduto01.value) + 1;

  //Manipular quantidade no subtotalInfo
  subtotalInfo.quantidade = subtotalInfo.quantidade + 1;

  //Manipular valor no subtotalInfo
  subtotalInfo.valor = subtotalInfo.valor + valorProduto01;

  //Atualizar o DOM
  atualizarSubtotal();
}
console.log(typeof quantidadeProduto01.value);

//Eventos
btnAdicionarProduto01.addEventListener("click", adicionarUm);
