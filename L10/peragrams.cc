#include <iostream>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
    set<char> letters;
    string s;
    cin >> s;

    // Add every unique character to set and erase if pair is found
    for (char &c : s)
    {
        if (letters.count(c))
            letters.erase(c);
        else
            letters.insert(c);
    }
    
    // Compute and output characters missing
    int n = letters.size() - 1;
    int res = (n <= 0) ? 0 : n;
    cout << res;
    return 0;
}
