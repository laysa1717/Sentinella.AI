# Sentinella.AI

Sentinella é uma API inteligente desenvolvida em Python com Flask que identifica e interpreta sentimentos em textos de forma simples e eficiente. Ideal para aplicações que precisam entender a opinião do usuário, como reviews de produtos, comentários em redes sociais ou feedbacks de atendimento.

## Requisitos

- **Python**: Certifique-se de ter o Python 3.8 ou superior instalado em seu sistema.

## Arquitetura

A arquitetura do Sentinella.AI é baseada em uma estrutura cliente-servidor, onde o Flask atua como o servidor que processa as requisições de análise de sentimento. A API utiliza modelos de machine learning para interpretar o sentimento dos textos recebidos.

## Passo a Passo para Rodar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sentinella-ai.git
   cd sentinella-ai
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor**:
   ```bash
   flask run
   ```

5. **Teste a API**:
   - Para testar a API, envie mensagens em inglês para obter resultados precisos de análise de sentimento.

## Observações

- A API está otimizada para processar textos em inglês. Para melhores resultados, certifique-se de que as entradas estejam nesse idioma.

## Testes

Para rodar os testes, use o seguinte comando:
```bash
python -m unittest tests/test_textBlob_service.py
```
