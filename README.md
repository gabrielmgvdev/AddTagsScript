# AddTagsScript



> Adicione uma tag a múltiplos Work Itens no Azure DevOps de uma só vez!

## 🔑 Gerando a chave PAT

Para usar o script corretamente, siga estas etapas:

1️⃣ Acesse o Azure DevOps

- Vá para: Azure DevOps
- Faça login na sua conta.


2️⃣ Vá para as Configurações de Segurança

- No canto superior direito, clique na sua foto de perfil.
- Selecione "Configurações do usuário" (User settings) .
- Clique em "Tokens de Acesso Pessoal" (Personal Access Tokens) .


3️⃣ Criação de um Novo Token

- Clique em "+" Criar um Token Novo" (New Token) .
- Dê um nome para o token (exemplo: "Meu Script de Tags").
- Defina a data de expiração (por exemplo, 30 ou 90 dias).
- Escolha o escopo de permissões :
- Se o objetivo for manipular Work Items , role até a seção "Work Items" e selecione "Read & Write".
- Se for querer mais permissões, pode selecionar "Full Access", mas é menos recomendado por segurança.


4️⃣ Gerar e Copiar o Token

- Clique em "Criar" .
- O token será gerado apenas uma vez. Então, copie-o imediatamente e salve-o em um local seguro.

## 👩🏻‍💻 Configurando o script

- Com a chave em mãos, cole ela no objeto "pat". Coloque a chave entre aspas, por exemplo: "123456".

```
pat = "SEU_PERSONAL_ACCESS_TOKEN_AQUI"
```

- Edite também os campos *organization*, *project*, *tag_to_add* e *work_items_ids*:
```
organization = "sua-organizacao"  
project = "seu-projeto"  
tag_to_add = "sua-tag"  
work_items_ids = [123, 321]
```

