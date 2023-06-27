import subprocess

def download_video(url):
    try:
        subprocess.call(['youtube-dl', url])
        print('Vídeo baixado com sucesso.')
    except Exception as e:
        print('Falha ao baixar o vídeo:', str(e))

# Para baixar o vídeo do link específico
video_url = 'blob:https://awujpypy2.nl/a98cfdd3-0648-4e6c-8c0d-098fd87f22f1'

download_video(video_url)
