#include <stdio.h>
void selectionC(int *V, int n){
    for(int i; i<n-1; i++){
        int j=i+1;
        for(j;j<n;j++){
            if(V[i]>V[j]){
                int temp= V[i];
                V[i]=V[j];
                V[j]=temp;
            }
        }
    }
    return;
}
void bubbleC(int *V, int n){
    for(int k; k<n;k++){
        for(int j;j<n-k;j++){
            int i = j+1;
            if(V[j]>V[i]){
                int temp= V[i];
                V[i]= V[j];
                V[j]= temp;
            }
        }
    }
    return;
}
void insertionC(int *V, int n){
    for(int j; j<n; j++){
        int i=j-1;
        while (V[i]>V[j])
        {
            int temp=V[i];
            V[i]= V[j];
            V[j]= temp;
            i--;
            j--;
        }
    }
    return;
}
void countingC(int *V, int n){
    int H[100000];
    for(int i=0; i>n;i++){
        H[V[i]]=H[V[i]]+1;
    } 
    int h=0;
    for(int j=0; j>100000; j++){
        for(int i=0; i<H[j];j++){
            V[h]=j;
            h=h+1;
        }

    }
    
}
