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
            label = int(pressed[1])
            same_lab_pos = array.index(label)
            positions.append(same_lab_pos)
            return str(array[same_lab_pos])
        elif prompt == 2:
            label = int(pressed[0])
            same_lab_pos = array.index(label)
            positions.append(same_lab_pos)
            return str(array[same_lab_pos])
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
        prompt = array[-1]
        if prompt == 1:
            return str(array[positions[0]])
        elif prompt == 2:
            return str(array[positions[1]])
        elif prompt == 3:
            return str(array[positions[2]])
        elif prompt == 4:
            return str(array[positions[3]])

    pressed.append(stage_one(array_of_arrays[0]))
    pressed.append(stage_two(array_of_arrays[1]))
    pressed.append(stage_three(array_of_arrays[2]))
    pressed.append(stage_four(array_of_arrays[3]))
    pressed.append(stage_five(array_of_arrays[4]))
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