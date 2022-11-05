#include <iostream>
#include <math.h>

using namespace std;

double area(int xa,int ya,int xb,int yb,int xc, int yc) { 
   return abs((xa*(yb-yc) + xb*(yc-ya)+ xc*(ya-yb)) / 2.0);
} 

int main(int argc, char const *argv[])
{
    int xa, ya, xb, yb, xc, yc, apple_trees, to_return = 0;
    cin >> xa >> ya >> xb >> yb >> xc >> yc >> apple_trees;
    double land = area(xa,ya,xb,yb,xc,yc);

    while (apple_trees--)
    {
        int applex, appley;
        cin >> applex >> appley;
        double land_tot = area(applex,appley,xb,yb,xc,yc);
        land_tot += area(xa,ya,applex,appley,xc,yc);
        land_tot += area(xa,ya,xb,yb,applex,appley);
        if (land_tot ==  land)
            to_return++;
    }

    printf("%.1f\n%d", land, to_return);
    return 0;
}
