#include <iostream>
#include <array>

using namespace std;

int main()
{
    int testcases;
    cin >> testcases;
    while (testcases--)
    {
        int tmp;
        cin >> tmp;
        cout << tmp << " ";
        int steps = 0;
        array<int, 20> heights;
        for (int i = 0; i < 20; i++)
            cin >> heights[i];

        // Insertion sort and count steps
        for (int i = 0; i < 20; i++)
        {
            int tmp = heights[i];
            int j = i - 1;
            while (j >= 0 && heights[j] > tmp)
            {
                heights[j + 1] = heights[j];
                j--;
                steps++;
            }
            heights[j + 1] = tmp;
        }
        cout << steps << '\n';
    }
    return 0;
}
