# Criando um código simples para abrir uma pagina do youtube quantas vezes a cada x minutos determinarmos

# Primeiro importamos as bibliotecas necessárias
import webbrowser  # para ter acesso a ações pelo navegador
import time  # para poder definir pausa e o momento de execução

# criamos aqui uma função para converter minutos em segundos e aguardar o tempo definido


def AguardarMinutos(minutos):
    segundos = minutos * 60  # convertendo minutos em segundos
    # executando o método sleep da biblioteca time que irá esperar conforme o tempo determinado
    return time.sleep(segundos)

# criamos aqui uma função para definirmos quantas vezes queremos que o video seja executado,
# quantos minutos devemos esperar e qual o link para o vídeo a ser aberto


def InciniarBreakTime(vezes, minutos, video_url):
    print "Iniciado em ", time.ctime()  # estamos aqui quando iniciamos a execução
    i = 0  # definimos a variável que iremos incrementar a cada execução
    while i < vezes:  # fazemos aqui o loop que será interrompido quando a variável chegar ao valor que definimos em vezes
        # executamos nossa função para que seja aguardado os minutos
        AguardarMinutos(minutos)
        i += 1  # incrementamos a variável
        # estamos aqui imprimindo a vez e quando foi feita a execução, apenas para consulta
        print "Execução", i, "vez em", time.ctime()
        # aqui executamos o método open da biblioteca webbrowser
        webbrowser.open(video_url)
    # estamos aqui imprimindo quando terminamos a execução
    print "Execução terminada em ", time.ctime()


# aqui executamos nosso código
InciniarBreakTime(5, 25, "https://www.youtube.com/watch?v=HyhB3c_whgo")
