import streamlit as st
import yt_dlp
import os
import tempfile
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎥",
    layout="centered"
)

# Título do app
st.title("🎥 YouTube Downloader")
st.markdown("Converta vídeos do YouTube para MP4 ou MP3")

# Input do link
url = st.text_input("📎 Cole o link do vídeo do YouTube:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    # Seleção do formato
    formato = st.radio("📁 Escolha o formato:", ["MP4 (Vídeo)", "MP3 (Áudio)"])
    
    # Opções de qualidade baseadas no formato
    if formato == "MP4 (Vídeo)":
        qualidade = st.selectbox(
            "🎬 Escolha a qualidade do vídeo:",
            ["Baixa (480p)", "Média (720p)", "Alta (1080p)"]
        )
        
        # Mapear opções para configurações
        opcoes_qualidade = {
            "Baixa (480p)": {
                'format': 'best[height<=480]',
                'outtmpl': '%(title)s_480p.%(ext)s'
            },
            "Média (720p)": {
                'format': 'best[height<=720]',
                'outtmpl': '%(title)s_720p.%(ext)s'
            },
            "Alta (1080p)": {
                'format': 'best[height<=1080]',
                'outtmpl': '%(title)s_1080p.%(ext)s'
            }
        }
        
    else:  # MP3
        qualidade = st.selectbox(
            "🎵 Escolha a qualidade do áudio:",
            ["Baixa (128 kbps)", "Média (192 kbps)", "Alta (320 kbps)"]
        )
        
        # Mapear opções para configurações
        opcoes_qualidade = {
            "Baixa (128 kbps)": {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '128',
                }],
                'outtmpl': '%(title)s_128kbps.%(ext)s'
            },
            "Média (192 kbps)": {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s_192kbps.%(ext)s'
            },
            "Alta (320 kbps)": {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'outtmpl': '%(title)s_320kbps.%(ext)s'
            }
        }

    # Botão de download
    if st.button("⬇️ Baixar", type="primary"):
        if not url.strip():
            st.error("❌ Por favor, insira um link válido!")
        else:
            try:
                # Criar pasta temporária
                temp_dir = tempfile.mkdtemp()
                
                # Configurar opções do yt-dlp
                opcoes = opcoes_qualidade[qualidade].copy()
                opcoes['outtmpl'] = os.path.join(temp_dir, opcoes['outtmpl'])
                
                # Mostrar loading
                with st.spinner(f"⏳ Baixando {formato.lower()}..."):
                    with yt_dlp.YoutubeDL(opcoes) as ydl:
                        # Obter informações do vídeo
                        info = ydl.extract_info(url, download=False)
                        titulo = info.get('title', 'video')
                        
                        # Fazer download
                        ydl.download([url])
                
                # Encontrar o arquivo baixado
                arquivos = list(Path(temp_dir).glob('*'))
                if arquivos:
                    arquivo = arquivos[0]
                    
                    # Ler o arquivo
                    with open(arquivo, 'rb') as f:
                        dados = f.read()
                    
                    # Botão de download
                    st.success("✅ Download concluído!")
                    st.download_button(
                        label="💾 Clique para baixar o arquivo",
                        data=dados,
                        file_name=arquivo.name,
                        mime="application/octet-stream"
                    )
                    
                    # Limpar arquivo temporário
                    os.remove(arquivo)
                    os.rmdir(temp_dir)
                    
                else:
                    st.error("❌ Erro: Arquivo não encontrado após o download")
                    
            except Exception as e:
                st.error(f"❌ Erro ao baixar: {str(e)}")
                
                # Sugestões de erro comuns
                if "FFmpeg" in str(e):
                    st.info("💡 **Dica:** Certifique-se de ter o FFmpeg instalado para conversão de áudio")
                elif "private" in str(e).lower():
                    st.info("💡 **Dica:** Este vídeo pode ser privado ou restrito")
                elif "age" in str(e).lower():
                    st.info("💡 **Dica:** Este vídeo pode ter restrição de idade")

# Sidebar com informações
with st.sidebar:
    st.markdown("### ℹ️ Informações")
    st.markdown("""
    **Formatos suportados:**
    - 🎥 MP4: 480p, 720p, 1080p
    - 🎵 MP3: 128, 192, 320 kbps
    
    **Requisitos:**
    - Para MP3: FFmpeg instalado
    - Link válido do YouTube
    """)
    
    # st.markdown("### 🛠️ Como instalar FFmpeg")
    # st.code("winget install ffmpeg", language="bash")
    
    st.markdown("---")
    st.markdown("*Desenvolvido com ❤️ usando Streamlit*")