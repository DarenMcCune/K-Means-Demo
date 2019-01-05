all: k-means.o test.c
	gcc -o test test.c k-means.o -lm
clean:
	rm *.o test
