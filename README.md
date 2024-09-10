# SGym

# Gym Management Project

Este repositório contém um projeto desenvolvido para aprimorar conhecimentos sobre padrões de projeto de software.

## Descrição

O projeto implementa uma interface de gerenciamento de usuários, organizando o código com base na arquitetura MVC (Model-View-Controller). A aplicação foi desenvolvida com o intuito de explorar e entender melhor a aplicação de diversos padrões de projeto, incluindo Singleton e DAO.

## Estrutura do Projeto

- **Model**: Contém as classes que representam a lógica de negócios, como usuários, clientes, personal trainers, e suas respectivas funcionalidades.
- **View**: Inclui as interfaces de usuário, tanto para administradores quanto para clientes, personal trainers, entre outros.
- **Controller**: Gerencia a lógica que conecta as views aos models, controlando o fluxo de dados e a lógica de aplicação.
- **Persistence**: Implementa o padrão DAO (Data Access Object) para manipulação e persistência de dados, facilitando o acesso e a manipulação dos dados da aplicação.

## Padrões de Projeto Utilizados

- **MVC (Model-View-Controller)**: Estrutura básica da aplicação, separando as responsabilidades em Model, View e Controller.
- **Singleton**: Utilizado para garantir que certas classes tenham apenas uma instância ativa durante a execução do programa.
- **DAO (Data Access Object)**: Utilizado para abstrair e encapsular todas as interações com o armazenamento de dados.

