using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int num_of_words = int.Parse(Console.ReadLine());
        for(int i =0; i<num_of_words; i++)
        {
            var word = Console.ReadLine();
            for(int j=0; j<word.Length; j++)
            {
                if(j%2==0){Console.Write(word[j]);}
            }
            Console.Write(" ");
            for(int j = 0; j<word.Length; j++)
            {
                if(j%2!=0){Console.Write(word[j]);}
            }
            Console.WriteLine();
        }
    }
}

// O(n^2) this is using something like selection sort
