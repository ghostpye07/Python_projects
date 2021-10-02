//C++ implementation of groovingmonkeyproblem by niyalimukherjee 
#include"bits/stdc++.h"
using namespace std;
int main()
{
    int t,N;
    cin>>t;
    cin>>N;
    int monkeys[N];
    for(int i=0;i<N;i++)
    {
        cin>>monkeys[i];
    }
    int b[N];
    int c=0;
    
    for(int i=0;i<N;i++)
    {
        b[(i+1)%N]=monkeys[i];
        c++;
        if(b[i]==monkeys[i])
        break;
    }
    cout<<c<<endl;
    
}

