package Kattis.Java;

import java.util.Scanner;

public class TwoSum {
    // i want to add two numbers
    public static void main(String[] args) {
        int a;
        int b;
        // i want to take input from the user
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        sc.close();
        // i want to print the sum of the two numbers
        System.out.println(a + b);
    }
}
