// https://open.kattis.com/problems/periodicstrings
#include <iostream>

using namespace std;

bool kperiodic(int k, string s)
{
    // If s is not divisible by k, pass
    if (s.size() % k != 0){
        return false;   
    }

    // Get s[0:k] and compare
    string curr = (s.substr(0, k));
    string copy = s;
    while (copy.size() > 0)
    {
        if (copy.rfind(curr, 0) != 0)
            return false;
        copy = copy.substr(k, copy.size());                     // copy = copy[k:]
        curr = curr.back() + curr.substr(0, curr.size() - 1);   // shift curr string
    }
    return true;
}

int main()
{
    string s;
    cin >> s;
    for (int i = 1; i <= s.size(); i++)
    {
        if (kperiodic(i, s))
        {
            cout << i;
            break;
        }
    }
    return 0;
}
