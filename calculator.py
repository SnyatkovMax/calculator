from calc_functions import add, sub, mult, div, int_div, ostatok_ot_div, exponentiation, sinus, cosinus, tangent


def start_program():  # функция входа в калькулятор
    start = input('Для запуска калькулятора введите: 1, для выхода введите что угодно >>>   ').strip()
    if start == '1':
        print('приступим к работе')
    else:
        print('конец программы')
        exit()


calculator = {  # операции калькулятора
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
    '//': int_div,
    '%': ostatok_ot_div,
    '**': exponentiation,
    'sin': sinus,
    'cos': cosinus,
    'tg': tangent
}

start_program()  # вход в программу

while True:  # циклический ввод данных от пользователя
    try:
        print('Возможные  операции данного калькулятора: ', list(calculator.keys()))
        a = float(input('введите первое число >>> '))
        b = None
        operation = input('введите операцию >>> ').lower().strip()
        if operation == 'sin':
            break
        elif operation == 'cos':
            break
        elif operation == 'tg':
            break
        b = float(input('введите второе число >>> '))
    except ValueError as error:
        print('Ошибка ввода:', error)
        print('Попробуйте еще раз ')
        print()
    except Exception as err:
        print('Ошибка:', err)
    else:
        break

result = None

if operation in list(calculator.keys()):
    result = calculator[operation](a, b)

else:
    print('Неверная операция')

if result is not None:
    print('Результат операции = ', result)
