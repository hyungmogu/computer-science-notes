question_23: question_23.o word.o line.o
	gcc -o question_23 question_23.o word.o line.o

question_23.o: question_23.c line.h line.c word.h word.c
	gcc -c question_23.c

word.o: word.c word.h
	gcc -c word.c word.h

line.o: line.c line.h
	gcc -c line.c line.h

