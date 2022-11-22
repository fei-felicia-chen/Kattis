#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    while (n--)
    {
        int s, d;
        cin >> s >> d;
        if (d > s || (s + d) & 1)
            printf("impossible\n");
        else
        {
            int x = (s + d) / 2;
            int y = s - x;
            printf("%d %d\n", x, y);
        }
    }
    return 0;
}
