"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

"""Пример создания стека через ООП"""

"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = []
        self.stack = []

    def push_in_stack(self):
        """Копируем, поскольку иначе это будет функционировать как ссылка на elems"""
        self.stack.append(self.elems.copy())

    def pop_out_stack(self):
        return self.stack.pop()

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.stack_size() < 10:
            self.elems.append(el)
        else:
            self.push_in_stack()
            self.elems.clear()
            self.elems.append(el)

    def pop_out(self):
        if self.stack_size() > 0:
            return self.elems.pop()
        else:
            self.elems = self.pop_out_stack()
            return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(f'стек тарелок пустой: {SC_OBJ.is_empty()}')  # -> стек тарелок пустой
    print(f'Размер стека тарелок: {SC_OBJ.stack_size()}')

    # Наполняем стек тарелками. Индекс для того, чтобы тарелки были помечены
    for i in range(39):
        SC_OBJ.push_in(100 + i)
    # Контроль
    print(f'Размер стека тарелок: {SC_OBJ.stack_size()}')
    print(f'Число и состав стопок: \n{SC_OBJ.stack}')
    print(f'Контроль стека тарелок: \n{SC_OBJ.elems}')

    # уберем часть тарелок
    for i in range(21):
        SC_OBJ.pop_out()
    # Контроль
    print(f'Размер стека тарелок: {SC_OBJ.stack_size()}')
    print(f'Число и состав стопок: \n{SC_OBJ.stack}')
    print(f'Контроль стека тарелок: \n{SC_OBJ.elems}')
