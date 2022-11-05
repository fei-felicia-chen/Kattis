#define _USE_MATH_DEFINES
#include <iostream>
#include <math.h>

using namespace std;

int dist(double x, double y) {
    double distance = sqrt(pow(x, 2) + pow(y, 2));
    return round(distance);
}

int main()
{
    int ncases;
    cin >> ncases;
    while (ncases--)
    {
        int ncommands;
        cin >> ncommands;
        double currx = 0, curry = 0;
        int angle = 0; 
        while (ncommands--)
        {
            string dir;
            int dist;
            cin >> dir >> dist;
            if (dir == "fd")
            {
                currx += dist * sin(angle * (M_PI / 180));
                curry += dist * cos(angle * (M_PI / 180));
            }
            else if (dir == "bk")
            {
                currx -= dist * sin(angle * (M_PI / 180));
                curry -= dist * cos(angle * (M_PI / 180));
            }
            else if (dir == "lt")
                angle += dist;
            else
                angle -= dist;
        }
        printf("%d\n", dist(currx, curry));
    }
    return 0;
}
