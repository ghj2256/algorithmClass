package algoClass;

import java.util.Arrays;

public class findZero {
	public static int[] func(int[] arr) {
		int j = 0;
		for(int item : arr) {
			if(item != 0) {
				arr[j] = item;
				j += 1;
			}
		}
		for(int i = j; i < arr.length; i++)
			arr[i] = 0;
		return arr;
	}

	public static void main(String[] args) {
		int[] array = {6, 0, 8, 2, 0, 0, 4, 3, 1};
		System.out.println(Arrays.toString(func(array)));
	}

}
