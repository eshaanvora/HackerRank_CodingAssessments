//Input: aabcccaa
//Output: a4b1c3
//Output2 a2b1c3a2

import java.io.*;
import java.util.*;

public class stringCondenser {

  //Method to count specific character in string
  static Integer count(char c, String s){

    int charCount = 0;

    for (int i = 0; i <s.length(); i++){
      if (c == s.charAt(i)) charCount++;
    }
    return charCount;
  }

  static String stringCondense(String input) {
    //Attempting to create output 1
    LinkedHashMap<Character, Integer> countChars = new LinkedHashMap<Character, Integer>();
    char tmp;
    int count = 0;
    String result = "";

    //Populate dictionary with unique character values
    for (int i = 0; i < input.length(); i++) {
      tmp = input.charAt(i);
      countChars.put(tmp,1);
    }
    //Count unique characters
    for (char s : countChars.keySet()) {
      countChars.put(s, count(s, input));
    }
    for (Map.Entry<Character, Integer> entry : countChars.entrySet()) {
      //Concatenate results string
      result = result + entry.getKey() + entry.getValue();
    }
    return result;
  }

  static String compress(String s) {
    //Attempting to create output 2
    String out = "";
    int sum = 1;
    for (int i = 0; i < s.length() - 1; i++) {
        //If the next char is the equal to the current char, increase count by 1
        //Only append to results string when the current char does not equal the next char
        if (s.charAt(i) == s.charAt(i+1)) {
            sum++;
        } else {
            out = out + s.charAt(i) + sum;
            sum = 1;
        }
    }
    //Append the last char to the results string
    out = out + s.charAt(s.length() - 1) + sum;

    return out;
  }

public static void main(String[] args){

  String input = "aabcccaa";
  System.out.println(stringCondense(input));
  System.out.println(compress(input));

}

}
