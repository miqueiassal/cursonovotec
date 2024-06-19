#include <stdio.h>
void selection(int *V, int n){
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
void bubble(int *V, int n){
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
void insertion(int *V, int n){
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
void counting(int *V, int n){
    
}
int main(){
    int W[10]={5,4,2,7,1,7,69,2};
    int *p=&W[0];
    selection(p, 10);
    for(int i; i<10; i++){
        printf("%d",W[i]);
    }
    return (0);
}