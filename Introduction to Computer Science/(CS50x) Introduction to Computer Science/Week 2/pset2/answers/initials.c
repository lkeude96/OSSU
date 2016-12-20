#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void printInitial(string name);

int main(void)
{
    string name = GetString();
    printInitial(name);
}

// Print the Initials of a given name
void printInitial(string name)
{
    // Keep track of the character index in each given word in name
    int charWordI = 0;
    for (int i = 0; i < strlen(name); i++)
    {
        // Check if the current char is a space
        // which mean the next char will be the begining of a new word
        if (name[i] == ' ')
        {
            charWordI = 0;
        }
        else
        {
            // Check if the current char is the first letter in a new word
            if (charWordI == 0)
            {
                // Print the uppercased letter of the initial
                printf("%c",toupper(name[i]));
            }
            charWordI++;
        }
    }
    printf("\n");
}
