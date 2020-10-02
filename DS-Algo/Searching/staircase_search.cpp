#include<iostream>

using namespace std;

int main(){
	int n;
	int val = 1;
	cin >> n;
	int a[10][10];
	for(int i = 0;i < n;i++){
		for(int j = 0;j < n;j++){
			a[i][j] = val;
			val++;
		}
	}
	for(int i = 0;i < n;i++){
		for(int j = 0;j < n;j++){
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}

	int key;
	cout<<"Enter Key to Search:";
	cin >> key;
	int cols = n-1;
	bool flag = false;
	for(int i = 0;i<n;i++){
		while(cols>=0){
			if(key == a[i][cols]){
				cout<<"Element Found at:"<<i<<"-"<<cols<<endl;
				flag = true;
				break;
			}
			if(key > a[i][cols]){
				break;
			}
			else{
				cols--; 
			}
		}
	}
	if(flag == false){
		cout<<"Element Not Found"<<endl;
	}
}