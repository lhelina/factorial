#include <iostream>
using namespace std;

int main() {
    int n = 121;
    int temp = n;
    int rev = 0;

    while(temp > 0) {
        int digit = temp % 10;
        rev = rev * 10 + digit;
        temp = temp / 10;
    }

    if(n == rev) {
        cout << n << " is palindrome" << endl;
    } else {
        cout << n << " is not palindrome" << endl;
    }

    return 0;
}
