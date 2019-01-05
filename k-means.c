#include <math.h>
/*Returns the square of the euclidean distance between two 2D points. Since the only thing that is important in K-Means clustering is relative disnce, i.e. is this point further from this center or this center, and not the actual distance we don't take the root of this number because calling sqrt() would be expensive.*/
//TODO make this n-dimensional
int distance(double p1[], double p2[]){
	return pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2);
}
