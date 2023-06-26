from models.calculate import Calculate
from utils.messages import (
    sucess_message,operation_message
)

def main() -> None: 
    points: int = 0
    play(points)
    
def play(points: int) -> None:
    difficulty: int = int(input(operation_message(
        'Informe o nível de dificuldade desejado [1, 2, 3, 4]: '
    )))
    if difficulty not in [1, 2, 3, 4]:
        print(sucess_message(
            "Dificuldade Calculadora-Humana setada!"
        ))        
    calc: Calculate = Calculate(difficulty) 
    calc.print_operation()

    result: int = int(input())
    
    if calc.check_result(result):
        points += 1
        print(operation_message(f'Você tem: {points} ponto(s).'))
    
    continue_in_game: int = int(input(operation_message(
        'Deseja continuar no jogo? [1 - sim, 0 - não] '
    ))) 
    
    if continue_in_game:
        play(points)
    else:
        print(f'Você finalizou com {points} ponto(s).')
        print(sucess_message('Até a proxima!'))
    
if __name__ == '__main__':
    main()
