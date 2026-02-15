#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int x;
    cout << "donner un entier svp: ";
    cin >> x;
    if(x%2==0)
    {
        cout << x << " est pair\n";
    }
    else
    {
        cout << x << " est impair\n";
    }
    return 0;
}