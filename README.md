# desafio-cloudpark-sistema-chamados
Sistema de Chamados - Desafio Técnico CloudPark


##### CONFIGURAÇÕES BACKEND 

* **Backend**
   1. Faça o clone do repositório no github ou donwload ZIP do repositório
   ```.sh
    git clone https://github.com/brennolsantos/desafio-cloudpark-sistema-chamados.git
   ```

   2. Mude para a pasta
   ```.sh
   cd desafio-cloudpark-sistema-chamados
   ```
   3. Crie um ambiente virtual python e o ative
   ```.sh
   python3 -m virtualenv venv
   source venv/bin/activate #ou venv\Scripts\Activate para windows
   ```

   4. Instale as dependencias:
   ```
   pip install -r requirements.txt
   ```

   5. Em seguida, crie as tabelas no banco de dados
   ```
   python manage.py makemigrations autenticacao
   python manage.py makemigrations atendentes
   python manage.py makemigrations tecnicos

   python manage.py migrate
   ```

   6. Inicie o servidor na porta 8000
   ```.sh
   python manage.py runserver 0.0.0.0:8000
   ```

   7. Acesse localhost:8000 e utilize o sistema onde você poderá: se cadastrar como atendente, fazer login, criar editar e remover chamado  
     


* **Frontend**
  1. Abra outra aba do terminal e se localize na mesma pasta do inicio do tutorial 

  2. Mude para a pasta correta e nstale as dependencias
  ```.sh
  cd frontend
  npm install  
  ```

  3. Rode o sistema na porta 5173
  ```.sh
  npm run dev 
  ```
  Acesse localhost:5173 e acesse o sistema de tecnicos onde você poderá: logar e se cadastrar como tecnico, editar chamados e marcar como resolvido


* **Observações**
  1. O sistema de atendentes possui um websockets interno com django-channels, onde um usuário poderá modificar e ver instantaneamente a alteração em dispositivos diferentes
  
  2. Estava previsto para utilizar websockets no frontend, mas resolvi só deixar um botão de atualização para não correr o risco de passar a deadline, já que tive apenas parte do fim de semana livre para fazer

  3. Frontends básicos usando bootstrap

  4. Comecei o projeto utilizando branchs e pull requests, mas depois tive que acelerar o processo e aumentar o tamanho dos commits devido o prazo apertado
