import pyautogui as pg, pandas as pd, numpy, openpyxl
import time

# link fictício: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# 1. acessar o site

pg.PAUSE = 1 # a cada comando espera 2 segundos
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # colocando o link numa variável para economizar tempo

pg.press("win")
pg.write("edge")
pg.press("enter")
pg.write(link)
pg.press("enter")

time.sleep(2)

 # 2. fazer login

pg.click(x=822, y=492)
pg.write("dan@gmail.com")

pg.press("tab")
pg.write("1234")

pg.click(x=950, y=687)

time.sleep(2)

# 3. importar base de dados

tabela = pd.read_csv("produtos.csv")
#print(tabela)

# 4. cadastrar um produto

for linha in tabela.index:    # para cada linha da minha tabela
    
    pg.scroll(5000)
    pg.click(x=689, y=350)
    
    #codigo
    #codigo = tabela.loc[linha, coluna]
    codigo = tabela.loc[linha,"codigo"]
    pg.write(codigo)
    pg.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pg.write(marca)
    pg.press("tab")

    #tipo 
    tipo = tabela.loc[linha, "tipo"]
    pg.write(tipo)
    pg.press("tab")

    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pg.write(str(categoria))
    pg.press("tab")

    #preco_unitario
    preco = tabela.loc[linha,"preco_unitario"]
    pg.write(str(preco))
    pg.press("tab")

    #custo
    custo = tabela.loc[linha,"custo"]
    pg.write(str(custo))
    pg.press("tab")

    #obs
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pg.write(obs)
        pg.press("tab")
    else:
        pg.press("tab")

    #enviar produto
    pg.press("enter")


# repetir até cadastrar tudo da base de dados