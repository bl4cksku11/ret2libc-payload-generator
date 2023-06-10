# ret2libc-payload-generator

**Author: Jose Rivas (Aka. BlackSkull)**

## What is a RET2LIBC attack?
Ret2libc is a type of exploit that takes advantage of a vulnerability in a program to bypass its security mechanisms and gain control of the program's execution flow. This technique is used to launch arbitrary code execution attacks when the target binary is running on a system with ASLR and NX protections enabled.

The ret2libc exploit is carried out by overwriting the saved return address on the stack with the address of a function from the libc library, such as system(). This function is then called with the address of a string that contains the shell command to be executed.

## What does this script do?
This script is a payload generator for a ret2libc exploit. This script takes your input for the EIP (Extended Instruction Pointer) offset, base address of the libc library, offset of the system() function, offset of the exit() function, and the offset of the /bin/sh string. These addresses are then packed using the struct.pack() function and appended to a string of NOP (\x90) instructions, which is used to fill the buffer until it reaches the saved return address.

Finally, the payload is printed to the console for use in a ret2libc attack. The payload will overwrite the saved return address with the address of system() function and pass the address of the /bin/sh string as an argument to execute a shell. 

### Note
It's important to note that this script is just a payload generator and the exploit itself must be crafted and executed separately to target a specific program with a vulnerability that can be exploited using ret2libc technique.


## Usage
1. Clone the repository:
```bash
git clone https://github.com/bl4cksku11/ret2libc-payload-generator.git
```

3. Move to ret2libc-payload-generator:
```bash
cd ret2libc-payload-generator
```

5. You must configure the addresses within the script before running it. Replace #here message comments with your addresses.

7. Run the script:
```bash
python getpayload.py
```
