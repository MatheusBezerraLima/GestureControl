GestureControl
GestureControl é um programa em Python que utiliza a webcam para detectar e interpretar movimentos das mãos em tempo real. Este projeto permite controlar o cursor do mouse e realizar cliques apenas movendo as mãos na frente da câmera, criando uma interface interativa sem a necessidade de tocar em dispositivos físicos.

Funcionalidades
Controle do Mouse: Move o cursor do mouse baseado na posição do dedo indicador.
Clique por Gestos: Executa um clique do mouse quando a distância entre o polegar e o dedo indicador é menor que um determinado limite.
Detecção de Mãos: Utiliza a biblioteca MediaPipe para detectar e rastrear as mãos na imagem da webcam.
Pré-requisitos
Antes de executar o programa, você precisa instalar as seguintes bibliotecas:

pyautogui: Para controlar o cursor do mouse e realizar cliques.
opencv-python: Para captura e processamento de vídeo da webcam.
mediapipe: Para detecção e rastreamento das mãos.
Você pode instalar as dependências usando o pip:

sh
Copiar código
pip install pyautogui opencv-python mediapipe
Uso
Clone o Repositório:

sh
Copiar código
git clone https://github.com/seu-usuario/GestureControl.git
cd GestureControl
Execute o Programa:

sh
Copiar código
python nome_do_seu_arquivo.py
Controle do Programa:

Pressione s para iniciar ou parar a detecção de mãos.
Pressione q para sair do programa.
Funcionamento
O programa usa a webcam para capturar o vídeo em tempo real e processa cada frame para detectar a posição das mãos. Quando a mão é detectada, a posição do dedo indicador é usada para mover o cursor do mouse, e a distância entre o polegar e o dedo indicador é verificada para simular cliques.

Código
O código fonte está disponível em GestureControl.py. O código inclui:

Inicialização das bibliotecas e configuração da webcam.
Função para calcular a distância entre dois pontos.
Loop principal para processar os frames da webcam e aplicar a lógica de controle.
Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções. Para contribuir, siga os seguintes passos:

Faça um fork do repositório.
Crie uma branch para sua alteração (git checkout -b minha-alteracao).
Faça commit das suas mudanças (git commit -am 'Adiciona nova funcionalidade').
Faça push para a branch (git push origin minha-alteracao).
Crie uma pull request.
Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue no repositório ou entrar em contato.
