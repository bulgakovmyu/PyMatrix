# Объявляется класс матриц, наследуемый от списка и определяются его основные свойства и методы
class Matrix(list):
    def __init__(self, n, m):
        super(Matrix, self).__init__()
        self.row_no = n
        self.column_no = m
        self.type = 'matrix'

        for el in range(m):
            self.append([0 for el in range(n)])

    def __repr__(self):
        max_len = self.max_len_element()
        output_str = ''
        for k in range(self.row_no):
            for s in range(self.column_no):
                if s == 0:
                    output_str += '| '
                output_str += ' ' + str(self.get_elem(k+1,s+1)) + ' '*(max_len - len(str(self.get_elem(k+1,s+1)))+1)
            output_str += '|\n'
        return output_str

    #  Функция определения самого длинного элемента матрицы
    def max_len_element(self):
        for k in range(self.row_no):
            for s in range(self.column_no):
                if k == 0 and s == 0:
                    m = len(str(self.get_elem(k+1, s+1)))
                if len(str(self.get_elem(k+1,s+1))) > m:
                    m = len(str(self.get_elem(k+1, s+1)))
        return m

    #  Функция получения значения элемента
    def get_elem(self, i, k):
        return self[k-1][i-1]

    #  Функция определения значения элемента
    def put_elem(self, i, k, value: float=0):
        self[k - 1][i - 1] = value

    #  Функция транспонирования матрицы
    def transpose(self):
        tr_matrix = Matrix(self.column_no, self.row_no)
        for k in range(self.row_no):
            k += 1
            for s in range(self.column_no):
                s += 1
                tr_matrix.put_elem(s, k, value=self.get_elem(k,s))
        return tr_matrix

    #  Функция умножения матрицы на число
    def multiply(self, m: float):
        if not isinstance(m, float):
            raise ValueError('Аргумент умножения не float')
        new_mat = Matrix(self.row_no, self.column_no)
        for k in range(self.row_no):
            k += 1
            for s in range(self.column_no):
                s += 1
                new_mat.put_elem(k, s, value=m*self.get_elem(k,s))
        return new_mat

    #  Функция вычисления минора ij
    def minor(self, row, col):
        if row > self.row_no or col > self.column_no:
            raise ValueError('Индексы в параметрах функции не должны превышать размерности матрицы ')
        new_mat = Matrix(self.row_no - 1, self.column_no - 1)
        for k in range(new_mat.row_no):
            k += 1
            for s in range(new_mat.column_no):
                s += 1

                if k >= row:
                    new_k = k + 1
                else:
                    new_k = k

                if s >= col:
                    new_s = s + 1
                else:
                    new_s = s
                new_mat.put_elem(k, s, value=self.get_elem(new_k,new_s))
        return new_mat

    def det(self):
        if self.column_no != self.row_no:
            raise ValueError('Попытка вычислить определитель неквадратной матрицы')

        if self.row_no == 2:
            return self.get_elem(1,1)*self.get_elem(2,2) - self.get_elem(1,2)*self.get_elem(2,1)
        elif self.row_no == 1:
            return self.get_elem(1,1)
        else:
            res = 0
            for k in range(self.row_no):
                k += 1
                res += self.get_elem(1, k)*(-1)**(1+k)*self.minor(1, k).det()
            return res

    def inverse(self):
        if self.column_no != self.row_no:
            raise ValueError('Попытка вычислить обратную матрицу неквадратной матрицы')
        new_mat = Matrix(self.row_no, self.column_no)
        for k in range(new_mat.row_no):
            k += 1
            for s in range(new_mat.column_no):
                s += 1
                v = (-1)**(k+s)*self.minor(s, k).det()/self.det()
                new_mat.put_elem(k, s, value=v)
        return new_mat


#  Функция сравнения двух матриц
def equals_mat(m1: Matrix, m2: Matrix ):
    if m1.column_no != m2.column_no or m1.row_no != m2.row_no:
        return False
    else:
        for k in range(m1.row_no):
            k += 1
            for s in range(m1.column_no):
                s += 1
                if m1.get_elem(k, s) != m2.get_elem(k, s):
                    return False
        return True


#  Функция суммирования двух матриц
def sum_mat(m1: Matrix, m2: Matrix):
    if m1.column_no != m2.column_no or m1.row_no != m2.row_no:
        raise ValueError('Ошибка! Размерности матриц не совпадают. Суммирование невозможно')
    new_mat = Matrix(m1.row_no, m1.column_no)
    for k in range(m1.row_no):
        k += 1
        for s in range(m1.column_no):
            s += 1
            new_mat.put_elem(k, s, value=m1.get_elem(k, s) + m2.get_elem(k, s))
    return new_mat


#  Функция умножения двух матриц
def mul_mat(m1: Matrix, m2: Matrix):
    if m1.column_no != m2.row_no:
        raise ValueError('Ошибка! Матрицы не подходят для перемножения!')
    new_mat = Matrix(m1.row_no, m2.column_no)
    for k in range(m1.row_no):
        k += 1
        for s in range(m2.column_no):
            s += 1
            element = 0
            for q in range(m1.column_no):
                element += m1.get_elem(k, q+1) * m2.get_elem(q+1, s)

            new_mat.put_elem(k, s, value=element)
    return new_mat


#  Функция создания единичной матрицы размера n
def unit_mat(n):
    new_mat = Matrix(n, n)
    for k in range(new_mat.row_no):
        for s in range(new_mat.column_no):
            if k == s:
                new_mat.put_elem(k + 1, s + 1, value=1)
            else:
                new_mat.put_elem(k + 1, s + 1, value=0)
    return new_mat




