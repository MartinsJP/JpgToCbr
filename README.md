# 📚 Conversor de Mangá para CBR

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![WinRAR](https://img.shields.io/badge/Requires-WinRAR-red.svg)](https://www.win-rar.com/)

> Uma aplicação Python com interface gráfica para converter capítulos de mangá organizados em pastas para o formato CBR de forma simples e eficiente.

## ✨ Funcionalidades

- 🎯 **Interface Intuitiva**: GUI moderna e fácil de usar com Tkinter
- 📁 **Seleção Flexível**: Escolha volumes e capítulos específicos para converter
- 🔄 **Conversão em Lote**: Converta múltiplos capítulos de uma só vez
- 📊 **Progresso Visual**: Barra de progresso e status detalhado em tempo real
- 🎨 **Suporte Múltiplos Formatos**: JPG, JPEG, PNG, GIF, BMP, WEBP
- 🔢 **Ordenação Inteligente**: Organização natural dos arquivos (1, 2, 10 ao invés de 1, 10, 2)
- ⚠️ **Tratamento de Erros**: Relatórios detalhados de sucesso e falhas
- 🏷️ **Nomenclatura Automática**: Nomes de arquivo organizados por volume e capítulo

## 🖼️ Screenshots

### Interface Principal
```
📚 Conversor de Mangá para CBR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Passo 1: Selecione a pasta principal
┌─────────────────────────────────────┐
│ C:\Users\User\Documents\MeuManga    │ 📂 Procurar
└─────────────────────────────────────┘

📖 Passo 2: Selecione os volumes
┌─────────────────────────────────────┐
│ ☑ Volume 01                         │
│ ☑ Volume 02                         │
│ ☐ Volume 03                         │
└─────────────────────────────────────┘
         🔄 Atualizar Volumes

📄 Passo 3: Selecione os capítulos  
┌─────────────────────────────────────┐
│ ☑ Volume 01/Capitulo 001           │
│ ☑ Volume 01/Capitulo 002           │
│ ☐ Volume 02/Capitulo 003           │
└─────────────────────────────────────┘
        🔄 Atualizar Capítulos

🚀 Passo 4: Conversão
      🎯 Converter para CBR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[████████████████████████████] 100%
```

## 🚀 Instalação

### Pré-requisitos

1. **Python 3.7 ou superior**
   ```bash
   # Verificar versão do Python
   python --version
   ```

2. **WinRAR** (obrigatório)
   - Baixe em: https://www.win-rar.com/
   - Instale na localização padrão ou adicione ao PATH do sistema

### Download e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/manga-cbr-converter.git
   cd manga-cbr-converter
   ```

2. **Execute o programa:**
   ```bash
   python manga_cbr_converter.py
   ```

## 📖 Como Usar

### Estrutura de Pastas Esperada

Organize seus mangás na seguinte estrutura:

```
📁 MeuManga/
├── 📁 Volume 01/
│   ├── 📁 Capitulo 001/
│   │   ├── 001.jpg
│   │   ├── 002.jpg
│   │   └── ...
│   └── 📁 Capitulo 002/
│       ├── 001.jpg
│       └── ...
└── 📁 Volume 02/
    └── 📁 Capitulo 003/
        └── ...
```

### Passo a Passo

1. **📁 Selecionar Pasta Principal**
   - Clique em "Procurar" e escolha a pasta que contém os volumes do mangá

2. **📖 Escolher Volumes**
   - Clique em "Atualizar Volumes" para listar as pastas disponíveis
   - Selecione os volumes desejados (use Ctrl+Click para múltipla seleção)

3. **📄 Escolher Capítulos**
   - Clique em "Atualizar Capítulos" para listar capítulos dos volumes selecionados
   - Selecione os capítulos que deseja converter

4. **🚀 Converter**
   - Clique em "Converter para CBR"
   - Escolha a pasta onde salvar os arquivos CBR
   - Acompanhe o progresso na barra de status

### Resultado

Os arquivos CBR serão criados com nomenclatura organizada:
- `Volume_01_Capitulo_001.cbr`
- `Volume_01_Capitulo_002.cbr`
- `Volume_02_Capitulo_003.cbr`

## ⚙️ Configuração Avançada

### Caminhos do WinRAR

O programa procura automaticamente o WinRAR nos locais padrão:
- `C:\Program Files\WinRAR\rar.exe`
- `C:\Program Files (x86)\WinRAR\rar.exe`
- `rar` (se estiver no PATH)

### Formatos Suportados

- **Entrada**: JPG, JPEG, PNG, GIF, BMP, WEBP
- **Saída**: CBR (Comic Book RAR)

## 🐛 Solução de Problemas

### ❌ "WinRAR não encontrado"
**Solução**: Instale o WinRAR ou adicione-o ao PATH do sistema

### ❌ "Nenhuma imagem encontrada"
**Solução**: Verifique se as pastas dos capítulos contêm arquivos de imagem

### ❌ "Erro ao ler volumes/capítulos"
**Solução**: Verifique as permissões de leitura das pastas

### ❌ Arquivo CBR não abre
**Solução**: Teste com leitores como CDisplayEx, YACReader ou ComicRack

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### 💡 Ideias para Contribuições

- [ ] Suporte para outros compressores (7-Zip, ZIP)
- [ ] Interface em outros idiomas
- [ ] Conversão para outros formatos (CBZ, PDF)
- [ ] Drag & Drop de pastas
- [ ] Preview das imagens
- [ ] Configurações de compressão
- [ ] Suporte para Linux/macOS

## 🔧 Desenvolvimento

### Estrutura do Código

```python
class MangaCBRConverter:
    ├── __init__()           # Inicialização da interface
    ├── setup_ui()           # Configuração da GUI
    ├── select_main_folder() # Seleção da pasta principal
    ├── update_volumes()     # Atualização da lista de volumes
    ├── update_chapters()    # Atualização da lista de capítulos
    ├── convert_to_cbr()     # Conversão principal
    └── create_cbr_from_folder() # Criação de arquivo CBR
```

### Executar em Modo Debug

```bash
python -v manga_cbr_converter.py
```

---
