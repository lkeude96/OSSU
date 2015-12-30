#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void caesarCipher(string plaintext, int key);

int main(int argc, string argv[])
{
    // Check if we have the correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar <key>\n");
        return 1;
    }

    // Get the key from the argv array and convert it to an int
    int key = atoi(argv[1]);

    // Get the plaintext from the user
    string plaintext = GetString();

    // Print the enciphered text
    caesarCipher(plaintext, key);
    return 0;
}

void caesarCipher(string plaintext, int key)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        // Check if the character is in the alphabet
        if (isalpha(plaintext[i]))
        {
            int result = plaintext[i] + key;

            // Check if the character is uppercased and wrap it
            if (isupper(plaintext[i]))
            {
                result = ((result - 'A') % 26) + 'A';
            }
            else
            {
                result = ((result - 'a') % 26) + 'a';
            }
            // Print the enciphered character
            printf("%c", result);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}
