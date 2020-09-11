question_23: justify.o word.o line.o
	gcc -o question_23 justify.o word.o line.o

justify.o: justify.c line.h line.c word.h word.c
	gcc -g -c justify.c

word.o: word.c word.h
	gcc -g -c word.c word.h

line.o: line.c line.h
	gcc -g -c line.c line.h

