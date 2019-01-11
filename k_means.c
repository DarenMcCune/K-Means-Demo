#include <math.h>
#include <float.h>
#include <stdio.h>
/*Returns the square of the euclidean distance between two 2D points. Since the only thing that is important in K-Means clustering is relative disnce, i.e. is this point further from this center or this center, and not the actual distance we don't take the root of this number because calling sqrt() would be expensive.*/
//TODO make this n-dimensional
double distance(double p1[], double p2[]){
	return pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1], 2);
}

double k_means(int k, double** centers, double** dataset,  __int8_t** clusters, int maxindex){
	double point[2], center[2], minDistance, minDistanceCenter, totalDistance, curDistance;
	int pointIndex, centerIndex, minDistanceIndex, i;
	for(pointIndex=0; pointIndex<maxindex; pointIndex++){
		
		minDistance=DBL_MAX;
		point[0]=dataset[0][pointIndex];
		point[1]= dataset[0][pointIndex];
		for(centerIndex=0; centerIndex<k; centerIndex++){
			center[0]=centers[0][centerIndex];
			center[1]=centers[1][centerIndex];
			curDistance=distance(point,center);
			if(curDistance<minDistance){
				minDistanceIndex=centerIndex;
				minDistance=curDistance;
			}
		}
		totalDistance+=minDistance;
		//TODO Merge these two loops into one
		for(i=0; i<k; i++){
			if(i==minDistanceIndex){
				clusters[i][pointIndex]=1;
			}
			else{
				clusters[i][pointIndex]=0;
			}
		}
	}
	printf("Blah is %f\n", totalDistance);
	return totalDistance;
}
