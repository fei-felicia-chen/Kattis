// https://open.kattis.com/problems/sortofsorting
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare_first_two(const string &a, const string &b)
{
    // compare first two letters
    if (a[0] == b[0])
        return a[1] < b[1];                 
    else
        return a[0] < b[0];                 
}

int main()
{
    int n;
    vector<string> last_names;
    while (cin >> n && n != 0)
    {
        last_names.clear();
        while (n--)
        {
            string last_name;
            cin >> last_name;
            last_names.push_back(last_name);
        }
        stable_sort(last_names.begin(), last_names.end(), compare_first_two);
        for (string nom : last_names)
            cout << nom << endl;
        cout << endl;
    }
    return 0;
}
