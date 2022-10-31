// does not work
#include <iostream>
#include <set>
#include <map>
#include <vector>

using namespace std;

bool dfs(string s, set<string> s1, set<string> s2, map<string, set<string>> m)
{
    if (!s1.count(s) && !s2.count(s))
    {
        s1.insert(s);
    }
    for (string curr : m[s])
    {
        // Add to appropriate set
        if (!s1.count(curr) && !s2.count(curr))
        {
            if (s1.count(s))
            {
                s2.insert(curr);
                dfs(curr, s1, s2, m);
            }
            if (s2.count(s))
            {
                s1.insert(curr);
                dfs(curr, s1, s2, m);
            }
        }
        // Check if someone has to carry 2 sus items
        if (s1.count(s) && s1.count(curr) || s2.count(s) && s2.count(curr))
            return false;
    }
    return true;
}

int main()
{
    map<string, set<string>> m;
    vector<string> allIngredients;
    bool good = true;
    int N, M;
    string item;
    set<string> walter;
    set<string> jesse;

    cin >> N;
    while (N--)
    {
        cin >> item;
        allIngredients.push_back(item);
        set<string> aSet;
        m[item] = aSet;
    }

    cin >> M;
    while (M--)
    {
        string ingredient1, ingredient2;
        cin >> ingredient1 >> ingredient2;
        m[ingredient1].insert(ingredient2);
        m[ingredient2].insert(ingredient1);
    }

    for (string s : allIngredients)
    {
        if (!dfs(s, walter, jesse, m))
        {
            good = false;
            printf("impossible");
            break;
        }
    }

    if (good)
    {
        for (string s : walter)
            printf("%s ", s);
        printf("\n");
        for (string s : jesse)
            printf("%s ", s);
    }
    return 0;
}
