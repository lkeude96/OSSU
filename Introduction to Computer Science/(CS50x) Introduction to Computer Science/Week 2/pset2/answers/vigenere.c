#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void vigenereCipher(string plaintext, string keyword);

int main(int argc, string argv[])
{
    // Check if we have the correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./vigenere <key>\n");
        return 1;
    }

    // Get the keyword from the argv array
    string keyword = argv[1];

    // Iterate through the keyword to check if it only contents characters
    // that are in the alphabet
    for (int i = 0; i < strlen(keyword); i++)
    {
        if (!isalpha(keyword[i]))
        {
            printf("Please only use characters that are in the alphabet\n");
            return 1;
        }
    }

    // Get the plaintext from the user
    string plaintext = GetString();

    // Print the enciphered text
    vigenereCipher(plaintext, keyword);
    return 0;
}

void vigenereCipher(string plaintext, string keyword)
{
    // Keep track of the index of the characters that are in the alphabet
    int alphaCharI = 0;

    for (int i = 0; i < strlen(plaintext); i++)
    {
        // Check if the character is in the alphabet
        if (isalpha(plaintext[i]))
        {
            // Keep the index of character in the keyword
            // and wrap it as long as needed
            int keywordIndex = alphaCharI % strlen(keyword);

            int keywordCharpos = keyword[keywordIndex];
            int plaintextCharpos = plaintext[i];

            int result = 0;

            // Check if the character in the keyword is uppercase
            // and saves the position of that char in the alphabet
            if (isupper(keyword[keywordIndex]))
            {
                keywordCharpos -= 'A';
            }
            else
            {
                keywordCharpos -= 'a';
            }

            // Check if the character in the plaintext is uppercase,
            // save the position of that char in the alphabet and the result
            if (isupper(plaintext[i]))
            {
                plaintextCharpos -= 'A';
                result = ((plaintextCharpos + keywordCharpos) % 26) + 'A';
            }
            else
            {
                plaintextCharpos -= 'a';
                result = ((plaintextCharpos + keywordCharpos) % 26) + 'a';
            }
            alphaCharI++;

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
