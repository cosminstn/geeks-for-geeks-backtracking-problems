# Given a valid sentence without any spaces between the words and a dictionary of valid English words,
# find all possible ways to break the sentence in individual dictionary words.

# Example
# Consider the following dictionary
# { i, like, sam, sung, samsung, mobile, ice,
# and, cream, icecream, man, go, mango}
#
# Input: "ilikesamsungmobile"
# Output: i like sam sung mobile
# i like samsung mobile
#
# Input: "ilikeicecreamandmango"
# Output: i like ice cream and man go
# i like ice cream and mango
# i like icecream and man go
# i like icecream and mango


dict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "and", "cream", "icecream", "man", "go", "mango"]


def solve_part(to_solve, solution):
    if len(to_solve) == 0:
        return True
    if to_solve in dict:
        solution.append(to_solve)
        return True
    print(f"DEBUG: Called solvePart for input: {to_solve} solution: ")
    print(f"DEBUG {solution}")
    for word in dict:
        if to_solve.startswith(word):
            solution.append(word)
            return solve_part(to_solve[len(word):], solution)

    return False


def solve(to_solve):
    solution = []
    solve_part(to_solve, solution)
    print('Final solution: ')
    return solution


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solve("ilikesamsungmobile"))
