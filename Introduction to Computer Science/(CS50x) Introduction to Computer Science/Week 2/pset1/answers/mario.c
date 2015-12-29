#include <cs50.h>
#include <stdio.h>

int main(void)
{
    
    int height;
    
    // prompt and validate user input
    do
    {
        printf("Height: ");
        height = GetInt();
    }
    while (height < 0 || height > 23);
    
    // draw half pyramid
    for (int row = 0; row < height; row++)
    {
        // print spaces
        for (int space = height ; space > row + 1; space--)
        {
            printf(" ");
        }
        
        // print hashes
        for (int hash = 0; hash < row + 2; hash++)
        {
            printf("#");
        }
        
        // print a new line
        printf("\n");
    }
}
