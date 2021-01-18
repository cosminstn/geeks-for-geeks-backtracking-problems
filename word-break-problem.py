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


def solve_part(to_solve, solution, all_solutions):
    if len(to_solve) == 0:
        all_solutions.append(solution)
        return True
    if to_solve in dict:
        solution.append(to_solve)
        all_solutions.append(solution)
        return True
    print(f"DEBUG: Called for to_solve: {to_solve} & current solution: {solution}")
    for word in dict:
        if to_solve.startswith(word):
            solution.append(word)
            return solve_part(to_solve[len(word):], solution, all_solutions)

    return False


def solve(to_solve):
    all_solutions = []
    solve_part(to_solve, [], all_solutions)
    print('Final solution: ')
    return all_solutions


if __name__ == '__main__':
    print(solve("ilikesamsungmobile"))
