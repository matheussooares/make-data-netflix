## Considerações iniciais

- [Dataset no GitHub](https://github.com/digitalinnovationone/netflix-dataset/tree/main/raw): os dados são fictícios da empresa Netflix.

- Pacotes utilizados: 
  pip install pandas
  pip install openpyxl
  pip install xlsxwriter


- ***Virtual Enviroment*** ou ambiente virtual: serve para encapsular a aplicação, sem ficar prezo a versões diferentes. Mais informações sobre ambiente virtuais em python, basta acessar o [link](https://www.alura.com.br/artigos/ambientes-virtuais-em-python?_gl=1*17pwqit*_ga*OTE0MTYyOTM4LjE3MTAxNjUxNTI.*_ga_1EPWSW3PCS*MTcxMzc4NzAyOS4xOS4xLjE3MTM3OTA2NzAuMC4wLjA.*_fplc*MEslMkJsVFdLMnR3b2QlMkZwRGVtNmYlMkZtOWJManhrdlRtM1RINGFGSjNSZDIzMTclMkJUZ1dBTlZtU1A5SHolMkZmRXlmJTJGRUdZUExmbE5mV051Y3Z6c2slMkJwbXM2MnJTclVDUzJVY28lMkZMZ01wJTJCQzklMkJsdndmMWZFSktoaWVvb0xYZnoxNHclM0QlM0Q.). Para criar e ativar um ambiente:
    ```` 
    python -m venv venv

    venv/scripts/activate
    ````
    Caso esteja no windows e o powershell apresentar uma restrinção. Vá no *Windows Powershell(Admin)*, e usar o comando;
    ````
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ````

- ***Código Fonte (src)***: Códigos fontes e arquivos do projeto, dataset etc.
    - Na pasta (data) é armazenado os dados, que estão divididos entre:
      - **raw**: todos os dados de maneira bruta ou cru;
      - **ready**: dados tratados, ou seja, passou pelo seu respectivo processo de tratamento.
    - Em (scripts) é armazenados outros códigos relacionados a outras execuções


## Pipeline de dados

A técnica utilizada foi a ETL (extrair, transformar e carregar), prezanda pela confiabilidade e rastreabilidade dos dados.

Os dados brutos estão localizados na pasta [raw](https://github.com/matheussooares/make-data-netflix/tree/main/src/data/raw), e foram extraidos do [Dataset no GitHub](https://github.com/digitalinnovationone/netflix-dataset/tree/main/raw).

Para a transformação dos dados brutos é sugerido colocar todas as tabelas em um único aquivo (.xlsx). A adição das colunas "location" e "file_name" é para validar a rastreabilidade dos dados.

Por fim, os dados são carregados na [ready]([src/data/ready](https://github.com/matheussooares/make-data-netflix/tree/main/src/data/ready)) e estão disponíveis para a análise de **BI**.
