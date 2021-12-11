from math import floor

arr = []
auto_complete_scores = []
syntax_error_score = 0
auto_complete_score_table = [')', ']', '}', '>']
error_score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
segments = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

with open('input.txt') as f:
    arr = [i.strip() for i in f]

for i, line in enumerate(arr):
    auto_complete_score = 0
    object_stack = []
    for j in line:
        if j in segments.keys():
            object_stack.append(j)
        if j in segments.values():
            if j == segments[object_stack[-1]]:
                object_stack.pop(-1)
            else:
                syntax_error_score += error_score_table[j]
                break
    else:
        for j in object_stack[::-1]:
            auto_complete_score = 5 * auto_complete_score + \
                auto_complete_score_table.index(segments[j]) + 1
        auto_complete_scores.append(auto_complete_score)

print("Syntax score error:", syntax_error_score)
print("Autocomplete score:", sorted(
    auto_complete_scores)[floor(len(auto_complete_scores)/2)])
