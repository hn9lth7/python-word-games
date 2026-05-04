import random 

def inp_secret_word():
    word = ['СОБАКА', 'ВІКНО', 'МОНІТОР', 'АЛГОРИТМ', 'ПРОЦЕСОР', 'БУДИНОК']
    secret_word = random.choice(word)
    return secret_word.upper()

def calc_attempts(secret_word):
    return len(secret_word)

def inp_symbol():
    while True:
        symbol = input('Введіть одну літеру: ').upper()
        if len(symbol) == 1 and symbol.isalpha():
            return symbol 
        print("Помилка! Треба ввести лише одну літеру.")

def check_game(word, attempts):
    used_symbols = []
    display_word = ['_'] * len(word)

    while attempts > 0 and '_' in display_word:
        print("=" * 40)
        print(" ".join(display_word))
        print("=" * 40)
        print(f"Використані літери: {','.join(used_symbols)}")
        print(f"Залишилося {attempts} спроб")
        print("=" * 40)

        current_symb = inp_symbol()

        if current_symb in used_symbols:
            print(f"Ви вже використовували літеру '{current_symb}'!")
            continue

        used_symbols.append(current_symb)

        if current_symb in word:
            print(f"Є така літера!")
        
            for i in range(len(word)):
                if word[i] == current_symb:
                    display_word[i] = current_symb
        else:
            print(f"Такої літери немає.")
            attempts -= 1

        if "_" not in display_word:
            return "WIN"
            
    return "LOSE"

def run_game():
    secret_word = inp_secret_word()
    attempts = calc_attempts(secret_word)

    result = check_game(secret_word, attempts)

    if result == "WIN":
        print("\n" + "="*40)
        print(f"Вітаємо! Ви відгадали слово: {secret_word}")
        print("Гравець виграв")
    else:
        print("\n" + "="*40)
        print(f"Спроби закінчилися. Таємне слово було: {secret_word}")
        print("Гравець програв")

if __name__ == '__main__':
    run_game()