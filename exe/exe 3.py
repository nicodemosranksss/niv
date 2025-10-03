loja_frutas = {
    'maça': {'preço': 3.50,
             'quantidade':10},
    'banana': {'preço': 3.50,
               'quantidade':10},
    'uva': {'preço':3.50,
            'quantidade':10},           
}

loja_frutas.update({'limão':{'preço':3.50,'quantidade':10},
                   'laranja':{'preço':3.50, 'quantidade':10},
                   'abacaxi':{'preço': 3.50, 'quantidade':10}})
print(loja_frutas)

for k,v in loja_frutas.items():
    loja_frutas.get(k)['preço']*=1.15
print(loja_frutas)

for k,v in loja_fruta.items():
    loja_fruta.get(k)['quantidades']+=20
    print(loja_fruta)

    loja_fruta.pop('maça')
    #Exericicos

loja_comidas ={
    'laranja baiana':{
        'valor': 4.00,
    },
    'maca verde':{
        'valor': 5.00,
    },
    'coco verde':{
        'valor': 2.00,
    },
}

for k,v in loja_comidas.items():
  loja_comidas.get(k)['valor']*1.2 
print(loja_comidas)

loja_comidas.update({'Mexerica': 4.00})
print(loja_comidas,'#Mexirica adicionada')

for chave, valor in loja_comidas.items():
  print(f"key:{chave}: value:'{valor}")

loja_comidas.pop('maca verde')
print(loja_comidas, '#Maca verde removida')

