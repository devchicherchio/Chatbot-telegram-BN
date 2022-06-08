import time
import telebot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PyQt5 import uic, QtWidgets
import threading

host = "smtp.gmail.com"
port = "587"
login = "bnbot.emails@gmail.com"
senha = "hlfaebrutyrprhuw"
para = "geraldo@bninvestimentos.com"
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login, senha)


def iniciar():
    try:

        def iniciar1():
            chave_api = "2017542557:AAFgp2knhFMqrNPR5vGJpX-JKQeWcYE4wiA"
            bot = telebot.TeleBot(chave_api)
            # PDF carteira + PDF resultados
            carteira1 = primeira_tela.lineEdit.text()
            resultados1 = primeira_tela.lineEdit_2.text()
            pack_estudos = primeira_tela.lineEdit_3.text()
            primeira_tela.label_5.setText("          BOT ONLINE")

            @bot.message_handler(content_types=['photo'])
            def photo(messagem):
                fileID = messagem.photo[-1].file_id
                file_info = bot.get_file(fileID)
                downloaded_file = bot.download_file(file_info.file_path)
                a = (messagem.from_user.first_name)
                b = (a) + 'print.jpg'
                texto3 = """

/menu 🗳 voltar ao menu principal

Show de bola 🔥 Já recebemos sua imagem !

Como você quer ganhar dinheiro?(Clique na opção):

/Crescimento 📈 Crescimento patrimonial
/Dividendos    💸 Divindendos
/Ambos          💱 Crescimento e dividendos                                   

                      """

                bot.send_message(messagem.chat.id, texto3)
                with open(b, 'wb') as new_file:
                    new_file.write(downloaded_file)

            @bot.message_handler(commands=["analise"])
            def analise(mensagem):
                mensagem_usuario = mensagem.text
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)
                texto2 = """

/menu 🗳 voltar ao menu principal 

Otíma escolha! Agora, preciso que nos informe o Ativo escolhido ✅

▪️  OBS: Coloque + antes do ativo ▪️  

exemplo: 🔺 + PETR4       
exemplo: 🔺 + CASH3 


                          """

                bot.send_message(mensagem.chat.id, texto2)

            @bot.message_handler(commands=["otimize"])
            def otimize(mensagem):
                mensagem_usuario = mensagem.text
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)
                texto2 = """

/menu 🗳 voltar ao menu principal

Boa Escolha! Agora, precisamos de um print da sua carteira de investimento atual 🖼


                      """

                bot.send_message(mensagem.chat.id, texto2)

            @bot.message_handler(commands=["carteira"])
            def carteira(mensagem):
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)

                texto2 = """
/Menu  Voltar ao menu principal 

Legal ! 🔥  Iremos te enviar nossa carteira de investimento BN+                                 

                          """

                bot.send_message(mensagem.chat.id, texto2)
                bot.send_message(mensagem.chat.id, carteira1)
                print((nome_usuario) + ' ID: ' + (id_usuario1) + ' Carteira BN+ enviado')

            @bot.message_handler(commands=["resultados"])
            def resultados(mensagem):
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)

                texto2 = """
/Menu  Voltar ao menu principal 

Legal ! 🔥  Iremos te enviar nosso resultado da semana 💥                                  

                          """

                bot.send_message(mensagem.chat.id, texto2)
                bot.send_message(mensagem.chat.id, resultados1)
                print((nome_usuario) + ' ID: ' + (id_usuario1) + ' Resultados BN+ enviado')

            @bot.message_handler(commands=["pack"])
            def pack(mensagem):
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)

                texto2 = """
/Menu  Voltar ao menu principal 

Legal ! 🔥  Iremos te enviar nosso Pack de estudos 💥                                  

                          """

                bot.send_message(mensagem.chat.id, texto2)
                bot.send_message(mensagem.chat.id, pack_estudos)
                print((nome_usuario) + ' ID: ' + (id_usuario1) + ' Pack BN+ enviado')

            def verificar(mensagem):
                return True

            @bot.message_handler(func=verificar)
            def saudacao(mensagem):
                mensagem_usuario = mensagem.text
                nome_usuario = mensagem.from_user.first_name
                id_usuario = mensagem.from_user.id
                id_usuario1 = str(id_usuario)
                a = (mensagem.from_user.first_name)
                b = (a) + 'print.jpg'
                if "+" in mensagem.text:
                    bot.send_message(mensagem.chat.id, "/menu 🗳 voltar ao menu principal")
                    bot.send_message(mensagem.chat.id, "Beleza " + (
                        nome_usuario) + ", já cadastramos seu pedido no sistema, em até 24horas, iremos te envia um PDF com a análise do ativo escolhido. Muito Obrigado por entrar em contato conosco! 🤖")
                    print('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// ordem: Análise /// Número para contato + Ativo escolhido: ' + (
                              mensagem_usuario))
                    analisee = ('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// Ordem: Análise /// Ativo escolhido: ' + (mensagem_usuario))
                    email_msg = MIMEMultipart()
                    email_msg['From'] = login
                    email_msg['To'] = para
                    email_msg['Subject'] = "Olá, você tem uma nova ordem de " + (nome_usuario)
                    email_msg.attach(MIMEText(analisee, 'plain'))
                    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

                elif "/Crescimento" in mensagem.text:
                    bot.send_message(mensagem.chat.id, "/menu 🗳 voltar ao menu principal")
                    bot.send_message(mensagem.chat.id, "Beleza " + (
                        nome_usuario) + ", já cadastramos seu pedido no sistema, em até 24horas, iremos te envia um PDF com a otimização escolhida(Crescimento Patrimionial). Muito Obrigado por entrar em contato conosco! 🤖")
                    print('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// ordem: Crescimento Patrimonial /// Print baixado ')
                    email_msg1 = MIMEMultipart()
                    email_msg1['From'] = login
                    email_msg1['To'] = para
                    email_msg1['Subject'] = "Olá, você tem uma nova ordem de " + (nome_usuario)
                    crescimentoo = ('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// Ordem: Crescimento Patrimonial /// Print baixado ')
                    cam_arquivo = 'C:/Users/Geraldo Dias/OneDrive/BN+ Investimentos/Empresa/BOT BN+/' + (b)
                    attchment = open(cam_arquivo, 'rb')
                    att = MIMEBase('application', 'octet-stream')
                    att.set_payload(attchment.read())
                    encoders.encode_base64(att)
                    att.add_header('Content-Disposition', f'attachment; filename=BN+print.jpg')
                    attchment.close()
                    email_msg1.attach(att)
                    email_msg1.attach(MIMEText(crescimentoo, 'plain'))
                    server.sendmail(email_msg1['From'], email_msg1['To'], email_msg1.as_string())


                elif "/Dividendos" in mensagem.text:
                    bot.send_message(mensagem.chat.id, "/menu 🗳 voltar ao menu principal")
                    bot.send_message(mensagem.chat.id, "Beleza " + (
                        nome_usuario) + ", já cadastramos seu pedido no sistema, em até 24horas, iremos te envia um PDF com a otimização escolhida(Dividendos). Muito Obrigado por entrar em contato conosco! 🤖")
                    print('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// ordem: Dividendos /// Print baixado ')
                    email_msg2 = MIMEMultipart()
                    email_msg2['From'] = login
                    email_msg2['To'] = para
                    email_msg2['Subject'] = "Olá, você tem uma nova ordem de " + (nome_usuario)
                    dividendoss = ('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// Ordem: Dividendos /// Print baixado ')
                    cam_arquivo = 'C:/Users/Geraldo Dias/OneDrive/BN+ Investimentos/Empresa/BOT BN+/' + (b)
                    attchment = open(cam_arquivo, 'rb')
                    att = MIMEBase('application', 'octet-stream')
                    att.set_payload(attchment.read())
                    encoders.encode_base64(att)
                    att.add_header('Content-Disposition', f'attachment; filename=BN+print.jpg')
                    attchment.close()
                    email_msg2.attach(att)
                    email_msg2.attach(MIMEText(dividendoss, 'plain'))
                    server.sendmail(email_msg2['From'], email_msg2['To'], email_msg2.as_string())
                elif "/Ambos" in mensagem.text:
                    bot.send_message(mensagem.chat.id, "/menu 🗳 voltar ao menu principal")
                    bot.send_message(mensagem.chat.id, "Beleza " + (
                        nome_usuario) + ", já cadastramos seu pedido no sistema, em até 24horas, iremos te envia um PDF com a otimização escolhida(Cresimento e Dividendo). Muito Obrigado por entrar em contato conosco! 🤖")
                    print('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// ordem: Crescimento Patrimonial + Dividendos /// Print baixado ')
                    email_msg3 = MIMEMultipart()
                    email_msg3['From'] = login
                    email_msg3['To'] = para
                    email_msg3['Subject'] = "Olá, você tem uma nova ordem de " + (nome_usuario)
                    ambos = ('Cliente: ' + (nome_usuario) + ' /// ID: ' + (
                        id_usuario1) + ' /// Ordem: Crescimento + Dividendos /// Print baixado ')
                    cam_arquivo = 'C:/Users/Geraldo Dias/OneDrive/BN+ Investimentos/Empresa/BOT BN+/' + (b)
                    attchment = open(cam_arquivo, 'rb')
                    att = MIMEBase('application', 'octet-stream')
                    att.set_payload(attchment.read())
                    encoders.encode_base64(att)
                    att.add_header('Content-Disposition', f'attachment; filename=BN+print.jpg')
                    attchment.close()
                    email_msg3.attach(att)
                    email_msg3.attach(MIMEText(ambos, 'plain'))
                    server.sendmail(email_msg3['From'], email_msg3['To'], email_msg3.as_string())
                else:
                    texto_nome = '🤖 Fala ' + (nome_usuario) + '! Tranquilo?'"""

Fala aí, como posso te ajudar?(Clique na opção):

/analise       🔍 Análise
/otimize       🌐 Otimize minha carteira
/carteira      🚀 Carteira investimentos BN+
/resultados 🤑 Resultados da semana   
/pack            📕 Pack de estudos                              

▪️  Responder qualquer outra coisa não vai funcionar, clique em uma das opções  ▪️"""

                    bot.reply_to(mensagem, texto_nome)

            bot.polling()
    except:
        return

    tarefa = threading.Thread(target=iniciar1)
    tarefa.daemon = True
    tarefa.start()


def enviar():
    pass

    def enviar2():
        chave_api = "2017542557:AAFgp2knhFMqrNPR5vGJpX-JKQeWcYE4wiA"
        bot = telebot.TeleBot(chave_api)
        pdf_cliente1 = primeira_tela.lineEdit_6.text()
        id_cliente = primeira_tela.lineEdit_4.text()
        id_cliente2 = float(id_cliente)
        bot.send_message((id_cliente2), '🤖 Olá, segue PDF com serviço solicitado!')
        bot.send_message((id_cliente2), (pdf_cliente1))
        bot.send_message((id_cliente2), '💫 Muito Obrigado pela preferência!')
        primeira_tela.label_5.setText("       PDF ENVIADO !")
        time.sleep(2)
        primeira_tela.label_5.setText("          BOT ONLINE")

        # bot.polling()

    tarefa = threading.Thread(target=enviar2)
    tarefa.daemon = True
    tarefa.start()


def enviar_m():
    pass

    def enviar_m2():
        chave_api = "2017542557:AAFgp2knhFMqrNPR5vGJpX-JKQeWcYE4wiA"
        bot = telebot.TeleBot(chave_api)
        pdf_cliente1 = primeira_tela.lineEdit_7.text()
        id_cliente = primeira_tela.lineEdit_5.text()
        id_cliente2 = float(id_cliente)
        bot.send_message((id_cliente2), (pdf_cliente1))
        primeira_tela.label_5.setText("  MENSAGEM ENVIADA !")
        time.sleep(2)
        primeira_tela.label_5.setText("          BOT ONLINE")

        # bot.polling()

    tarefa = threading.Thread(target=enviar_m2)
    tarefa.daemon = True
    tarefa.start()


def frame1():
    primeira_tela.frame.close()
    primeira_tela.frame_2.show()


def frame2():
    primeira_tela.frame.show()


def frame3():
    primeira_tela.frame.close()
    primeira_tela.frame_2.close()
    primeira_tela.frame_3.show()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("config2.ui")
primeira_tela.pushButton.clicked.connect(frame2)
primeira_tela.pushButton_2.clicked.connect(frame1)
primeira_tela.pushButton_3.clicked.connect(frame3)
primeira_tela.pushButton_4.clicked.connect(iniciar)
primeira_tela.pushButton_5.clicked.connect(enviar)
primeira_tela.pushButton_6.clicked.connect(enviar_m)
primeira_tela.show()
app.exec()

