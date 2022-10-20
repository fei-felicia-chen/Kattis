#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

/*
 * Notes: 
 * - x, y, z coords are stored as int values, as the example uses int values
 * - printDistance from Point2D is overridden in Point3D
 * - although printDistance does not actually requires a Point2D or Point3D,
 *   I still declared it as a method (could declare friend)
 */
class Point2D
{
protected: // Protected so that Point3D can access these fields
    int x;
    int y;

public:
    Point2D(int param_x, int param_y):
    x(param_x),
    y(param_y)
    {
        // Only Constructor
    }

    ~Point2D()
    {
        cout << "Point2D Destructor was called";
    }

    double dist2D(Point2D p)
    {
        return sqrt(pow((this->x - p.x), 2) + pow((this->y - p.y), 2));
    }

    void printDistance(double d)
    {
        cout << "2D distance = " << ceil(d) << endl;
    }
};

class Point3D: public Point2D
{
private:
    int z;

public:
    Point3D(int param_x, int param_y, int param_z):
    Point2D(param_x, param_y),
    z(param_z)
    {
        // Only Constructor
    }

    double dist3D(Point3D p)
    {
        return sqrt(pow((this->x - p.x), 2) + pow((this->y - p.y), 2) + pow((this->z - p.z), 2));
    }

    void printDistance(double d) // Overriding
    {
        cout << "3D distance = " << ceil(d) << endl;
    }
};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    // Initialize vars
    int x, y, z;

    // Read input
    cin >> x;
    cin >> y;
    cin >> z;

    // Create points
    Point2D p1_2D = Point2D(x, y);
    Point3D p1_3D = Point3D(x, y, z);

    // Read input
    cin >> x;
    cin >> y;
    cin >> z;

    // Create points
    Point2D p2_2D = Point2D(x, y);
    Point3D p2_3D = Point3D(x, y, z);

    // Compute distances
    double dist_2D = p1_2D.dist2D(p2_2D);
    double dist_3D = p1_3D.dist3D(p2_3D);

    // Output distances
    p1_2D.printDistance(dist_2D);
    p1_3D.printDistance(dist_3D);

    return 0;
}