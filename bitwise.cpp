# include <bits/stdc++.h>
using namespace std;
int main(){


int n=234;

int p=1;
int sum=0;
while(n>0){
		int r=n%10;
		p=p*r;
		sum=sum+r;
		n=n/10;
}


cout<<p<<" "<<sum;
	}