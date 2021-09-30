#include <bits/stdc++.h>
using namespace std;

int main()
{
    int m = 4, n = 4;
    int A[4][4] =
        {{1, 2, 3, 4},
         {5, 6, 7, 8},
         {9, 10, 11, 12},
         {13, 14, 15, 16}};
        
    int k = 15;
    for(int i = 0; i<m; i++){
        for(int j = 0; j<m; j++){
            if(A[i][j] == k){
                cout << ++i <<'\t' << ++j << endl;
                break;
            }
        }
    }
    return 0;

}