#ifndef K_MEANS_H //I don't really need an include guard for this file, but I include it for safety's sake
#define K_MEANS_H

int distance(double p1[], double p2[]);
double k_means(int k, double** centers, double** dataset, double*** clusters, int maxIndex);
#endif
