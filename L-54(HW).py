def direct_access(scores, index):
    """Method 1: Direct Access - O(1) Time"""
    try:
        return scores[index]
    except IndexError:
        return None


def linear_search(scores, target):
    """Method 2: Linear Search - O(n) Time"""
    for score in scores:
        if score == target:
            return True
    return False


def check_pairs(scores):
    """Method 3: Pair Comparison - O(n^2) Time"""
    n = len(scores)
    for i in range(n):
        for j in range(i + 1, n):
            if scores[i] == scores[j]:
                return True
    return False


# --- Sample Test Execution ---
if __name__ == "__main__":
    student_scores = [85, 92, 78, 92, 64, 89]
    
    print("Execution Results:")
    print("-" * 30)
    print(f"1. Direct Access (Index 2): {direct_access(student_scores, 2)}")
    print(f"2. Linear Search (Target 64): {linear_search(student_scores, 64)}")
    print(f"3. Pair Comparison (Any duplicates?): {check_pairs(student_scores)}")
