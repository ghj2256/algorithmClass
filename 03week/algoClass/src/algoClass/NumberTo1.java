package algoClass;

import java.util.*;

public class NumberTo1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		int result = 0;
		
		while(true) {
			int target = (n / k) * k;
			result += (n - target);
			if(n < k) break;
			result += 1;
			n /= k;
		}
		result += 1;
		System.out.println(result);
		
		sc.close();
	}

}
