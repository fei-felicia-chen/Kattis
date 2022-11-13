#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int main()
{
    pair<int,int> jump_dir[] = { make_pair(-2, 1),
                        make_pair(-2, -1),
                        make_pair(1, 2), 
                        make_pair(1, -2), 
                        make_pair(2, 1),
                        make_pair(2, -1),
                        make_pair(-1, -2),
                        };
    int n;
    cin >> n;
    int x, y;
    vector<string> arr;
    vector<vector<bool>> visited;
    string tmp;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        arr.push_back(tmp);
        size_t found = tmp.find('K');
        if (found != string::npos)
        {
            x = i;
            y = found;
        }
        vector<bool> tmp_vect;
        for (int j = 0; j < n; j++)
            tmp_vect.push_back(false);
        visited.push_back(tmp_vect);
    }

    deque<tuple<int, int, int>> q;
    q.push_back(make_tuple(x, y, 0));
    while (q.size() > 0)
    {
        x = get<0>(q.front());
        y = get<1>(q.front());
        int score = get<2>(q.front());
        if (x == 0 && y == 0)
        {
            cout << score;
            return 0;
        }
        for (auto p : jump_dir)
        {
            int tmp_x = p.first + x;
            int tmp_y = p.second + y;
            if (tmp_x >= 0 && tmp_x < n && tmp_y >= 0 && tmp_y < n && arr[tmp_x][tmp_y] == '.' && !visited[tmp_x][tmp_y])
            {
                q.push_back(make_tuple(tmp_x, tmp_y, score + 1));
                visited[x][y] = true;
            }
        }
        q.pop_front();
    }
    cout << -1;
    return 0;
}
