const nomeProduto = document.getElementById("nome-produto");
const valorProduto = document.getElementById("valor-produto");
const descricaoProduto = document.getElementById("descricao-produto");
const btnEnviar = document.getElementById("btn-enviar");
const feedbackUsuario = document.getElementById("feedback-usuario");
const produtosCadastrados = document.getElementById("produtos-cadastrados");

function cadastrarProduto(e) {
  feedbackUsuario.innerText = "Carregando...";
  e.preventDefault();

  const produtoData = {
    nome: nomeProduto.value,
    valor: parseFloat(valorProduto.value), // Convertendo para número
    descricao: descricaoProduto.value,
  };

  const jsonBody = JSON.stringify(produtoData);

  fetch("https://httpbin.org/post", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonBody,
  })
    .then((res) => res.json())
    .then((data) => {
      // Precisa dessa constante, pois ele estava puxando os valores como string e não um objeto JSON
      const jsonfy = JSON.parse(data.data);

      console.log(jsonfy);
      console.log(data.data);

      const novoProduto = document.createElement("div");

      novoProduto.classList.add("novoProduto");
      novoProduto.innerHTML = `
            <h3>${jsonfy.nome} - R$ ${jsonfy.valor.toFixed(2)}</h3>
            <p>${jsonfy.descricao}</p>
        `;

      // Adicionando o novo produto à seção 'Produtos Cadastrados'
      produtosCadastrados.prepend(novoProduto);

      // Limpando os dados
      nomeProduto.value = "";
      valorProduto.value = "";
      descricaoProduto.value = "";
      feedbackUsuario.innerText = "";
      alert("Cadastro do produto realizado com sucesso!");
    })
    .catch((error) => {
      console.log(error);
      feedbackUsuario.innerText = "Não foi possível cadastrar o produto!";
    });
}

btnEnviar.addEventListener("click", (e) => cadastrarProduto(e));
