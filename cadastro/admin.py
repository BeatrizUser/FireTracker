from django.contrib import admin
from django import forms
from cadastro.models import Cliente, Endereco, Fornecedor, Email


class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 0
    verbose_name = 'Endereço'
    verbose_name_plural = 'Cadastro de Endereços'
    fieldsets = (
        ('Endereço', {
            'fields': [('Tipo_de_Endereço'),('Logradouro','Numero','Complemento'),('CEP','Bairro','Cidade','UF','Pais'),('Responsavel'),('observacoes')]
        }),
    )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline]
    list_display = ('Nome_do_Cliente', 'Tipo_Pessoa', 'gerar_relatorio')
    fieldsets = (
        ('Informações Gerais', {
            'fields': ['Nome_do_Cliente', 'Data_Aniversario', 'Tipo_Pessoa', 'CNPJ_CPF', 'Contato']
        }),
        ('Informações Pessoa Jurídica', {
            'fields': [('Nome_Fantasia', 'Tipo_Empresa'),('Ramo_Atividade', 'Descricao_CNAE'),('Situacao_cadastral', 'Inscricao_Estadual', 'Inscricao_Municipal'),('Desc_Nat_Juridica','Telefones_emails'),('Observacoes')],
        }),
    )

class EmailInline(admin.StackedInline):
    model = Email
    extra = 0
    verbose_name = 'Email'
    verbose_name_plural = 'Cadastro de Emails'

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    inlines = [EmailInline]

# admin.site.register(Servico)