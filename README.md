# loja-fluxo
Quinta entrega para o processo PAME 21.2 da Fluxo Consultoria

## Funcionamento do programa:
Todos as tabelas possuem post e get. Caso acesse o id (http://127.0.0.1:5000/usuarios/1 por exemplo) terão get, put, patch e delete. 


###### **Usuário:** 
Coloque IP/usuarios 
\
Por exemplo: http://127.0.0.1:5000/usuarios \
Campos necessários para funcionar: \
nome (string, digite com "") \
cpf  (string, digite com "") \
email (string, digite com "") \
telefone (string, digite com "")\
endereco (string, digite com "")


###### **Carrinho:** 
Coloque IP/carrinhos \
Campos necessários para funcionar: \
forma_pagamento (string, digite com "")\
preco_frete (int, digite sem "")\
quantidade (int, digite sem "")\
preco_total (int, digite sem "")


###### **Cupons:** 
Coloque IP/cupons \
Campos necessários para funcionar: \
codigo_cupom (int, digite sem "")\
valor_desconto (int, digite sem "")\
quantidade (int, digite sem "")\
categoria (string, digite com "")

###### **Novidades:** 
Coloque IP/novidades \
Campos necessários para funcionar: \
nome_novidade (string, digite com "")\
descricao (string, digite com "")\
preco (int, digite sem "")\
validade (string, digite com "")\
data_lancamento (string, digite com "")

###### **Novidades Carrinho:** 
Coloque IP/novidadescarrinho \
Campos necessários para funcionar: \
nome_novidade (string, digite com "")\
quantidade (int, digite sem "")\
preco_unitario  (int, digite sem "")

###### **Produtos:** 
Coloque IP/produtos \
Campos necessários para funcionar: \
nome_produto (string, digite com "")\
descricao (string, digite com "")\
preco (int, digite sem "")\
validade (string, digite com "")

###### **Produtos Carrinho:** 
Coloque IP/produtoscarrinho \
Campos necessários para funcionar: \
nome_produto (string, digite com "")\
quantidade (int, digite sem "")\
preco_unitario  (int, digite sem "")



