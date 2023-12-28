#include <stdio.h>
#include <math.h>

// arithmetic
int add(int a, int b)
{
    return a + b;
}

int subtract(int a, int b)
{
    return a - b;
}

int multiply(int a, int b)
{
    return a * b;
}

int divide(int a, int b)
{
    if (b != 0)
    {
        return a / b;
    }
    else
    {
        return -1; // error case for division by zero
    }
}

// some advanced math functions
double power(double base, double exponent)
{
    return pow(base, exponent);
}

double square_root(double number)
{
    if (number < 0)
    {
        return -1; // error case for square root of negative number
    }
    return sqrt(number);
}

// utility, etc.
int factorial(int number)
{
    if (number < 0)
    {
        return -1; // error case for negative numbers
    }
    int result = 1;
    for (int i = 2; i <= number; i++)
    {
        result *= i;
    }
    return result;
}

int is_prime(int number)
{
    if (number <= 1)
    {
        return 0; // not prime
    }
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
        {
            return 0; // not prime
        }
    }
    return 1; // returnprime
}