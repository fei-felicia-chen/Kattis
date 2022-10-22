//https://open.kattis.com/problems/repeatingdecimal

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b, c;
    while (cin >> a >> b >> c) {
        cout << "0.";
        while (c--)
        {
            a *= 10;
            long x = a / b;
            cout << x;
            a -= b * x;
        }
        cout << endl;
    }
    return 0;
}
