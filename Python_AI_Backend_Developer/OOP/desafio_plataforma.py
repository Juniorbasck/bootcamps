# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone(plano):
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
    
    def fazer_chamada(self):
      
      if self.verificar_saldo():
        saldo = self.deduzir_saldo()
        return f"Chamada para {destinatario} realizada com sucesso. Saldo: {saldo}"
      
      return "Saldo insuficiente para fazer a chamada."
      
      def verificar_saldo(self):
        
        custo = self.custo_chamada()
        
        if custo > saldo:
           return False
        
      def custo_chamada(self):
        valor_chamada = duracao * 0.10
        
        return valor_chamada
        
      def deduzir_saldo(self):
        valor_chamada = self.custo_chamada()
        
        Saldo = valor_chamada - Saldo
        return saldo


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
