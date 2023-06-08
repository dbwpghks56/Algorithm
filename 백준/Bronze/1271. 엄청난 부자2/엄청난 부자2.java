import java.math.BigInteger;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		BigInteger people;
		BigInteger money;
		
		people = sc.nextBigInteger();
		money = sc.nextBigInteger();
		
		sc.close();
		
		System.out.println(people.divide(money));
		System.out.println(people.mod(money));
		
		System.exit(0);
	}

}