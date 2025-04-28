# Automação de Criativos para Google Ads

Este projeto automatiza a geração e upload de criativos para campanhas do Google Ads, utilizando templates e logos armazenados no Google Drive.

## 🚀 Funcionalidades

- Geração automática de criativos usando templates
- Suporte a múltiplos idiomas e países
- Integração com Google Drive para templates e logos
- Integração com Google Sheets para gerenciamento de campanhas
- Upload automático para o Google Ads
- Suporte a formatos PNG e GIF
- Interface interativa para seleção de países e campanhas

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conta Google Ads
- Acesso ao Google Drive
- Acesso ao Google Sheets
- Credenciais de serviço do Google (arquivos JSON)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/creative-update-template.git
cd creative-update-template
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as credenciais:
   - Coloque o arquivo `drive_credentials.json` na raiz do projeto
   - Coloque o arquivo `sheets_credentials.json` na raiz do projeto
   - Coloque o arquivo `google-ads.yaml` na raiz do projeto

## ⚙️ Configuração

1. **Google Drive**:
   - Crie uma pasta para templates
   - Crie uma pasta para logos

2. **Google Sheets**:
   - Use a planilha com ID: `1QQ7_ByU8siGV_NAMXM-fWiEt60fyPOJp0h-RshNsFeg`
   - A planilha deve ter as colunas: Site, ID da Conta, Nome da Conta, ID do Grupo de Anúncios, Campanha, País

## 📦 Estrutura de Pastas

```
.
├── output/              # Pasta para criativos gerados
├── templates/           # Cache local de templates
├── logos/              # Cache local de logos
├── main.py             # Script principal
├── update_mcc_sheet.py # Script de atualização da planilha MCC
├── requirements.txt    # Dependências
└── README.md          # Este arquivo
```

## 🎯 Como Usar

1. **Modo Interativo**:
```bash
python main.py
```
- Siga as instruções na tela para selecionar países e campanhas
- Escolha entre gerar criativos aleatórios ou específicos
- Defina a quantidade de criativos a serem gerados

2. **Modo com Parâmetros**:
```bash
python main.py --account_id "SEU_ID" --ad_group_id "SEU_ID" --site "NOME_DO_SITE" --quantity "QUANTIDADE"
```

3. **Atualização da Planilha MCC**:
```bash
python update_mcc_sheet.py
```

## 🔧 Configurações Personalizáveis

No arquivo `main.py`:
- `MAX_REQUESTS`: Limite de requisições (padrão: 3000)
- `DIMENSOES`: Tamanho dos criativos (padrão: 336x280)
- `LOGO_SIZE`: Tamanho da logo (padrão: 45x14)
- `IDIOMAS_POR_PAIS`: Mapeamento de países para idiomas

## 📝 Notas

- Os criativos são gerados com dimensões compatíveis com o Google Ads
- As logos são automaticamente redimensionadas e posicionadas
- O sistema suporta templates em PNG e GIF
- Os criativos são salvos sem metadados para otimização

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- Seu Nome - [GitHub](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Google Ads API
- Google Drive API
- Google Sheets API
- Pillow (PIL)
