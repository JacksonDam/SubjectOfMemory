def memory(array_of_arrays):
    pressed = []
    positions = []
    def stage_one(array):
        prompt = array[-1]
        if prompt == 1 or prompt == 2:
            positions.append(1)
            return str(array[1])
        else:
            positions.append(prompt - 1)
            return str(array[prompt - 1])

    def stage_two(array):
        prompt = array[-1]
        if prompt == 1:
            positions.append(array.index(4))
            return "4"
        elif prompt == 3:
            positions.append(0)
            return str(array[0])
        else:
            positions.append(positions[0])
            return str(array[positions[0]])

    def stage_three(array):
        prompt = array[-1]
        if prompt == 1:
            positions.append(1)
            return pressed[1]
        elif prompt == 2:
            positions.append(0)
            return pressed[0]
        elif prompt == 3:
            positions.append(2)
            return str(array[2])
        else:
            positions.append(array.index(4))
            return "4"

    def stage_four(array):
        prompt = array[-1]
        if prompt == 1:
            positions.append(positions[0])
            return str(array[positions[0]])
        elif prompt == 2:
            positions.append(0)
            return str(array[0])
        else:
            positions.append(positions[1])
            return str(array[positions[1]])

    def stage_five(array):
        return str(array[positions[array[-1] - 1]])

    pressed.append(stage_one(array_of_arrays[0]))
    pressed.append(stage_two(array_of_arrays[1]))
    pressed.append(stage_three(array_of_arrays[2]))
    pressed.append(stage_four(array_of_arrays[3]))
    pressed.append(pressed[(array_of_arrays[4][-1]) - 1])

    return "".join(pressed)

# print(memory([[1,3,2,4,1],
#
#  [3,1,2,4,3],
#
#  [2,3,4,1,2],
#
#  [2,1,4,3,1],
#
#  [4,1,2,3,4]]))