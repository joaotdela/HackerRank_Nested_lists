if __name__ == '__main__':
    students =[]
    for _ in range(int(input('Quantos estudantes'))):
        name = input('nome: ')
        score = float(input('score: '))
        students.append([name,score])
    grades = sorted(set(g for _, g in students))
    second_grade = grades[1]
    for name in sorted(n for n,g in students if g == second_grade):
        print(name)
