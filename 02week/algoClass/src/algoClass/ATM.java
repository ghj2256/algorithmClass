package algoClass;

import java.util.*;

public class ATM {
	static Scanner sc = new Scanner(System.in);
	static int func(int n) {
		int answer = 0;
		int[] p = new int[n];
		for(int i = 0; i < 5; i++)
			p[i] = sc.nextInt();
		Arrays.sort(p);
		for(int i = 0; i < p.length; i++) {
			answer += (p.length - i) * p[i];
		}
		sc.close();
		return answer;
	}
	public static void main(String[] args) {
		int n = sc.nextInt();
		System.out.println(func(n));
		
		sc.close();
	}

}
