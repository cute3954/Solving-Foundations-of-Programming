package main;

public class Blackjack_main {

	public static void main(String[] args) {

		Blackjack blackjack = new Blackjack();
		
		int result = blackjack.play(22, 50);
		
		System.out.println(result);
	}
}
