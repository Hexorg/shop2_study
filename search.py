# Study of the SHOP2 algorithm from
# https://www.cs.umd.edu/~nau/papers/nau2001total-order.pdf
# LISP implementation - https://github.com/cl-axon/shop2

import random

def reduction(S, task):
    # if t is a primitive task then return <t,NIL>
    if task.is_primitive():
        return (task, None)
    # else if no method is applicable to t in S then return <FAIL,NIL>
    applicable_methods = filter(lambda method: method.is_applicable(S), task.methods)
    elif len() == 0:
        task.is_fail = True
        return (task, None)
    # nondeterministically let m be any method applicable to t in S

def SHOP2(S, M, L):
    '''
    S is the current state, 
    M is a partially ordered set of tasks
    L is a list of protected conditions
    '''
    if len(M) == 0:
        return None
    # nondeterministically choose a task t in M that has no predecessors
    task = random.choice(filter(lambda task: len(task.predecessors) == 0, M))
    # <r,R’> = reduction(S,t)
    r, Rp = reduction(S, task)
    if r.is_fail:
        return Exception("r failed after reduction")
    # nondeterministically choose an operator instance o applicable to r in S (current state)
    o = random.choice(filter())
    # S’ = the state produced from S by applying o to r
    Sp = o.apply(r)
    # L’ = the protection list produced from L by applying o to r
    Lp = o.protection(L, r)
    # M’ = the partially ordered set of tasks produced from M by replacing t with R’
    Mp = M.replace(t, Rp)
    P = SHOP2(Sp,Mp,Lp)
    return cons(o,P)

if __name__ == '__main__':
    start = State('start')
    goal = State('goal')



    print(search(start, goal, Domain(), lambda n: 50.0 if n.name == 'start' else 40.0 if n.name == 'l1' else 30.0 if n.name == 'l2' else 0.0 if n.name == 'goal' else 25.0))
