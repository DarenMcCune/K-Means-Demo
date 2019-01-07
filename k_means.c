#include <math.h>
#include <limits.h>
#include <stdio.h>
/*Returns the square of the euclidean distance between two 2D points. Since the only thing that is important in K-Means clustering is relative disnce, i.e. is this point further from this center or this center, and not the actual distance we don't take the root of this number because calling sqrt() would be expensive.*/
//TODO make this n-dimensional
int distance(double p1[], double p2[]){
	return pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2);
}

double k_means(int k, double** centers, double** dataset,  double*** clusters, int maxindex){
	double point[2], center[2], minDistance, minDistanceCenter, totalDistance, curDistance;
	int pointIndex, centerIndex, minDistanceIndex, i;
	for(pointIndex=0; pointIndex<maxindex; pointIndex++){
		minDistance=INT_MAX;
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
		for(i=0; i<k; i++){
			if(i==minDistanceIndex){
				clusters[i][0][pointIndex]=point[0];
				clusters[i][1][pointIndex]=point[1];
			}
			else{
				clusters[i][0][pointIndex]=NAN;
				clusters[i][1][pointIndex]=NAN;
			}
		}
	}
	return totalDistance;
}

int tester(float** centers){
	int i,j;
	printf("%f\n", centers[0][0]);
	puts("{");
	for(i=0;i<2; i++){
		printf("{");
		for(j=0; j<2; j++){
			printf("%f,", centers[i][j]);
		}
		printf("},");
	}
	printf("\n");
}