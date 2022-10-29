// DOES NOT WORK IDK WHY
#include <iostream>

using namespace std;

string shiftString(string s)
{
    s = s.back() + s.substr(0, s.size() - 1);
    return s;
}

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
        copy = copy.substr(k, copy.size());
        curr = shiftString(curr);
    }    
    return true;
}

int main(void)
{
    string s;
    cin >> s;
    for (int i = 1; i <= s.size(); i++)
    {
        if (kperiodic(i, s))
        {
            cout << i;
        }
    }
    return 0;
}
