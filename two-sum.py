# Two Sum


def twoSum(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if (
            diff in prevMap
        ):  # Se eu já vi antes o número que falta para atingir o alvo, retorno a posição onde o vi antes (prevMap[diff]) e a posição atual (i)"
            return [prevMap[diff], i]
        prevMap[n] = i


nums = [2, 11, 11, 7]
target = 9
result = twoSum(nums, target)
print(result)
