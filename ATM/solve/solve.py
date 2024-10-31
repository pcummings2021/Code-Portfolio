import ctypes
import time
from pwn import *


binary = args.BIN

context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary)
r = ROP(e)

gs = '''
continue
'''

def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote("spaceheroes-atm.chals.io", 443, ssl=True, sni="spaceheroes-re-atm.chals.io")
    else:
        return process(e.path)

p = start()

p.recvuntil('Option: \n')
p.sendline('w')
p.recvuntil('Amount: \n')

libc = ctypes.CDLL(None)
libc.srand.argtypes = [ctypes.c_uint]
libc.srand(int(time.time()))

random_number = libc.rand()

p.sendline(random_number)

p.interactive()
