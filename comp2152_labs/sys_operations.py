import os
import platform
import socket

# Print system-related information
print(f"Machine type: {platform.machine()}")
print(f"Processor type: {platform.processor()}")
socket.setdefaulttimeout(50)
print(f"Default socket timeout: {socket.getdefaulttimeout()} seconds")
print(f"Operating system: {platform.system()}")
print(f"Current process ID: {os.getpid()}")

# Fork a new process (Unix-based systems only)
if hasattr(os, "fork"):
    pid = os.fork()
    if pid == 0:  # Child process
        print(f"Child process ID: {os.getpid()}")
        exit()
    else:  # Parent process
        print(f"Parent process ID: {os.getpid()}")
        os.wait()

# File operations using os module
file_name = "fdpractice.txt"
fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

# Print process ID
print(f"Current process ID: {os.getpid()}")

# Write to file
os.write(fd, b"Some string to write to the file")
os.lseek(fd, 0, os.SEEK_SET)  # Move file pointer to the beginning

if hasattr(os, "fork"):
    pid = os.fork()
    if pid == 0:  # Child process
        print(f"Child process ID: {os.getpid()}")
        data = os.read(fd, 100)  # Read file contents
        print(f"File contents: {data.decode()}")
        os.close(fd)
        exit()
    else:  # Parent process
        print(f"Parent process ID: {os.getpid()}")
        os.wait()
        os.close(fd)
