#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string>
#include <iostream>
#include<sys/ptrace.h>

#define BUFSIZE 16

int main()
{
	int pipefd[2];
	pid_t pid;
	char cbuf[BUFSIZE];
	if(ptrace(PTRACE_TRACEME)==-1){
		return 0;
	}
	
	if (pipe(pipefd) == -1) {
		perror("pipe()");
		exit(1);
	}
	
	__asm__ ("call L1+1\n\t" 
             "L1: xor %rax, %rax\n\t"
             "pop %rax\n\t"
             "add $0xa,%rax\n\t"
             "push %rax\n\t"
             "ret\n");
            
	printf("Decrypting...\n");
	snprintf(cbuf, BUFSIZE, "encypted key");
	
	for(int i =0;i<15; i++){
		cbuf[i] ^= 0x23;
	}
	
	Key real_key(cbuf);
	Bytes data("encypted flag");
	
	std::string flag = decrpy_string(data, real_key, 16);
	return 0;
}
