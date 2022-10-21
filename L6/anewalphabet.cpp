/*"""https://open.kattis.com/problems/anewalphabet"""*/
#include <iostream>
#include <map>

using namespace std;

map<char, string> d = {
    {'a', "@"},
    {'b', "8"},
    {'c', "("},
    {'d', "|)"},
    {'e', "3"},
    {'f', "#"},
    {'g', "6"},
    {'h', "[-]"},
    {'i', "|"},
    {'j', "_|"},
    {'k', "|<"},
    {'l', "1"},
    {'m', "[]\\/[]"},
    {'n', "[]\\[]"},
    {'o', "0"},
    {'p', "|D"},
    {'q', "(,)"},
    {'r', "|Z"},
    {'s', "$"},
    {'t', "']['"},
    {'u', "|_|"},
    {'v', "\\/"},
    {'w', "\\/\\/"},
    {'x', "}{"},
    {'y', "`/"},
    {'z', "2"},
};

int main(int argc, char const *argv[])
{
    string input;
    getline(cin, input);
    for (char c: input) {
        c = tolower(c);
        if (d.count(c))
            cout << d[c];
        else
            cout << c;
    }
    return 0;
}
