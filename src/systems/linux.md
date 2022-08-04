# Linux

```{contents} Table of Contents
---
local:
---
```

## Terminology (TODO: Remove it)

- Kernel  
  The kernel is the program that manages the system, including (depending on the kernel model) hardware devices, memory, and CPU scheduling. It runs in a privileged CPU mode that allows direct access to hardware, called kernel mode.
- Process  
  An OS abstraction and environment for executing a program. The program runs in user mode, with access to kernel mode (e.g., for performing device I/O) via system calls or traps into the kernel.
- Thread  
  An executable context that can be scheduled to run on a CPU. The kernel has multiple threads, and a process contains one or more.
- Task  
  A Linux runnable entity, which can refer to a process (with a single thread), a thread from a multithreaded process, or kernel threads.
- Virtual memory  
  An abstraction of main memory that supports multitasking and oversubscription. It is, practically, an infinite resource.
- Kernel space  
  The virtual memory address space for the kernel.
- User space  
  The virtual memory address space for processes.
- User land  
  User-level programs and libraries (/usr/bin, /usr/lib...).
- Context switch  
  A switch from running one thread or process to another.
- Mode switch  
  A switch between kernel and user modes.
- Trap  
  A signal sent to the kernel to request a system routine (privileged action). Trap types include system calls, processor exceptions, and interrupts.
- Hardware interrupt  
  A signal sent by physical devices to the kernel, usually to request servicing of I/O. An interrupt is a type of trap.
  

## Kernel and User Modes

Kernel mode allows full access to devices and the execution of privileges instructions. User mode request privileges operations to kernel via system calls.

Switching between user and kernel modes is a mode switch.

## Protection Ring

mechanisms to protect data and functionality from faults (by improving fault tolerance) and malicious behavior (by providing computer security)
![](https://upload.wikimedia.org/wikipedia/commons/2/2f/Priv_rings.svg)<https://en.wikipedia.org/wiki/Protection_ring>

## Context Switch

Process of storing the system state for one task, so that task can be paused and another task resumed.

There are three potential triggers for a context switch:

1. Multitasking
2. Interrupt handling
3. User and Kernel mode switching


- <https://en.wikipedia.org/wiki/Context_switch>

## System Calls

Programmatic way in which a computer program requests a service from the kernel. System calls provide an essential interface between a process and the operating system.

System calls are generally not invoked directly, but rather via wrapper functions in glibc.

- <https://en.wikipedia.org/wiki/System_call>
- <https://man7.org/linux/man-pages/man2/syscalls.2.html>

