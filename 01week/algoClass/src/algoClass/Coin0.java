package algoClass;

import java.util.Scanner;

class Coin0 {
	static Scanner scanner = new Scanner(System.in);
	static int func(int n, int k){
		int answer = 0, coin[] = new int[n];
		for(int i=0; i<n; i++) {
			coin[i] = scanner.nextInt();
		}
		for(int i = coin.length-1; i>0; i--) {
			answer += k/coin[i];
			k %= coin[i];
		}
		scanner.close();
		return answer;
	}
	public static void main(String[] args) {
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		
		System.out.println(func(a,b));		
		scanner.close();
	}
}
