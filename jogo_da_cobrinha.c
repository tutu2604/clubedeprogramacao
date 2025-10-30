#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <time.h>

#define LARGURA 20
#define ALTURA 20

int x, y, frutaX, frutaY, pontuacao;
int fimDeJogo;
int caudaX[100], caudaY[100];
int nCauda;

enum eDirecao { STOP = 0, ESQUERDA, DIREITA, CIMA, BAIXO };
enum eDirecao dir;

// --- Funções auxiliares de terminal ---
int kbhit(void) {
    struct termios oldt, newt;
    int ch;
    int oldf;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);
    if (ch != EOF) {
        ungetc(ch, stdin);
        return 1;
    }
    return 0;
}

char getch_noblock() {
    char c = 0;
    if (kbhit())
        c = getchar();
    return c;
}

// --- Movimentar cursor no terminal (ANSI escape) ---
void mover_cursor(int linha, int coluna) {
    printf("\033[%d;%dH", linha, coluna);
}

// --- Configuração inicial ---
void Setup() {
    fimDeJogo = 0;
    dir = STOP;
    x = LARGURA / 2;
    y = ALTURA / 2;
    srand(time(0));
    pontuacao = 0;
    nCauda = 0;

    // Garante que a fruta não nasce em cima da cobra
    do {
        frutaX = rand() % LARGURA;
        frutaY = rand() % ALTURA;
    } while (frutaX == x && frutaY == y);

    // Limpa tela e desenha bordas
    printf("\033[2J\033[?25l"); // limpa e oculta cursor

    // Bordas superiores
    mover_cursor(1, 1);
    for (int i = 0; i < LARGURA + 2; i++)
        printf("#");

    for (int i = 0; i < ALTURA; i++) {
        mover_cursor(i + 2, 1);
        printf("#");
        mover_cursor(i + 2, LARGURA + 2);
        printf("#");
    }

    mover_cursor(ALTURA + 2, 1);
    for (int i = 0; i < LARGURA + 2; i++)
        printf("#");

    // Desenha fruta e cabeça inicial
    mover_cursor(frutaY + 2, frutaX + 2);
    printf("F");

    mover_cursor(y + 2, x + 2);
    printf("O");

    mover_cursor(ALTURA + 4, 1);
    printf("Pontuação: %d", pontuacao);
    fflush(stdout);
}

// --- Atualiza apenas partes modificadas ---
void AtualizarTela(int oldX, int oldY) {
    // Apaga a antiga posição da cabeça
    mover_cursor(oldY + 2, oldX + 2);
    printf(" ");

    // Desenha o novo corpo (cauda)
    if (nCauda > 0) {
        mover_cursor(caudaY[0] + 2, caudaX[0] + 2);
        printf("o");
    }

    // Desenha nova cabeça
    mover_cursor(y + 2, x + 2);
    printf("O");

    // Atualiza pontuação
    mover_cursor(ALTURA + 4, 1);
    printf("Pontuação: %d  ", pontuacao);

    fflush(stdout);
}

// --- Entrada ---
void Input() {
    char tecla = getch_noblock();

    switch (tecla) {
        case 'a': if (dir != DIREITA) dir = ESQUERDA; break;
        case 'd': if (dir != ESQUERDA) dir = DIREITA; break;
        case 'w': if (dir != BAIXO) dir = CIMA; break;
        case 's': if (dir != CIMA) dir = BAIXO; break;
        case 'x': fimDeJogo = 1; break;
    }
}

// --- Lógica principal ---
void Logica() {
    int prevX = x;
    int prevY = y;
    int oldTailX = (nCauda > 0) ? caudaX[nCauda - 1] : -1;
    int oldTailY = (nCauda > 0) ? caudaY[nCauda - 1] : -1;

    // Atualiza posições da cauda
    int prevCaudaX = caudaX[0];
    int prevCaudaY = caudaY[0];
    int prev2X, prev2Y;

    caudaX[0] = x;
    caudaY[0] = y;

    for (int i = 1; i < nCauda; i++) {
        prev2X = caudaX[i];
        prev2Y = caudaY[i];
        caudaX[i] = prevCaudaX;
        caudaY[i] = prevCaudaY;
        prevCaudaX = prev2X;
        prevCaudaY = prev2Y;
    }

    // Movimento da cabeça
    switch (dir) {
        case ESQUERDA: x--; break;
        case DIREITA:  x++; break;
        case CIMA:     y--; break;
        case BAIXO:    y++; break;
        default: break;
    }

    // Colisão com paredes
    if (x >= LARGURA || x < 0 || y >= ALTURA || y < 0)
        fimDeJogo = 1;

    // Colisão com a cauda
    for (int i = 0; i < nCauda; i++) {
        if (caudaX[i] == x && caudaY[i] == y)
            fimDeJogo = 1;
    }

    // Comer fruta
    if (x == frutaX && y == frutaY) {
        pontuacao += 10;
        nCauda++;

        int posValida = 0;
        while (!posValida) {
            frutaX = rand() % LARGURA;
            frutaY = rand() % ALTURA;
            posValida = 1;

            // Garante que a fruta não apareça na cobra
            if (frutaX == x && frutaY == y)
                posValida = 0;
            for (int i = 0; i < nCauda; i++) {
                if (frutaX == caudaX[i] && frutaY == caudaY[i])
                    posValida = 0;
            }
        }

        // Desenha nova fruta
        mover_cursor(frutaY + 2, frutaX + 2);
        printf("F");
    } else if (nCauda > 0) {
        // Apaga o último segmento antigo da cauda
        mover_cursor(oldTailY + 2, oldTailX + 2);
        printf(" ");
    }

    AtualizarTela(prevX, prevY);
}

int main() {
    Setup();

    while (!fimDeJogo) {
        Input();
        Logica();
        usleep(100000); // velocidade do jogo
    }

    // Mostra mensagem final
    mover_cursor(ALTURA + 6, 1);
    printf("\nGame Over! Pontuação final: %d\n", pontuacao);
    printf("\033[?25h"); // mostra cursor novamente
    return 0;
}
