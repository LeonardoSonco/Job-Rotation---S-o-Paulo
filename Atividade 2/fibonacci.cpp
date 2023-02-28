#include <iostream>

using namespace std;

void calcFibonacci(int value)
{
    int lastNumbers[2];
    int currentNumber;
    for (int i = 0; i < value; i++)
    {
        if (i == 0)
        {
            cout << i << " ";
            lastNumbers[0] = i;
        }
        else if (i == 1)
        {
            cout << i << " ";
            lastNumbers[1] = i;
        }
        else
        {
            cout << lastNumbers[0] + lastNumbers[1] << " ";
            currentNumber = lastNumbers[0] + lastNumbers[1];
            lastNumbers[0] = lastNumbers[1];
            lastNumbers[1] = currentNumber;
        }
    }
}

int main()
{
    int value = 0;
    cout << "Digite um numero para ser calculado o Fibonacci = ";
    cin >> value;

    calcFibonacci(value);
    return 0;
}
