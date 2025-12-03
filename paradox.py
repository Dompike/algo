import sys

def read_input():
    try:
        data = sys.stdin.read().split()
        if not data:
            return None
    except Exception:
        return None
    
    test_cases = []
    data_ptr = 0
    
    while data_ptr < len(data):
        try:
            N = int(data[data_ptr])
            data_ptr += 1
        except (ValueError, IndexError):
            break

        if N == 0:
            break
        
        statements = []
        for _ in range(N):
            if data_ptr + 2 > len(data):
                return test_cases
            X = int(data[data_ptr])
            S = data[data_ptr + 1]
            statements.append((X, S))
            data_ptr += 2
        
        test_cases.append((N, statements))
        
    return test_cases


def check_consistency(N, statements, initial_guess_idx, initial_guess_value):
    state = [0] * (N + 1) 
    state[initial_guess_idx] = 1 if initial_guess_value else 2
    queue = [initial_guess_idx]
    
    while queue:
        i = queue.pop(0)
        X, S = statements[i - 1]
        i_is_true = (state[i] == 1)
        X_must_be_true = (S == "true"        
        required_X_value = (X_must_be_true == i_is_true)
        required_X_state = 1 if required_X_value else 2
        
        if state[X] == 0:
            state[X] = required_X_state
            queue.append(X)
        elif state[X] != required_X_state:
            return False

    return True

def solve():
    test_cases = read_input()
    if not test_cases:
        return
        
    output = []
    
    for N, statements in test_cases:
        
        is_paradoxical = False
        for i in range(1, N + 1):
            
            consistent_if_true = check_consistency(N, statements, i, True)
            
            consistent_if_false = check_consistency(N, statements, i, False)
            
            if not consistent_if_true and not consistent_if_false:
                is_paradoxical = True
                break
                
        output.append("PARADOX" if is_paradoxical else "NOT PARADOX")
        
    sys.stdout.write('\n'.join(output) + '\n')

solve()
