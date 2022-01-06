import drawing

dimension: int = int(input("Dimension: "))
filename: str = input("FileName: ")
"""
choose in wich dimension draw
"""

force: bool = False
vertex: int = 4  # square definition
plan = []
"""
## Create a cube constructor where constructor is a modulable 3 dimension plan like :  
### X -> 0 : [0,0,0]
### Y -> 1 : [0,0,0]
### Z -> 2 : [0,0,0]
"""

instruction = {
    0: drawing.square,
    1: drawing.difference,
    2: drawing.reliable,
    3: drawing.fill,
    False: drawing.stop
}


def dimension_attrib(payload: list[dict[int | bool]], dimension: int) -> None:
    for u in range(0, len(payload)):
        for s in range(0, len(payload[u])):
            payload[s] = 1

"""
The instruction the programm has to follow when the array has a certain value
"""
for i in range(0, dimension):
    surface = [[0] * 3] * dimension
    dim_n = {i: surface[i]}
    plan.append(dim_n)

print(plan)

for _ in range(2, dimension):
    vertex *= 2
        
print("sommets: ", vertex)
FaceDim = dimension * 2
ArreteDim = (vertex * dimension)/2
print("arrêtes: ", ArreteDim)

get_values = lambda key, inputData: [subval[key] for subval in inputData if key in subval]
#drawing.init(0, 0)

for x in range(0, len(plan)):
    print(get_values(x, plan)[0])
    print(sum(get_values(x, plan)[0]))
    instruction[sum(get_values(x, plan)[0])]()
    end: str = drawing.save(filename)
    print(end)
#while (arck.check_len(len(plan), plan) is True) and (force is not True):


