#! env python3

import dataclasses

@dataclasses.dataclass
class BallAt:
    x: int
    def __rshift__(self, num: int): self.x += num
    def __lshift__(self, num: int): self.x -= num
    def __matmul__(self, num: int): self.x = num
    def __repr__(self):
        return '|' + '-' * self.x + '@' + '-' * (30 - self.x) + '|'

if __name__ == '__main__':
    print('Start with ball at 10:')
    b = BallAt(10)
    print(b)
    print('Move it 15 to the right:')
    b >> 15
    print(b)
    print('Scooch it left 3 a few times:')
    for _ in range(4):
        b << 3
        print(b)
    print('Set it to 20:')
    b @ 20
    print(b)
