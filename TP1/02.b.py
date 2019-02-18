#b. Como elas podem ser obtidas pelo módulo ‘os’ de Python?

import os

print(os.environ)

print()

for a in os.environ:
    print(a, os.environ.get(a))