question23: justify.o question23.o word.o
			gcc -o question23 justify.o question23.o word.o

justify.o: justify.c question23.h question23.c word.h word.c
			gcc -c justify.c

question23.o: question23.c question23.h
			gcc -c question23.c

word.o: word.c word.h
		gcc -c word.c