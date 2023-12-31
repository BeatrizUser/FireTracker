# Generated by Django 4.0.4 on 2022-08-19 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_do_Cliente', models.CharField(max_length=100, verbose_name='Nome')),
                ('Data_Aniversario', models.DateField(default='')),
                ('Tipo_Pessoa', models.CharField(choices=[('CNPJ', 'Pessoa Jurídica'), ('CPF', 'Pessoa Física')], max_length=4)),
                ('CNPJ_CPF', models.CharField(max_length=200)),
                ('Regiao', models.CharField(max_length=200)),
                ('Inscricao_Estadual', models.CharField(max_length=200)),
                ('Inscricao_Municipal', models.CharField(max_length=200)),
                ('Contato', models.CharField(max_length=200)),
                ('Inscricao_Suframa', models.CharField(max_length=200)),
                ('Desconto', models.CharField(max_length=200)),
                ('Vendedor', models.CharField(max_length=200)),
                ('Reter_iss', models.CharField(max_length=200)),
                ('Guia_pg', models.CharField(max_length=200)),
                ('Data_Atualiazacao', models.CharField(max_length=200)),
                ('Ramo_Atividade', models.CharField(max_length=200)),
                ('Tipo_Empresa', models.CharField(max_length=200)),
                ('Desc_Nat_Juridica', models.CharField(max_length=200)),
                ('Nome_Fantasia', models.CharField(max_length=200)),
                ('Descricao_CNAE', models.CharField(max_length=200)),
                ('Situacao_cadastral', models.CharField(max_length=200)),
                ('Data_abertura', models.CharField(max_length=200)),
                ('Data_Pesquisa', models.CharField(max_length=200)),
                ('Observacoes', models.CharField(max_length=2000, verbose_name='Observações')),
                ('Telefones_emails', models.CharField(max_length=200)),
                ('Cadastrado_em', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['Nome_do_Cliente'],
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fornecedor', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_fantasia', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('data_aniversario', models.DateField(default='')),
                ('responsavel', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=200)),
                ('inscricao_estadual', models.CharField(max_length=200)),
                ('pix_1', models.CharField(max_length=200)),
                ('pix_2', models.CharField(max_length=200)),
                ('Observacoes', models.CharField(max_length=2000)),
                ('Cadastrado_em', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['nome_fornecedor'],
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_do_Servico', models.CharField(max_length=100)),
                ('Csit_Tributaria', models.CharField(max_length=100)),
                ('Patrimonio_NCM', models.CharField(max_length=100)),
                ('Cest', models.CharField(max_length=100)),
                ('Numero_Serie', models.CharField(max_length=100)),
                ('Pedidos', models.CharField(max_length=100)),
                ('Validade', models.CharField(max_length=100)),
                ('Pendência', models.CharField(max_length=100)),
                ('Preco_uni', models.CharField(max_length=100)),
                ('Uni_medida', models.CharField(max_length=100)),
                ('Data_Cadatro', models.CharField(max_length=100)),
                ('Data_Atualizacao', models.CharField(max_length=100)),
                ('Descricao', models.CharField(max_length=100)),
                ('Numero_Certificado', models.CharField(max_length=100)),
                ('Certificado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_de_Endereço', models.CharField(choices=[('Faturamento', 'Endereço de Faturamento'), ('Entrega', 'Endereço de Entrega'), ('Comercial', 'Endereço da Empresa')], max_length=200)),
                ('Logradouro', models.CharField(max_length=200)),
                ('Numero', models.CharField(max_length=6)),
                ('Complemento', models.CharField(max_length=200)),
                ('Bairro', models.CharField(max_length=200)),
                ('Pais', models.CharField(default='Brasil', max_length=200)),
                ('UF', models.CharField(max_length=200)),
                ('Cidade', models.CharField(max_length=200)),
                ('CEP', models.CharField(max_length=9)),
                ('observacoes', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('Responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to='cadastro.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=200)),
                ('cargo_responsavel', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fornecedor_nome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='cadastro.fornecedor')),
            ],
        ),
    ]
