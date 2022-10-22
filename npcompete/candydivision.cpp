#include <iostream>
#include <math.h>
#include <set>

using namespace std;

typedef long long ll;

set<int> divisors(int n)
{
    set<int> res({0});
    for (ll i = 1; i <= sqrt(n) + 2; i++)
    {
        if (n % i == 0)
        {
            if (n/i == i)
                res.insert(i - 1);
            else
            {
                res.insert(i - 1);
                res.insert(n / i - 1);
            }  
        }
    }
    return res;
}

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    set<int> res = divisors(n);
    for(int x: res)
    {
       cout << x << " ";
    }
    return 0;
}
