# FireTracker - Gerenciamento de Manutenção de Extintores de Incêndio

FireTracker é um projeto em Django desenvolvido para auxiliar no gerenciamento da manutenção de extintores de incêndio. Com esta aplicação, você poderá acompanhar facilmente o estado de cada extintor, agendar e registrar manutenções, além de visualizar relatórios de desempenho.

## Recursos principais

- Cadastro de extintores: Adicione informações detalhadas sobre cada extintor, como localização, tipo e data de validade.
- Agendamento de manutenções: Defina datas para a realização das manutenções em cada extintor.
- Registro de manutenções: Registre as manutenções realizadas, incluindo detalhes, data e responsável.
- Status de extintores: Acompanhe o status de cada extintor, indicando se está em dia com a manutenção ou se precisa de atenção.
- Relatórios: Gere relatórios personalizados sobre o desempenho dos extintores, incluindo estatísticas de manutenção e validade.

## Requisitos

- Python 3
- Django 3
- Django Restframework

## Como usar

1. Clone o repositório:
 ```
git clone https://github.com/BeatrizUser/FireTracker.git
 ```
2. Navegue até o diretório do projeto:
 ```
cd FireTracker
 ```

3. Crie um ambiente virtual:
 ```
python3 -m venv venv
 ```
4. Ative o ambiente virtual:
- No Linux/macOS:
  ```
  source venv/bin/activate
  ```
- No Windows:
  ```
  venv\Scripts\activate
  ```

5. Instale as dependências:
```
pip install -r requirements.txt
 ```

7. Execute as migrações do banco de dados:
 ```
python manage.py migrate
```

9. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
 ```

11. Acesse o aplicativo no seu navegador em http://localhost:8000/.


## Contribuindo

- Contribuições são bem-vindas! Se você desejar contribuir com o FireTracker.

