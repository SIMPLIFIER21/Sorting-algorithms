#include<iostream>
using namespace std;

void cyclicSort(int arr[],int n){
   int i = 0;
   while (i<n)
   {
      int correct = arr[i] - 1; //if array starting from 1 
                                //if starting from 0  do only correct = arr[i];
      if(arr[i]!=arr[correct]){
          swap(arr[i],arr[correct]);
      }else{
          i++;
      }
   }
}

int main()
{
    int arr[] = {3,5,2,1,4};
    int n = sizeof(arr)/sizeof(int);
    cyclicSort(arr,n);
    for(int x:arr){
        cout<<x<<" ";
    }
    return 0;
}