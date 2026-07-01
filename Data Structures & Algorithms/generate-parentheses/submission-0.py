class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We need to start with an opening parenthesis
        # We can not decide if we want to close this parenthesis, or open another one
        # This forms a decision tree
        # At each node we can decide to close a previous pratenthesis or open a new level

        # Constraints:
        # - Number of opening parenthesis == n
        # - Valid parenthesis closures

        # To make sure parenthesis are valid, we can use a stack
        # When we open a new parenthesis, we can append the closing prenthesis in the stack
        # At each child node we can decide if we want to open a new parenthesis or pop from stack
        # Popping from stack is just closing a parenthesis.

        # Approach:
        # We keep track of a counter i for each branch in decision tree.
        # If i == n, we pop remaining values from the stack and add the permutation to result
        # If i < n, we can open new levels of parenthesis

        result = []
        permutation = []

        def backtrack(i: int, c: int):
            if i == n and c == n:
                result.append("".join(permutation))
                return
            
            if i < n:
                permutation.append("(")
                backtrack(i + 1, c)
                permutation.pop()

            if c < i:
                permutation.append(")")
                backtrack(i, c + 1)
                permutation.pop()

        backtrack(0, 0)
        return result