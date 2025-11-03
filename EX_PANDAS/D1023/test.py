def solution(my_string, queries):
    string = list(my_string)
    for i in range(len(queries)):
        reverse = my_string[queries[i][0]:queries[i][1]+1]
        reverse = reverse[::-1]
        for j in range(queries[i][0],queries[i][1]+1):
            string[j] = reverse[j-queries[i][0]]
    
    answer = ''
    for i in string:
        answer += i
    return answer

result = solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])