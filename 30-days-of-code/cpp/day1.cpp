#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
    
    
    // Declare second integer, double, and String variables.
    int intNum;
    double doubleNum;
    string stringName;
    // Read and save an integer, double, and String to your variables.
    cin >> intNum;
    cin >> doubleNum;
    cin.ignore();
    getline(cin, stringName);
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    // Print the sum of both integer variables on a new line.
    int addNum;
    addNum = intNum + i;
    cout << addNum << '\n';
    // Print the sum of the double variables on a new line.
    double addDoubleNum;
    addDoubleNum = doubleNum + d;
    cout << fixed << setprecision(1) << addDoubleNum << '\n';
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    string fullstring;
    fullstring = s + stringName;
    cout << fullstring << '\n';

    return 0;
}
