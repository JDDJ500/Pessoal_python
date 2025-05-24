import time
import random
import os
from math import ceil
import json
from datetime import datetime

inimigos = {
    "Zombie sangrento": {"Classe": "Morto-Vivo"},
    "Caçador de almas": {"Classe": "Fantasma"},
    "Mutante descontrolado": {"Classe": "Morto-Vivo"},
    "Ekron, o Deformado": {"Classe": "Guerreiro"},
    "Thornak, o Sussurrante": {"Classe": "Fantasma"},
    "Zeltris, o colecionador": {"Classe": "Guerreiro"}
    }

itens = ["Espada de madeira", "Espada de pedra", "Espada de ferro"]

class Inimigo:
    def __init__(self, nome):
        self.enemy_nome = nome
        self.enemy_maxvida = 10
        self.enemy_vida = 10
        self.enemy_dano = 2
        self.enemy_expdrop = random.randint(2,3)
        self.enemy_golddrop = random.randint(5,15)
        self.enemy_multiplicador = 0.0

    def pocao_aleatoria(self):
        num = int(random.random()*10)
        if num > 5:
            return 1
        else:
            return 2

    def drop(self, jogador):
        if random.randint(0,100) < 30:
            talvez_pocao = 1
        else:
            talvez_pocao = 0
        
        num = random.randint(0, 3)
        if random.random() < 0.1:
            if num == 0:
                jogador.player_inventario['itens']["Espada de madeira"]['quantidade'] += 1
            else:
                jogador.adicionar_item(itens[num], random.randint(2,4))


        valor_drop = ceil(self.enemy_golddrop + (self.enemy_golddrop*self.enemy_multiplicador))
        pocao_tipo = self.pocao_aleatoria()

        jogador.player_receber_drops(valor_drop, self.enemy_expdrop, talvez_pocao, pocao_tipo, self)
    
    def enemy_status(self):
        print(f"Nome: {self.enemy_nome} | Vida: {self.enemy_vida} | Dano: {self.enemy_dano}")
        return
    
    def enemy_estado(self):
        if self.enemy_vida <= 0:
            print("O inimigo foi derrotado!")
            return str("morto")
        
    def enemy_receber_dano(self, dano):
        self.enemy_vida -= dano

class Morto_Vivo(Inimigo):
    def __init__(self, nome):
        super().__init__(nome)
        self.enemy_nome = nome
        self.enemy_maxvida = 7
        self.enemy_vida = 7
        self.enemy_dano = 2
        self.enemy_expdrop = random.randint(1,3)
        self.enemy_golddrop = random.randint(5,15)
        self.enemy_multiplicador = 0.0
    
    def drop(self, jogador):
        if random.randint(0,100) < 30:
            talvez_pocao = 1
        else:
            talvez_pocao = 0
        
        num = random.randint(0, 3)
        if random.random() < 0.1:
            if num == 0:
                jogador.player_inventario['itens']["Espada de madeira"]['quantidade'] += 1
            else:
                jogador.adicionar_item(itens[num], random.randint(2,4))


        valor_drop = ceil(self.enemy_golddrop + (self.enemy_golddrop*self.enemy_multiplicador))
        pocao_tipo = self.pocao_aleatoria()

        jogador.player_receber_drops(valor_drop, self.enemy_expdrop, talvez_pocao, pocao_tipo, self)
    
    def enemy_status(self):
        print(f"Nome: {self.enemy_nome} | Vida: {self.enemy_vida} | Dano: {self.enemy_dano} | Classe: Morto-Vivo")
        return
    
    def enemy_estado(self):
        if self.enemy_vida <= 0 or self.enemy_vida == 0:
            print("O inimigo foi derrotado!")
            return str("morto")
        
    def enemy_receber_dano(self, dano):
        self.enemy_vida -= dano

class Fantasma(Inimigo):
    def __init__(self, nome):
        super().__init__(nome)
        self.enemy_nome = nome
        self.enemy_maxvida = 10
        self.enemy_vida = 10
        self.enemy_dano = 2
        self.enemy_expdrop = random.randint(2,3)
        self.enemy_golddrop = random.randint(5,15)
        self.enemy_multiplicador = 0.0
    
    def drop(self, jogador):
        if random.randint(0,100) < 30:
            talvez_pocao = 1
        else:
            talvez_pocao = 0
        
        num = random.randint(0, 3)
        if random.random() < 0.1:
            if num == 0:
                jogador.player_inventario['itens']["Espada de madeira"]['quantidade'] += 1
            else:
                jogador.adicionar_item(itens[num], random.randint(2,4))


        valor_drop = ceil(self.enemy_golddrop + (self.enemy_golddrop*self.enemy_multiplicador))
        pocao_tipo = self.pocao_aleatoria()

        jogador.player_receber_drops(valor_drop, self.enemy_expdrop, talvez_pocao, pocao_tipo, self)
    
    def enemy_status(self):
        print(f"Nome: {self.enemy_nome} | Vida: {self.enemy_vida} | Dano: {self.enemy_dano} | Classe: Fantasma")
        return
    
    def enemy_estado(self):
        if self.enemy_vida <= 0 or self.enemy_vida == 0:
            print("O inimigo foi derrotado!")
            return str("morto")
        
    def enemy_receber_dano(self, dano):
        self.enemy_vida -= dano

            

class Guerreiro(Inimigo):
    def __init__(self, nome):
        super().__init__(nome)
        self.enemy_nome = nome
        self.enemy_maxvida = 15
        self.enemy_vida = 15
        self.enemy_dano = 3
        self.enemy_expdrop = random.randint(2,4)
        self.enemy_golddrop = random.randint(5,20)
        self.enemy_multiplicador = 0.0
    
    def drop(self, jogador):
        if random.randint(0,100) < 30:
            talvez_pocao = 1
        else:
            talvez_pocao = 0
        
        num = random.randint(0, 3)
        if random.random() < 0.1:
            if num == 0:
                jogador.player_inventario['itens']["Espada de madeira"]['quantidade'] += 1
            else:
                jogador.adicionar_item(itens[num], random.randint(2,4))


        valor_drop = ceil(self.enemy_golddrop + (self.enemy_golddrop*self.enemy_multiplicador))
        pocao_tipo = self.pocao_aleatoria()

        jogador.player_receber_drops(valor_drop, self.enemy_expdrop, talvez_pocao, pocao_tipo, self)
    
    def enemy_status(self):
        print(f"Nome: {self.enemy_nome} | Vida: {self.enemy_vida} | Dano: {self.enemy_dano} | Classe: Guerreiro")
        return
    
    def enemy_estado(self):
        if self.enemy_vida <= 0 or self.enemy_vida == 0:
            print("O inimigo foi derrotado!")
            return str("morto")
        
    def enemy_receber_dano(self, dano):
        self.enemy_vida -= dano

class Jogador:
    def __init__(self, nome):
        self.player_nome = nome
        self.player_vida = 10
        self.player_maxvida = 10
        self.player_mana = 10
        self.player_maxmana = 10
        self.player_golds = 0
        self.player_exp = 0
        self.player_maxexp = 10
        self.player_pocoes = 0
        self.player_nivel = 1
        self.player_dano = 2
        self.player_precopocao = 10
        self.player_pocaovida = 0
        self.player_pocaomana = 0
        self.player_armaequipada = None
        self.player_danoarma = 2
        self.player_armas = 1
        self.player_inventario = {
        'itens': { 
            0: {'nome': 'espada de madeira', 'quantidade': 1, 'dano': 2}
        },
        'dinheiro':{
            'ouro': {'quantidade': 0},
            'prata': {'quantidade': 0},
            'bronze': {'quantidade': 0},
            'brita': {'quantidade': 0}
        },
        'poções':{
            'poção de vida': {'quantidade': 0},
            'poção de mana': {'quantidade': 0},
            'poção de sorte': {'quantidade': 0}
        }}

    def para_dicionario(self):
        return {
            'nome': self.player_nome,
            'vida': self.player_vida,
            'maxvida': self.player_maxvida,
            'mana': self.player_mana,
            'maxmana': self.player_maxmana,
            'golds': self.player_golds,
            'exp': self.player_exp,
            'maxexp': self.player_maxexp,
            'nivel': self.player_nivel,
            'dano': self.player_dano,
            'pocaovida': self.player_pocaovida,
            'pocaomana': self.player_pocaomana,
            'armaequipada': self.player_armaequipada,
            'danoarma': self.player_danoarma,
            'inventario': self.player_inventario
            }

    @classmethod
    def do_dicionario(cls, data):
        jogador = cls(data['nome'])
        jogador.player_vida = data['vida']
        jogador.player_maxvida = data['maxvida']
        jogador.player_mana = data['mana']
        jogador.player_maxmana = data['maxmana']
        jogador.player_golds = data['golds']
        jogador.player_exp = data['exp']
        jogador.player_maxexp = data['maxexp']
        jogador.player_nivel = data['nivel']
        jogador.player_dano = data['dano']
        jogador.player_pocaovida = data['pocaovida']
        jogador.player_pocaomana = data['pocaomana']
        jogador.player_armaequipada = data['armaequipada']
        jogador.player_danoarma = data['danoarma']
        jogador.player_inventario = data['inventario']
        return jogador 
    
    def equipar_arma(self, id_arma):
        if id_arma in self.player_inventario['itens']:
            if self.player_inventario['itens'][id_arma]['quantidade'] > 0:
                self.player_armaequipada = id_arma
                self.player_danoarma = self.player_inventario['itens'][id_arma]['dano']
                print(f"{self.player_inventario['itens'][id_arma]['nome']} equipada!")
                return True
        print(f"Você não possui esta arma no inventário!")
        return False

    def converter_moeda(self, gold):
        while True:
            if gold >= 161:
                gold -= 161

                ouro = 161 // 100
                r_ouro = 161 % 100
                prata = r_ouro // 50
                r_prata = r_ouro % 50
                bronze = r_prata // 10
                r_bronze = r_prata % 10
                brita = r_bronze
                
                self.player_inventario['dinheiro']['ouro']['quantidade'] += ouro
                self.player_inventario['dinheiro']['prata']['quantidade'] += prata
                self.player_inventario['dinheiro']['bronze']['quantidade'] += bronze
                self.player_inventario['dinheiro']['brita']['quantidade'] += brita
                
            elif gold <= 161:
                ouro = gold // 100
                r_ouro = gold % 100
                prata = r_ouro // 50
                r_prata = r_ouro % 50
                bronze = r_prata // 10
                r_bronze = r_prata % 10
                brita = r_bronze
                
                self.player_inventario['dinheiro']['ouro']['quantidade'] += ouro
                self.player_inventario['dinheiro']['prata']['quantidade'] += prata
                self.player_inventario['dinheiro']['bronze']['quantidade'] += bronze
                self.player_inventario['dinheiro']['brita']['quantidade'] += brita
                self.player_golds = 0
                break
        return
    
    def adicionar_item(self, nome, dano):
        novo_id = max(self.player_inventario['itens'].keys()) + 1 if self.player_inventario['itens'] else 0
        self.player_inventario['itens'][novo_id] = {
            'nome': nome,
            'quantidade': 1,
            'dano': dano
        }
        self.player_armas += 1
        return novo_id
        
    
    def player_estado(self):

        if self.player_vida <= 0 or self.player_vida == 0:
            print("Você morreu, seus atributos foram reduzidos pela metade!")
            self.player_vida = int(self.player_maxvida/2)
            self.player_mana = int(self.player_maxmana/2)
            self.player_golds = int(self.player_golds/2)
            print(self.player_status())
            time.sleep(2)
            limpar()
            print("Tempo até o spaw:")
            for i in range(10):
                print(f"\r{i+1}/10", end="", flush=True)
                time.sleep(1)
                
            return str("morto")
    
    def player_receber_drops(self, gold, exp, pocao, tipo, enemy):
        self.player_golds += gold
        self.player_exp += exp
        if pocao > 0:
            self.player_pocoes += pocao
            if tipo == 1:
                self.player_pocaovida += 1
            elif tipo == 2:
                self.player_pocaomana += 1
        else:
            self.player_pocoes += pocao
        
        if random.randint(0,10) >= 5:
            arma = 0
        else:
            arma = 1
            self.player_inventario['itens'][0]['quantidade'] += 1

        print(f"\n\nParabens, Você recebeu; Golds: {gold} | Xp: {exp} | Poção: {pocao} | Arma: {arma}\n")
        self.player_up_atributos(enemy)

        time.sleep(4)
    def player_up_atributos(self, enemy):
        while self.player_exp >= self.player_maxexp:
            self.player_nivel += 1
            self.player_exp -= self.player_maxexp
            self.player_maxexp = int(self.player_maxexp * 1.1)
            self.player_maxvida = int(self.player_maxvida * 1.1)
            self.player_vida = self.player_maxvida
            self.player_maxmana = int(self.player_maxmana * 1.1)
            self.player_mana = self.player_maxmana
            self.player_dano = ceil((self.player_maxvida//self.player_nivel)*0.5)
            enemy.enemy_maxvida = int(enemy.enemy_maxvida * 1.1)
            enemy.enemy_vida = enemy.enemy_maxvida
            enemy.enemy_dano = ceil((enemy.enemy_maxvida//self.player_nivel)*0.7)
            enemy.enemy_multiplicador += 0.1
            print(f"\nParabéns {self.player_nome}! Você subiu para o nível {self.player_nivel}!")
    
    def player_receber_dano(self, dano):
        self.player_vida -= dano
    
    
    def troca_pocoes(self):
        while True:
            limpar()
            self.player_status()
            print(f"converter poções")
            print(f"{self.player_pocaovida} poções de vida")
            print(f"{self.player_pocaomana} poções de mana")
            print("Converter")
            print("1 - MANA -> VIDA")
            print("2 - VIDA -> MANA")
            print("3 - Voltar")
            entrada = input("> ")

            if entrada == "1":
                if self.player_pocaomana == 0:
                    print("Você não tem poções de mana para converter !!")
                    time.sleep(2)
                else:
                    self.player_pocaomana -= 1
                    self.player_pocaovida += 1
                    for i in range(4):
                        print(f"\rConvertendo"+"."*i, end="", flush=True)
                        time.sleep(1)
                    print("\nconverção bem sucedida !!")
                    time.sleep(2)
            elif entrada == "2":
                if self.player_pocaovida == 0:
                    print("Você não tem poções de vida para converter !!")
                    time.sleep(2)
                else:
                    self.player_pocaovida -= 1
                    self.player_pocaomana += 1
                    for i in range(4):
                        print(f"\rConvertendo"+"."*i, end="", flush=True)
                        time.sleep(1)
                    print("\nconverção bem sucedida !!")
                    time.sleep(2)

    def loja(self):
        limpar()
        print("-"*10,"LOJA","-"*10)
        print("\n1 - poção de cura\n2 - poção de mana\n3 - voltar")
        entrada = input("> ")
        ouro = self.player_inventario["dinheiro"]["ouro"]["quantidade"]
        prata = self.player_inventario["dinheiro"]["prata"]["quantidade"]
        brita = self.player_inventario["dinheiro"]["brita"]["quantidade"]
        bronze = self.player_inventario["dinheiro"]["bronze"]["quantidade"]
        dinheiro_total = (ouro * 100) + (prata * 10) + brita
        def converter_nota_gasto(gasto):
            while True:
                if gasto >= 161:
                    gasto -= 161
                    ouro1 = 161 // gasto
                    r_ouro1 = 161 % gasto
                    prata1 = r_ouro1 // 50
                    r_prata1 = r_ouro1 % 50
                    bronze1 = r_prata1 // 10
                    r_bronze1 = r_prata1 % 10
                    brita1 = r_bronze1
                else:
                    ouro1 = gasto // 161
                    r_ouro1 = gasto % 161
                    prata1 = r_ouro1 // 50
                    r_prata1 = r_ouro1 % 50
                    bronze1 = r_prata1 // 10
                    r_bronze1 = r_prata1 % 10
                    brita1 = r_bronze1
                    gasto = 0

                    self.player_inventario["dinheiro"]["ouro"]["quantidade"] -= ouro1
                    self.player_inventario["dinheiro"]["prata"]["quantidade"] -= prata1
                    self.player_inventario["dinheiro"]["bronze"]["quantidade"] -= bronze1
                    self.player_inventario["dinheiro"]["brita"]["quantidade"] -= brita1
                    break
            return

        def confirmar(entrada):
            if dinheiro_total <= 9:
                print("Você não tem dinheiro suficiente !!")
                return
            
            print(""*10,"CONFIRME",""*10)
            print("Quantas deseja comprar?")
            entry_qtd = int(input("> "))
            print(f"\nA poção custa {10 * entry_qtd} golds, Tem certeza?")
            print("\n1 - Comprar\n2 - Desistir")
            enter = input("> ")
            total = 10 * entry_qtd

            if entrada == "1":
                if enter == "1":
                    if brita >= 10 * entry_qtd:
                        self.player_pocaovida += entry_qtd
                        converter_nota_gasto(total)
                        print("Compra feita com sucesso!")
                        time.sleep(2)
                        return
                    else:
                        if bronze*10 >= 10 * entry_qtd:
                            self.player_pocaovida += entry_qtd
                            converter_nota_gasto(total)
                            print("Compra feita com sucesso!")
                            time.sleep(2)
                            return
                        else:
                            if prata*50 >= 10 * entry_qtd:
                                self.player_pocaovida += entry_qtd
                                converter_nota_gasto(total)
                                print("Compra feita com sucesso!")
                                time.sleep(2)
                                return
                            else:
                                if ouro*100 >= 10* entry_qtd:
                                    self.player_pocaovida += entry_qtd
                                    converter_nota_gasto(total)
                                    self.converter_moeda(90)
                                    print("Compra feita com sucesso!")
                                    time.sleep(2)
                                    return

                elif enter == "2":
                    return
                else:
                    print("Resposta invalida!")
                    time.sleep(2)


            elif entrada == "2":
                if enter == "1":
                    if brita >= 10 * entry_qtd:
                        self.player_pocaomana += entry_qtd
                        converter_nota_gasto(total)
                        print("Compra feita com sucesso!")
                        time.sleep(2)
                        return
                    else:
                        if bronze*10 >= 10 * entry_qtd:
                            self.player_pocaomana += entry_qtd
                            converter_nota_gasto(total)
                            print("Compra feita com sucesso!")
                            time.sleep(2)
                            return
                        else:
                            if prata*50 >= 10 * entry_qtd:
                                self.player_pocaomana += entry_qtd
                                converter_nota_gasto(total)
                                print("Compra feita com sucesso!")
                                time.sleep(2)
                                return
                            else:
                                if ouro*100 >= 10* entry_qtd:
                                    self.player_pocaomana += entry_qtd
                                    converter_nota_gasto(total)
                                    self.converter_moeda(90)
                                    print("Compra feita com sucesso!")
                                    time.sleep(2)
                                    return

        if entrada == "1":
            if brita >= 10 or prata >= 1 or ouro >= 1:
                confirmar(entrada)
                limpar()
            else:
                print("Dinheiro insuficiente!")
                time.sleep(2)
                limpar()

        elif entrada == "2":
            if brita >= 10 or prata >= 1 or ouro >= 1:
                confirmar(entrada)
                limpar()
            else:
                print("Dinheiro insuficiente!")
                time.sleep(2)
                limpar()
        
        elif entrada == "3":
            limpar()
            print("Volte sempre .-.")
            time.sleep(3)
            return

        else:
            print("Resposta invalida!")
            time.sleep(2)
            limpar()
    
    def player_status(self):
        if self.player_armaequipada is None:
            print(f"Vida: {self.player_vida}/{self.player_maxvida} | Mana: {self.player_mana}/{self.player_maxmana} | Britas: {self.player_inventario['dinheiro']['brita']['quantidade']} | Dano: {self.player_dano} | Poções - Vida: {self.player_pocaovida} - Mana: {self.player_pocaomana} | Nivel: {self.player_nivel}({self.player_exp}/{self.player_maxexp})")
        else:
            print(f"Vida: {self.player_vida}/{self.player_maxvida} | Mana: {self.player_mana}/{self.player_maxmana} | Britas: {self.player_inventario['dinheiro']['brita']['quantidade']} | Dano: {self.player_dano} +{self.player_danoarma} | Poções - Vida: {self.player_pocaovida} - Mana: {self.player_pocaomana} | Nivel: {self.player_nivel}({self.player_exp}/{self.player_maxexp})")
        
    def curar_atributos(self):
        limpar()
        print("curar -> 1 - Vida | 2 - Mana | 3 - Voltar")
        entrada = input(">")
        
        if entrada == "1":
            if self.player_pocaovida == 0 and self.player_vida == self.player_maxvida:
                print("Você nâo tem poções, mas sua vida está cheia!")
                time.sleep(2)
                return
            
            elif self.player_pocaovida >= 1 and self.player_vida == self.player_maxvida:
                print("Você tem poções, mas sua vida está cheia!")
                time.sleep(2)
                return
            
            elif self.player_vida < self.player_maxvida and self.player_pocaovida == 0:
                print("Você não tem poções para usar!")
                time.sleep(2)
                return
            
            elif self.player_vida < self.player_maxvida and self.player_pocaovida >= 1:
                vida_a_curar = self.player_maxvida - self.player_vida
                if vida_a_curar <=3:
                    self.player_vida = self.player_maxvida
                    self.player_pocaovida -= 1
                    return
                
                else:
                    self.player_vida += random.randint(3,4)
                    self.player_pocaovida -= 1
                    return
        
        elif entrada == "2":
            if self.player_pocaomana == 0 and self.player_mana == self.player_maxmana:
                print("Você nâo tem poções, mas sua mana está cheia!")
                time.sleep(2)
                return
            
            elif self.player_pocaomana >= 1 and self.player_mana == self.player_maxmana:
                print("Você tem poções, mas sua mana está cheia!")
                time.sleep(2)
                return
            
            elif self.player_mana < self.player_maxmana and self.player_pocaomana == 0:
                print("Você não tem poções para usar!")
                time.sleep(2)
                return
            
            elif self.player_mana < self.player_maxmana and self.player_pocaomana >= 1:
                vida_a_curar = self.player_maxmana - self.player_mana
                if vida_a_curar <=4:
                    self.player_mana = self.player_maxmana
                    self.player_pocaomana -= 1
                    return
                
                else:
                    self.player_mana += 4
                    self.player_pocaomana -= 1
                    return
        elif entrada == "3":
            limpar()
            return
        
        else:
            print(f"Resposta invalida!")
            time.sleep(2)
    
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar():
    while True:
        limpar()
        print(f"Bem-vindo ao rpg JDFN")
        print(f"Qual será o nome do personagem?")
        entrada = input("> ")
        if entrada.lower() == "jdfn" or entrada.lower() == "":
            check = input()
            if check == ",,0,,0,,":
                jogador = Jogador(entrada)
                break
            else:
                print(f"Hmmm, Não tente usar o nome do desenvolvedor ;(")
                time.sleep(2)
        else:
            jogador = Jogador(entrada)
            break
    limpar()
    menu_opcoes(jogador)

def ataque(jogador,enemy):
    print("1 - ataque fisico | 2 - ataque magico | 3 - Desistir")
    check = input(">")
    def ataque_magico(jogador, enemy):
        print(f"1 - Bola de fogo | 2 - Espinho de gelo | 3 - Emocional Damage | 4 - Desistir")
        chance_ataque_1 = 0.3
        chance_ataque_2 = 0.75
        chance_ataque_3 = 1
        dano = ""
        entry = input("> ")
        
        if (entry == "3"):
            dano = jogador.player_dano * 3
            if random.random() <= chance_ataque_1:
                if jogador.player_mana >= (jogador.player_maxmana * 0.6):
                    enemy.enemy_vida -= dano
                    jogador.player_mana -= ceil(jogador.player_maxmana * 0.6)
                    print(f"Ataque bem sucedido !!, você causou {dano} de dano")
                    time.sleep(2)
                    return 0
                else:
                    print(f"Mana não é o suficiente !!")
                    time.sleep(2)
                    limpar()
                    return 1
            else:
                print(f'Ataque falhou')
                time.sleep(2)
                limpar()
                return 1
                
        elif (entry == "2"):
            dano = ceil(jogador.player_dano * 1.5)
            if random.random() <= chance_ataque_2:
                if jogador.player_mana >= (jogador.player_maxmana * 0.4):
                    enemy.enemy_vida -= dano
                    jogador.player_mana -= ceil(jogador.player_maxmana * 0.4)
                    print(f"Ataque bem sucedido !!, você causou {dano} de dano")
                    time.sleep(2)
                    return 0
                else:
                    print(f"Mana não é o suficiente !!")
                    time.sleep(2)
                    limpar()
                    return 1
            else:
                print(f'Ataque falhou')
                time.sleep(2)
                limpar()
                return 1
            
        elif (entry == "1"):
            dano = ceil(jogador.player_dano * 2)
            if random.random() <= chance_ataque_3:
                if jogador.player_mana >= (jogador.player_maxmana * 0.2):
                    enemy.enemy_vida -= dano
                    jogador.player_mana -= ceil(jogador.player_maxmana * 0.2)
                    print(f"Ataque bem sucedido !!, você causou {dano} de dano")
                    time.sleep(2)
                    return 0
                else:
                    print(f"Mana não é o suficiente !!")
                    time.sleep(2)
                    limpar()
                    return 1
            else:
                print(f'Ataque falhou')
                time.sleep(2)
                limpar()
                return 1
            
        elif (entry == "4"):
            return 2
            
        
    if check == "1":
        if jogador.player_armaequipada is not None:
            arma_nome = jogador.player_inventario['itens'][jogador.player_armaequipada]['nome']
            dano = jogador.player_dano + jogador.player_danoarma
            enemy.enemy_receber_dano(dano)
            jogador.player_receber_dano(enemy.enemy_dano)
            print(f"Você atacou com {arma_nome}!")
            time.sleep(2)
        else:
            if enemy.enemy_nome == "Caçador de almas" or enemy.enemy_nome == "Thornak, o Sussurrante":
                dano = jogador.player_dano
                jogador.player_receber_dano(enemy.enemy_dano)
                print(f"Você não pode acertar um fantasma com as mãos !!\nVocê recebeu {dano} de dano")
                time.sleep(2)
            else:
                dano = jogador.player_dano
                enemy.enemy_receber_dano(dano)
                jogador.player_receber_dano(enemy.enemy_dano)
                print("Você atacou com seus punhos!")
                time.sleep(2)
        
        if enemy.enemy_estado() == "morto":
            return
        elif jogador.player_estado() == "morto":
            return
    elif check == "2":
        ataqueeee = ataque_magico(jogador,enemy)
        if ataqueeee == 0:
            enemyDano = enemy.enemy_dano
            jogador.player_receber_dano(enemyDano)
            if enemy.enemy_estado() == "morto" or jogador.player_estado() == "morto":
                return
            return
        elif ataqueeee == 1:
            enemyDano = enemy.enemy_dano
            jogador.player_receber_dano(enemyDano)
            if enemy.enemy_estado() == "morto":
                return
            elif jogador.player_estado() == "morto":
                return
        elif ataqueeee == 2:
            pass
    elif check == "3":
        return

def masmorra(jogador):
    limpar()
    print("Inimigos\n")
    nume = random.randint(0,6)
    if nume == 0:
        nume = "Zombie sangrento"
    elif nume == 2:
        nume = "Caçador de almas"
    elif nume == 3:
        nume = "Mutante descontrolado"
    elif nume == 4:
        nume = "Ekron, o Deformado"
    elif nume == 5:
        nume = "Thornak, o Sussurrante"
    else:
        nume = "Zeltris, o colecionador"

    for chave, valor in inimigos.items():
        for conteudo in valor.items():
            if chave == nume:
                print(f"{chave} - selecionado")
                classe = inimigos[nume]['Classe']
                if classe == "Morto-Vivo":
                    enemy = Morto_Vivo(nume)
                elif classe == "Fantasma":
                    enemy = Fantasma(nume)
                elif classe == "Guerreiro":
                    enemy = Guerreiro(nume)
                
            else:
                print(f"{chave} - {conteudo}")
    if classe == "Morto-Vivo":
        print(f"\nEle se levanta, o cheiro de carne podre domina o lugar\nPreparece para enfrentar o {nume}\n")
    elif classe == "Fantasma":
        print(f"\nAtravés das paredes ele está presente, um arrepio percorre sua espinha\nPreparece para enfrentar o {nume}\n")
    else:
        print(f"\nO chão está em tremores, uma presença incrivel domina o lugar\nPreparece para enfrentar o {nume}\n")

    print(f"precione enter")
    input()
    while True:
        num = int(random.random()*10)
        if jogador.player_vida < jogador.player_maxvida // 2:
            if jogador.player_vida < 3:
                if num < 6:
                    jogador.player_vida += 1
            else:
                if num < 4:
                    jogador.player_vida += 1

        limpar()
        print("-"*8,"MASMORRA","-"*8)
        print(f"O inimigo apareceu o que você vai fazer?\n")
        print("-"*3,"INIMIGO","-"*3)
        enemy.enemy_status()
        print("")
        print("-"*3,f"{jogador.player_nome}","-"*3)
        jogador.player_status()
        print(f"\n1 - Atacar\n2 - Curar\n3 - Fugir")
        entrada = input("> ")
        if entrada == "1":
            ataque(jogador, enemy)
            if enemy.enemy_estado() == "morto":
                if jogador.player_estado() == "morto":
                    enemy.drop(jogador)
                    return
                else:
                    enemy.drop(jogador)
                    return
            elif jogador.player_estado() == "morto":
                return
            limpar()
        elif entrada == "2":
            jogador.curar_atributos()

        elif entrada == "3":
            enemyDano = enemy.enemy_dano
            sorteio = random.randint(0,10)
            if sorteio < 3:
                jogador.player_receber_dano(enemyDano)
                print(f"Fuga concluida, dano recebido {enemyDano}")
                time.sleep(1)
            else:
                print(f"Fuga concluida, dano recebido 0")
                time.sleep(1)
            return
        
        else:
            print(f"Resposta invalida!")
            time.sleep(2)

def salvar_jogo(jogador):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo = f"save_{agora}.json"
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        dados = jogador.para_dicionario()
        dados['metadata'] = {
            'data_save': agora,
            'versao_jogo': '1.0'
        }
        json.dump(dados, f, indent=4)
    print(f"Jogo salvo como '{arquivo}'!")
    time.sleep(2)


def listar_saves():
    saves = [f for f in os.listdir() if f.endswith('.json')]
    if not saves:
        print("Nenhum save encontrado.")
        return None
    print("Saves disponíveis:")
    for i, save in enumerate(saves, 1):
        print(f"{i} - {save}")
    print(f"{len(saves)+1} - Voltar")
    
    escolha = input("> ")
    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(saves):
            return saves[escolha-1]
        else:
            return None
    except ValueError:
        return None

def carregar_jogo():
    arquivo = listar_saves()
    if not arquivo:
        return None

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)

        # Validação básica dos dados
        required_keys = ['nome', 'vida', 'inventario', 'dano', 'nivel']
        if not all(key in dados for key in required_keys):
            print("Save incompleto ou inválido.")
            return None

        jogador = Jogador.do_dicionario(dados)
        print(f"Jogo carregado: {arquivo}")
        time.sleep(2)
        return jogador

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except json.JSONDecodeError:
        print("Save corrompido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    time.sleep(2)
    return None

def ler_inventario(inventario):
    limpar()
    for chave, valor in inventario.items():
        print(f"\nCategoria: {chave}\n")
        if chave == 'itens':
            for id_item, detalhes in valor.items():
                print(f"ID: {id_item} - {detalhes['nome']}: Quantidade: {detalhes['quantidade']}, Dano: +{detalhes['dano']}")
        else:
            for itens, detalhes in valor.items():
                for quantidade, numero in detalhes.items():
                    print(f"- {itens} - {quantidade}: {numero}")
    print("\nAperte Enter para voltar\n")
    input()

def equipamento(jogador):
    limpar()
    print(f"\nEquipar Arma")
    print(f"1 - Equipar | 2 - Desequipar | 3 - Voltar")
    check = input("> ")
    
    if check == "1":
        print("\nArmas disponíveis no inventário:\n")
        for id_arma, dados in jogador.player_inventario['itens'].items():
            print(f"{id_arma} - {dados['nome']}: {dados['quantidade']} (Dano: +{dados['dano']})")
        
        try:
            arma_escolhida = int(input("Digite o ID da arma para equipar: "))
            jogador.equipar_arma(arma_escolhida)
        except ValueError:
            print("ID inválido! Digite um número.")
        time.sleep(2)
        return
        
    elif check == "2":
        if jogador.player_armaequipada is None:
            print("Você não tem nenhum equipamento sendo utilizado!")
            time.sleep(2)
            return
        else:
            jogador.player_armaequipada = None
            jogador.player_danoarma = 0
            print("Arma desequipada com sucesso!")
            time.sleep(2)
            return
            
    elif check == "3":
        return

def inventario(jogador):
    limpar()
    print("-"*4,"INVENTARIO","-"*4)
    print("1 - Ver Inventario | 2 - Equipamento | 3 - Trocar poções | 4 - Voltar")
    inputt = input("> ")
    if inputt == "1":
        ler_inventario(jogador.player_inventario)
        limpar()
        return
    elif inputt == "2":
        equipamento(jogador)
        limpar()
    elif inputt == "3":
        jogador.troca_pocoes()
        limpar
    elif inputt == "4":
        return


def menu_opcoes(jogador):    
    while True:
        limpar()
        jogador.converter_moeda(jogador.player_golds)
        print("-"*3,f"{jogador.player_nome}","-"*3)
        jogador.player_status()
        print("-"*10,"MENU","-"*10)
        print("\n1 - MASMORRA\n2 - LOJA\n3 - INVENTARIO")
        print("4 - SALVAR JOGO\n5 - CARREGAR JOGO\n6 - SAIR")
        
        entrada = input("> ")
        if entrada == "1":
            masmorra(jogador)
        elif entrada == "2":
            jogador.loja()
        elif entrada == "3":
            inventario(jogador)
        elif entrada == "4":
            salvar_jogo(jogador)
        elif entrada == "5":
            novo_jogador = carregar_jogo()
            if novo_jogador:
                jogador = novo_jogador
        elif entrada == "6":
            print("Volte Sempre ._.")
            time.sleep(1)
            quit()
        elif entrada == "?":
            jogador.player_golds = 999999
        else:
            print("Opção inválida!")
            time.sleep(1)


if __name__ == "__main__":
    iniciar()
