# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
#                O              T

def find_middle_node_of_linked_list(ll):
    runner_one = ll.head
    runner_two = ll.head.next

    while runner_two.next and runner_two.next.next:
        runner_one = runner_one.next
        runner_two = runner_two.next.next
    
    while runner_two.next:
        runner_one, runner_two = runner_one.next, runner_two.next

    return runner_one