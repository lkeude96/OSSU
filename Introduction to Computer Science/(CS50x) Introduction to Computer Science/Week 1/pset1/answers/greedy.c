#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // prompt the user for amount of change
    float change;
    printf("O hai! ");
    do
    {
        printf("How much change is owed?\n");
        change = GetFloat();
    }
    while (change <= 0);
    
    // convert amount of change to cents
    int cents = round(change * 100);
    
    // track coins
    int coins = 0;
    
    while (cents > 0)
    {
        // quarter
        if (cents >= 25)
        {
            coins += cents / 25;
            cents %= 25;
        }
        
        // dime
        else if (cents >= 10)
        {
            coins += cents / 10;
            cents %= 10;
        } 
        
        // nickel
        else if (cents >= 5)
        {
            coins += cents / 5;
            cents %= 5;
        }
        
        // cent
        else
        {
            coins += cents;
            cents %= 1;
        }
    }
    
    // print the finall amount of coins
    printf("%i\n",coins);
}
