// https://open.kattis.com/problems/stringmatching
#include <iostream>

using namespace std;

int main()
{
    string pattern;
    string text;
    while (getline(cin, pattern))
    {
        getline(cin, text);
        size_t found = text.find(pattern);
        while (found != string::npos)
        {
            printf("%d ", found);
            found = text.find(pattern, found + 1);
        }
        cout << endl;
    }
    return 0;
}
