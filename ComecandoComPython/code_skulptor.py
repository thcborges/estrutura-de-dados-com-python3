# para executar, copiar o código e colar em: http://www.codeskulptor.org/


from math import sqrt

import random
import simplegui

center_point = [50, 50]
window_width = 600  # Largura da janela
window_height = 400  # Altura da janela
radius = 20
score = 0


# desenha o canvas
def draw(canvas):
    canvas.draw_circle(center_point, radius, 1, 'Red', 'Red')


# temporizador
def timer_handler():
    center_point[0] = random.randint(0, window_height)
    center_point[1] = random.randint(0, window_height)


def mouse_handler(pos):
    global score

    # cáculo da distância
    dist = sqrt(((pos[0] - center_point[0]) ** 2) +
                ((pos[1] - center_point[1]) ** 2))

    # verifica se o usuário clicou dentro do círculo
    if dist < radius:
        score += 1  # incrementa o score
    elif score > 0:
        score -= 1  # decrementa o score

    # atualizo o texto do label
    label.set_text('Score: ' + str(score))


# cria uma janela passando o título largura e altura
frame = simplegui.create_frame(
    'Clique na bolinha',
    window_width,
    window_height)

# cria um temporizador passando o intervalo e o manipulador
timer = simplegui.create_timer(1000, timer_handler)

# seta os manipuladores de eventos
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

# adiciona um label
label = frame.add_label('Score: ' + str(score))

timer.start()  # inicia o temporizador
frame.start()  # loop principal da aplicação
