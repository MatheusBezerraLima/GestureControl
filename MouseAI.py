# INSTALAR BIBLIOTECAS NO CMD Python312\Script:
#  pip install pyautogui
#  pip install opencv-python    
#  pip install mediapipe

# AS para dar um "apelido" para o comando.

import cv2 
import pyautogui as py
import mediapipe as mp
import math 

mp_hands = mp.solutions.hands # Captura o contorna da mão
mp_drawing = mp.solutions.drawing_utils #  Desenha o contorna da mão (OSSOS)

# Iniciando o Mediapipe prad detectar a mão
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) # Define o numero de mãos que serâo capturadas / Calcula a porcentagem de quanto a sua mão parece com a mão salva na base de dados da IA

# Captura a Imagem
cap = cv2.VideoCapture(0)

# Capturar o tamanho da tela(Altura, Largura) * Poderia capturar profundidade tambem
screen_width, screen_height = py.size()

# Função para calcular a distancia entre dois pontos ultilizando o teorema de  pitagoras 
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

# Loop infinito para processar os frames da webcam
while True: 
    ret, frame = cap.read()

    # SE não encontrar a variavel ret ele para de executar (Não achou a câmera)
    if not ret:
        print("Câmera não encontrada :( ")
        break

    # Convertendo a imagem para RGB 
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processando a imagem para detectar mãos
    result = hands.process(frame_rgb)

    # Obtendo as dimensões do frame 
    frame_height, frame_width, _ = frame.shape

    # Se o processamento encontrar algum landmarks(Pontos da mão) executa a função
    if result.multi_hand_landmarks:
        # Pontos da mão: Dedo Polegadar = indice 4 / Dedo indicador = indice 8
        for hand_landmarks in result.multi_hand_landmarks:
            # Extraindo as coordenadas do ponto 8 (dedo indicador) e do ponto 4(polegar)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            
            # Calculando distancia entre polegar e indicador 
            distance = calculate_distance(index_finger_tip, thumb_tip)

            # Movendo o cursos do mouse
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)

            # INvertendo o eixo x (porque algumas cameras espelham) e ajustando po eixo y
            screen_x =(screen_width / frame_width * x)
            screen_y = screen_height / frame_height * y

            #Mover mouse com a mão
            py.moveTo(screen_x, screen_y)

            # Se a distancioa for menor que um certo limite, considera  um clique
            if distance < 0.05:
                py.click()

            # desenhando os landmarks(PONTOS) da mão
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Exibindo o frame na tela 
        cv2.imshow("Tracking da mão", frame)

        # Fechar ao pressionar "ESC"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberação dos recursos
cap.release()
cv2.destroyAllWindows()



