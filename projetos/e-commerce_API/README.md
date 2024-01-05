# E-Commerce Geek - Front End

Bem-vindo ao projeto E-Commerce Geek - Front End! Este projeto faz parte do Módulo 1, onde a equipe de Front End está desenvolvendo uma interface para permitir aos usuários cadastrar produtos relacionados à cultura geek.

## Funcionalidades

- **Cadastro de Produtos:** Os usuários podem cadastrar produtos informando o nome, valor e descrição.

- **Feedback em Tempo Real:** O sistema fornece feedback em tempo real sobre o sucesso ou falha no cadastro do produto.

- **Exibição de Produtos Cadastrados:** Produtos cadastrados com sucesso são exibidos na seção 'Produtos Cadastrados'.

## Tecnologias Utilizadas

- HTML
- CSS
- JavaScript
- Fetch API

## Instruções do Projeto

Você faz parte da equipe de Front End de um e-commerce onde usuários poderão comprar e vender produtos relacionados à cultura geek. A equipe de Back End está desenvolvendo uma API para permitir aos usuários postar os produtos que querem vender, e para isso encaminharam para você os seguintes trechos da documentação que estão montando:

Para cadastrar um produto é necessário enviar uma requisição do tipo POST para a URL https://httpbin.org/post, enviando uma string JSON como corpo da requisição. A string JSON deve ser um objeto com pelo menos três propriedades: produto, valor e descrição.

Crie um site simples com inputs para o nome, o valor, a descrição do produto e um botão para enviar as informações, além de um elemento textual vazio para mostrar um feedback. Escreva o código JavaScript necessário para capturar as informações inseridas pelo usuário, enviá-las para o Back End usando a Fetch API, e tratar a resposta da requisição avisando ao usuário se o cadastro do produto foi ou não realizado com sucesso. Lembre de limpar os inputs caso a requisição seja tratada com sucesso, e de manter os valores preenchidos pelo usuário caso a requisição seja rejeitada.

## Como Usar

1. Clone o repositório.
2. Abra o arquivo `index.html` em seu navegador.
3. Preencha os campos do formulário com as informações do produto.
4. Clique no botão `"Enviar"` para cadastrar o produto.
5. Observe o feedback em tempo real e verifique os produtos cadastrados na seção `'Produtos Cadastrados'`.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

