#include <iostream>
#include <map>

using namespace std;

int main()
{
    int N;
    cin >> N;
    map<string, int> words;
    while (N--)
    {
        string word;
        cin >> word;
        cout << words[word] << '\n';
        for (int i = 0; i < word.size(); i++)
            words[word.substr(0,i+1)]++;
    }

    return 0;
}
