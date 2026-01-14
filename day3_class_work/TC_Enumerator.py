fruits=['apple', 'banana', 'orange']
for index, value in enumerate(fruits):
    print(index, value)

from enum import Enum

class color(Enum):
    RED=1
    GREEN=2
    BLUE=3
print(color.RED.value)
print(color.GREEN.name)
print(color.BLUE.value)