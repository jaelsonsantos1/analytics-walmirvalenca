# Sistema de Avaliação de Desempenho - Walmir Valença

## Descrição
Este é um aplicativo desenvolvido para facilitar o registro de avaliações de desempenho dos colaboradores internos da empresa Walmir Valença. O sistema utiliza tecnologias como Python e PostgreSQL, e algumas bibliotecas notáveis incluem Streamlit e Pandas. O ambiente virtual foi empregado para garantir a consistência do ambiente de desenvolvimento.

## Funcionalidades

### 1. Dashboard
Uma área dedicada para exibir informações sobre as avaliações de desempenho dos colaboradores em forma de gráficos, proporcionando uma visão geral rápida e intuitiva.

### 2. Página de Avaliação
Nesta página, os gestores podem preencher formulários para registrar suas avaliações de desempenho para os colaboradores. Isso contribui para um processo transparente e estruturado de avaliação.

### 3. Página de Cadastro
Destinada aos gestores, esta página permite o cadastro de novos colaboradores. Isso é fundamental para manter o sistema atualizado com as informações mais recentes sobre a equipe.

### 4. Página de Gestão de Avaliações
Neste espaço, todas as avaliações feitas pelos gestores são registradas. Os gestores têm a capacidade de excluir avaliações, proporcionando flexibilidade e controle sobre o histórico de avaliações.

## Arquitetura MVC
O sistema segue a arquitetura Modelo-Visão-Controlador (MVC), uma abordagem que separa as responsabilidades em três componentes principais:

- **Modelo**: Responsável pela manipulação dos dados e regras de negócios. No caso, as operações no banco de dados PostgreSQL e lógica de avaliação.
  
- **Visão**: Refere-se à interface do usuário, neste contexto, implementada com a biblioteca Streamlit. Toda a apresentação gráfica e interação com o usuário ocorre nesta camada.

- **Controlador**: Responsável por gerenciar as interações entre a Visão e o Modelo. Garante que as ações do usuário sejam refletidas corretamente no sistema, manipulando os dados conforme necessário.

## Configuração do Ambiente Virtual
Certifique-se de criar e ativar um ambiente virtual para garantir a consistência das dependências. Utilize o seguinte comando:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
```

## Instalação de Dependências
Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Como Executar
Certifique-se de ter o ambiente virtual ativado e as dependências instaladas. Execute o aplicativo usando o seguinte comando:

```bash
streamlit run app.py
```

Acesse o aplicativo através do navegador no endereço fornecido pelo Streamlit.

**Observação:** Lembre-se de configurar corretamente as informações de conexão com o banco de dados PostgreSQL no arquivo de configuração.

Este aplicativo visa simplificar o processo de avaliação de desempenho, proporcionando uma maneira eficiente e centralizada de gerenciar as avaliações dos colaboradores na empresa Walmir Valença.
