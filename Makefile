all: k_means.o test.c
	gcc -o test test.c k_means.o -lm
clean:
	rm *.o test
