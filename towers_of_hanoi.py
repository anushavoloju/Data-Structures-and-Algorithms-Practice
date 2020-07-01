# return the steps to move all disks from source to destination through auxillary
# Source - S, Auxillary - A, Destination - D

def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    tower_of_Hanoi_solution(num_disks, 'S','A','D')

def tower_of_Hanoi_solution(num_disks, source, auxillary, destination):
    if num_disks == 0:
        return
    elif num_disks == 1:
        print("{} {}".format(source,destination))
        return
    elif num_disks > 1:
        tower_of_Hanoi_solution(num_disks - 1, source, destination, auxillary)
        print("{} {}".format(source,destination))
        tower_of_Hanoi_solution(num_disks - 1, auxillary, source, destination)

print(tower_of_Hanoi(4))