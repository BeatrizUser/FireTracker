from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone


Sim_Nao = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
Endereco_choices = (
    ('Faturamento', 'Endereço de Faturamento'),
    ('Entrega', 'Endereço de Entrega'),
    ('Comercial', 'Endereço da Empresa'),
    )
CNPJ_CPF = (
    ('CNPJ', 'Pessoa Jurídica'),
    ('CPF', 'Pessoa Física'),
)

class Fornecedor(models.Model):
    
    nome_fornecedor = models.CharField(max_length=100, verbose_name=('Nome'))
    nome_fantasia = models.CharField(max_length=100, verbose_name=('Nome Fantasia'))
    data_aniversario = models.DateField(default='', verbose_name=('Nascimento'))
    responsavel = models.CharField(max_length = 200)
    telefone = models.CharField(max_length = 200)
    fax = models.CharField(max_length = 200)
    cnpj = models.CharField(max_length = 200, verbose_name=('CNPJ'))
    inscricao_Estadual = models.CharField(max_length = 200)

    pix_1 = models.CharField(max_length = 200)
    pix_2 = models.CharField(max_length = 200)
    
    Observacoes = models.CharField(max_length = 2000)

    Cadastrado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nome_fornecedor']
        verbose_name_plural = "Fornecedores"


    def __str__(self):
        return self.nome_fornecedor

class Email(models.Model):

    fornecedor_nome = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, related_name = 'fornecedor', blank=True, null=True)
    nome_responsavel = models.CharField(max_length = 200)
    cargo_responsavel = models.CharField(max_length = 200)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email

class Endereco(models.Model):

    Tipo_de_Endereço = models.CharField(max_length = 200, choices=Endereco_choices)
    Logradouro = models.CharField(max_length = 200)
    Numero = models.CharField(max_length = 6)
    Complemento = models.CharField(max_length = 200)
    Bairro = models.CharField(max_length = 200)
    Pais = models.CharField(max_length = 200, default='Brasil')
    UF = models.CharField(max_length = 200)
    Cidade = models.CharField(max_length = 200)
    CEP = models.CharField(max_length = 9)
    observacoes = models.CharField(max_length = 2000, verbose_name='Observações', blank=True, null=True)
    Responsavel = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name = 'responsavel', blank=True, null=True)

    def __str__(self):
        return self.Tipo_de_Endereço

class Cliente(models.Model):

# DADOS DO CLIENTE
    Nome_do_Cliente = models.CharField(max_length=100, verbose_name=('Nome'))
    Data_Aniversario = models.DateField(default='')
    Tipo_Pessoa = models.CharField(max_length=4, choices= CNPJ_CPF)
    CNPJ_CPF = models.CharField(max_length = 200)
    Regiao = models.CharField(max_length = 200)
    Inscricao_Estadual = models.CharField(max_length = 200)
    Inscricao_Municipal = models.CharField(max_length = 200)
    Contato = models.CharField(max_length = 200)
    Inscricao_Suframa = models.CharField(max_length = 200)
    Desconto = models.CharField(max_length = 200)
    Vendedor = models.CharField(max_length = 200)

# DADOS DA EMPRESA
    Reter_iss = models.CharField(max_length = 200)
    Guia_pg = models.CharField(max_length = 200)
    Data_Atualiazacao = models.CharField(max_length = 200)
    Ramo_Atividade = models.CharField(max_length = 200)
    Tipo_Empresa = models.CharField(max_length = 200)
    Desc_Nat_Juridica = models.CharField(max_length = 200)
    Nome_Fantasia = models.CharField(max_length = 200)
    Descricao_CNAE = models.CharField(max_length = 200)
    Situacao_cadastral = models.CharField(max_length = 200)
    Data_abertura = models.CharField(max_length = 200)
    Data_Pesquisa = models.CharField(max_length = 200)
    Observacoes = models.CharField(max_length = 2000, verbose_name='Observações')
    Telefones_emails = models.CharField(max_length = 200)
    Cadastrado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['Nome_do_Cliente']

    def gerar_relatorio(self):
        return mark_safe("""<a href=\"/relatorio/pdf/%s/\" target="_blank"><img src=\"/static/images/relatorio.png\" alt="Gerar Relatorio"></a>""" % self.id)

    def __str__(self):
        return self.Nome_do_Cliente

# class Servico(models.Model):
#     Nome_do_Servico = models.CharField(max_length=100)
#     Csit_Tributaria = models.CharField(max_length=100)
#     Patrimonio_NCM = models.CharField(max_length=100)
#     Cest = models.CharField(max_length=100)
#     Numero_Serie = models.CharField(max_length=100)
#     Pedidos = models.CharField(max_length=100)
#     Validade = models.CharField(max_length=100)
#     Pendência = models.CharField(max_length=100)
#     Preco_uni = models.CharField(max_length=100)
#     Uni_medida = models.CharField(max_length=100)
#     Data_Cadatro = models.CharField(max_length=100)
#     Data_Atualizacao = models.CharField(max_length=100)
#     Descricao = models.CharField(max_length=100)
#     Numero_Certificado = models.CharField(max_length=100)
#     Certificado = models.CharField(max_length=100, choices = Sim_Nao)

#     def __str__(self):
#         return self.Nome_do_Servico