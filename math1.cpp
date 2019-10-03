#include <iostream>
using namespace std;
int main() {
    int n,digit;
  cin>>n;
  int sum=0;
  while(n)
  {
  digit=n%10;
  sum+=digit;
  n/=10;}
  if(sum%3==0)
    cout<<"Yes";
  else
    cout<<"Not";
    return 0;
}
