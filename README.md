# 🎥 YouTube Downloader

Um aplicativo simples e intuitivo para baixar vídeos do YouTube em formato MP4 ou converter para MP3, com interface web moderna usando Streamlit.

## ✨ Funcionalidades

- 🎬 **Download de vídeos** em formato MP4
- 🎵 **Conversão para áudio** em formato MP3
- 📊 **3 níveis de qualidade** para cada formato
- 🌐 **Interface web** moderna e responsiva
- ⚡ **Download direto** pelo navegador
- 📱 **Compatível** com desktop e mobile

### Qualidades Disponíveis

#### 🎥 Vídeo (MP4)
- **Baixa:** 480p - Ideal para economia de espaço
- **Média:** 720p - Equilíbrio entre qualidade e tamanho
- **Alta:** 1080p - Máxima qualidade disponível

#### 🎵 Áudio (MP3)
- **Baixa:** 128 kbps - Menor tamanho, qualidade básica
- **Média:** 192 kbps - Boa qualidade para uso geral
- **Alta:** 320 kbps - Qualidade premium

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- FFmpeg (obrigatório para conversão MP3)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/youtube-downloader.git
cd youtube-downloader
```

### 2. Instale as dependências

```bash
pip install streamlit yt-dlp
```

### 3. Instale o FFmpeg

#### Windows

**Opção 1 - Usando winget (recomendado):**
```bash
winget install ffmpeg
```

**Opção 2 - Download manual:**
1. Baixe de: https://ffmpeg.org/download.html
2. Extraia para `C:\ffmpeg\`
3. Adicione `C:\ffmpeg\bin` ao PATH do sistema

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS
```bash
brew install ffmpeg
```

### 4. Verifique a instalação do FFmpeg

```bash
ffmpeg -version
```

## 🖥️ Como Usar

### 1. Execute o aplicativo

```bash
streamlit run app.py
```

### 2. Acesse no navegador

O aplicativo abrirá automaticamente em `http://localhost:8501`

### 3. Use a interface

1. **Cole o link** do vídeo do YouTube
2. **Escolha o formato:** MP4 (vídeo) ou MP3 (áudio)
3. **Selecione a qualidade** desejada
4. **Clique em "Baixar"**
5. **Aguarde o processamento**
6. **Baixe o arquivo** clicando no botão que aparece

## 📁 Estrutura do Projeto

```
youtube-downloader/
│
├── app.py                 # Aplicativo principal Streamlit
├── youtube_downloader.py  # Versão linha de comando
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
└── .gitignore           # Arquivos ignorados pelo Git
```

## 🛠️ Versões Disponíveis

### Interface Web (Streamlit)
- Interface moderna e intuitiva
- Download direto pelo navegador
- Mensagens de erro claras
- Responsivo para mobile

### Linha de Comando
- Versão mais leve
- Ideal para automação
- Sem dependências de interface

## ⚠️ Problemas Comuns

### Erro: "FFmpeg not found"
**Solução:** Instale o FFmpeg seguindo as instruções acima

### Erro: "Video unavailable"
**Possíveis causas:**
- Vídeo privado ou removido
- Restrição geográfica
- Restrição de idade
- Link inválido

### Erro: "This video is private"
**Solução:** Não é possível baixar vídeos privados

### Download muito lento
**Dicas:**
- Escolha qualidade menor
- Verifique sua conexão
- Tente em horário de menor tráfego

## 📋 Requisitos do Sistema

### Mínimos
- Python 3.7+
- 2GB RAM
- 1GB espaço livre
- Conexão com internet

### Recomendados
- Python 3.9+
- 4GB RAM
- 5GB espaço livre
- Conexão banda larga

## 🔒 Considerações Legais

- ⚖️ **Respeite os direitos autorais**
- 📝 **Use apenas para conteúdo permitido**
- 🚫 **Não redistribua conteúdo protegido**
- ✅ **Siga os termos de uso do YouTube**

## 🛡️ Limitações

- Não baixa playlists completas
- Não suporta vídeos com DRM
- Máximo de 1080p para vídeos
- Depende da disponibilidade do YouTube

## 🔄 Atualizações

Para manter o aplicativo funcionando:

```bash
pip install --upgrade yt-dlp streamlit
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0 (2025-07-24)
- ✅ Interface Streamlit
- ✅ Download MP4 em 3 qualidades
- ✅ Conversão MP3 em 3 qualidades
- ✅ Download direto pelo navegador
- ✅ Tratamento de erros

## 📞 Suporte

Encontrou um problema? Abra uma [issue](https://github.com/seu-usuario/youtube-downloader/issues) no GitHub.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🏃‍♂️ Início Rápido

```bash
# 1. Clone e entre na pasta
git clone https://github.com/seu-usuario/youtube-downloader.git
cd youtube-downloader

# 2. Instale dependências
pip install streamlit yt-dlp

# 3. Instale FFmpeg
winget install ffmpeg

# 4. Execute o app
streamlit run app.py
```

**Pronto! 🎉 Agora é só usar!**

---

<div align="center">

**Desenvolvido com ❤️ usando Python e Streamlit**

[⭐ Dê uma estrela](https://github.com/seu-usuario/youtube-downloader) se este projeto te ajudou!

</div>