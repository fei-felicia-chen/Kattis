#include <iostream>
#include <cmath>

using namespace std;

class A {
public:
    int a;
    A(int pA): a(pA)
    {}
    void print() {
        cout << a << endl;
    }
};

class B: A {
public:
    int b;
    B(int pA, int pB):
    A(pA),
    b(pB)
    {}
    void print() {
        cout << a << ", " << b << endl;
    }
};

int main() {
    A a = A(5);
    B b = B(2, 3);
    a.print();
    b.print();
    return 0;
}