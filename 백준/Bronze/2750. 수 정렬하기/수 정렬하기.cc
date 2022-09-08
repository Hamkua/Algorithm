#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int array[1001];

int main(void) {
	int N,i,j, temp, index;
	
	
	scanf("%d", &N);
	for ( i = 0; i < N; i++) {
		scanf("%d", &array[i]);
	}
	//삽입 정렬
	
	for (i = 0; i <N-1; i++) {
		j = i;
		while(array[j]>array[j+1] && j>=0){
			temp = array[j];
			array[j] = array[j + 1];
			array[j + 1] = temp;
			if(j>0) j--;
	
		}
	}

	//출력
	for (i = 0; i < N; i++) {
		printf("%d\n", array[i]);
	}
	return 0;
}