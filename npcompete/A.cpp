#include <iostream>
#include <cmath>
#include <set>

using namespace std;

void getDivisors(int n, set<int> *friends)
{
    //
}

int main()
{
    int n;
    cin >> n;
    set<int> friends;
    getDivisors(n, &friends);
    for (int x: friends)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}