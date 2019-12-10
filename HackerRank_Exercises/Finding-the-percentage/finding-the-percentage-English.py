if __name__ == '__main__':

    n = int(input())
    student_marks = {}

    search_marks = []

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    search_marks = student_marks[query_name]
    avg_marks = search_marks[0] + search_marks[1] + search_marks[2]

    print("{0:.2f}".format(avg_marks/3))