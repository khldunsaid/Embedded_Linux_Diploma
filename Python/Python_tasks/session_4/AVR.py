import os
import shutil

def generate_ddra_config():
    # Initialize a list to store the bit modes
    bit_modes = []

    # Loop to get input for each bit mode from 0 to 7
    for i in range(8):
        while True:
            mode = input(f"Please enter Bit {i} mode (in/out): ").strip().lower()
            if mode in ["in", "out"]:
                bit_modes.append(mode)
                break
            else:
                print("Invalid input. Please enter 'in' or 'out'.")

    # Generate the binary representation for DDRA
    ddra_binary = ''.join(['0' if mode == 'in' else '1' for mode in bit_modes])
    
    # Convert the binary representation to hexadecimal
    ddra_hex = hex(int(ddra_binary, 2)).upper()

    # Output the result
    # print(f"DDRA={ddra_hex[2:].zfill(2)}")
    # print(f"DDRA=0b {ddra_binary}")

    # create c file 
    fd = open ('/home/khldun/Python_course/config.c',"w")
    os.write(fd.fileno(),"void Init_PORTA_DIR { \n"
          f"DDRA=0b {ddra_binary}\n"
        "} \n".encode())
    
    fd.close()

    

# Run the function to generate DDRA configuration
generate_ddra_config()
