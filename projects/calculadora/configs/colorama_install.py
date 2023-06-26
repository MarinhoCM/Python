import subprocess
def install_colorama():
    try:
        import colorama
        print('A biblioteca "colorama" já está instalada.')
    except ImportError:
        try:
            subprocess.check_call(['pip', 'install', 'colorama'])
            print('A biblioteca "colorama" foi instalada com sucesso!')
        except subprocess.CalledProcessError:
            print('Erro ao instalar a biblioteca "colorama". Certifique-se de que o pip está instalado e tente novamente.')
