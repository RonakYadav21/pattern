/*    *
 **
 ***
 ****
 */
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int i, j, k;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n - i; j++)
        {
            cout << " ";
        }
        for (k = n - i + 1; k <= n; k++)
        {
            cout << "*";
        }
        cout << endl;
    }

    /*
   *
   **
   ***
   ****

    */
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }

    /*
    ****
     ***
      **
       *

    */
    cout << "3";
    for (i = n; i >= 1; i--)
    {
        for (j = n - i; j > 0; j--)
        {
            cout << " ";
        }
        for (k = i; k > 0; k--)
        {
            cout << "*";
        }
        cout << endl;
    }

    /*

    ****
    ***
    **
    *

    */
    cout << "4";
    for (i = 0; i < n; i++)
    {
        for (j = 1; j <= n - i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    // or
    for (i = n; i > 0; i--)
    {
        for (j = i; j > 0; j--)
        {
            cout << "*";
        }
    }
}
