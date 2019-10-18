#include <bits/stdc++.h>
#include <stdlib.h>
#include <time.h>
#define lli long long int
using namespace std;

lli extgcd(lli a,lli b, lli &x, lli &y){
  if(b==0){
    x=1,y=0;
    return a;
  }
  lli x1,y1;
  lli d=extgcd(b,a%b,x1,y1);
  x=y1;
  y=x1-(a/b)*y1;
  return d;
}

lli inverso(lli a,lli  m){
  lli a_inv, basura;
  if(1==extgcd(a,m,a_inv,basura))
  return a_inv;
  else{ 
    cout << a << " No tiene inverso"<<endl;
    cout << basura << endl;
    return 0;
  }

}

lli exp(lli b ,lli x, lli n){
  lli z=1;
  lli l=0;
  lli aux=b;
  while(aux=aux>>1)l++;
  for(int i=l;i>=0;i--){
    z=(z*z)%n;
    if((1<<i)&b){
      z=(z*x)%n;
    }
  }
  return z;
}

bool primalidad(lli n){
  if(!n%5)return false;
  lli k,m,o;
  lli b,a;
  k=0;
  o=n-1;
  while(!(o%2))k++,o/=2;
  m=(n-1)/(1<<k);
  srand(time(NULL));
  do{a=rand()%(n-1);}while(!a%5);
  b=exp(m,a,n);
  if(b==1)return true;
  for(int i=0;i<k;i++){
    if(b==-1)return true;
    else b=(b*b)%n;
  }
  return false;
}


int main(){
  lli a =inverso(121,51504);
  if(primalidad(99823)) cout << "si" <<endl;
  a=exp(71,2,99823);
  cout << a <<endl;
  a=exp(105,2,99823);
  cout << a <<endl;
  a=exp(105,17084,99823);
  a=(a*82)%99823;
  cout << a <<endl;
  a=exp(99751,45412,99823);
  cout << a <<endl;
  a=(a*70200)%99823;
  cout << a <<endl;
  return 0;
}
