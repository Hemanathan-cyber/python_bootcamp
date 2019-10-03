#include<iostream>
using namespace std;
int main()
{
    int n,k;
    cin>>n>>k;
    int a[n];
    int count=0;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        if(a[i]==k)
        count++;
    }
    if(count==0)
    cout<<-1<<endl;
    else
    cout<<count-1<<endl;
    return 0;
}
